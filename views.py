from flask import Flask,render_template,request,redirect,flash
from .app import app
import os
from .models.models import User,Profile,Post,Comment
from .database import db
from flask_login import login_user,LoginManager,login_required,current_user,logout_user
login_manager = LoginManager()
login_manager.init_app(app)

# app = Flask(__name__)
# app.secret_key = os.urandom(24)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["email"]).first()
        ##not literaly first() it's 'ONE' row data
        if user is not None and request.form["email"] == user.username and request.form["password"] == user.password:
            login_user(user)
            return redirect("/dashboard")
        else:
            flash(u"Invalid Username or Password","error")
            return redirect("/register")
    return render_template("login.html")

    

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(fullname=request.form["fullname"],
                    username=request.form["email"],
                    password=request.form["password"])
        db.session.add(user)
        db.session.commit()
        return redirect("/")
        
    return render_template("register.html")


@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():
    title="Tweet Page"
    return render_template("dashboard.html",title=title)

@app.route("/tweet",methods=["POST"])
@login_required   ## this cord means we should login first
def tweet():
    post = Post(user_id=current_user.id,post=request.form["post"])
    db.session.add(post)
    db.session.commit()
    return redirect("/profile")

@app.route("/comment",methods=["POST"])
@login_required
def comment():
    comment = Comment(post_id=request.form["id"],comment=request.form["comment"],user_id= current_user.id)
    db.session.add(comment)
    db.session.commit()
    return redirect("/profile")


@app.route("/profile",methods=["GET","POST"])
@login_required
def profile():
    title="Profile Page"
    if current_user:
        posts = Post.query.order_by(Post.created_at.desc()).all()
        # comments = db.session.query(Comment).join(User,User.id == Comment.user_id).all()
        profile = Profile.query.filter_by(id=current_user.id).first()
        user = User.query.filter_by(id=current_user.id).first()
    return render_template("profile/profile.html",title=title,posts=posts,profile=profile,user=user)

@app.route("/contacts",methods=["GET","POST"])
@login_required
def contacts():
    title="Contacts"
    if request.method == "POST":
        profiles = Profile.query.filter_by(first_name=request.form["search"]).order_by(Profile.created_at.desc()).all()
        return render_template("contacts/contacts.html",title=title,profiles=profiles)
    profiles = Profile.query.order_by(Profile.created_at.desc()).all()
    return render_template("contacts/contacts.html",title=title,profiles=profiles)

@app.route("/viewprofile/<int:id>")
def viewprofile(id):
    user = User.query.filter_by(id=id).first()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    profile = Profile.query.filter_by(user_id=id).first()
    return render_template("profile/profile.html",user=user,posts=posts,profile=profile)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@login_manager.user_loader
def Load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/about",methods=["GET","POST"])
@login_required
def about():
    if request.method == "POST":
        profile = Profile(user_id = current_user.id,
                    first_name = request.form["first_name"],
                    last_name = request.form["last_name"],
                    address = request.form["address"],
                    occupation = request.form["occupation"],
                    birthday = request.form["birthday"],
                    skills = request.form["skills"]
                    )
        db.session.add(profile)
        db.session.commit()
        return redirect("/profile")
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)
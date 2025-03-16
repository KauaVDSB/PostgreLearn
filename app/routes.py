from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@main.route("/add", methods=["POST"])
def add_user():
    nome = request.form.get("name")
    email = request.form.get("email")
    if nome and email:
        new_user = User(nome=nome, email=email)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/delete/<int:user_id>")
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("main.index"))

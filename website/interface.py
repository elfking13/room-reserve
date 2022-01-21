from flask import Blueprint, render_template

interface = Blueprint('interface',__name__)

@interface.route('/home')

def home():
    return render_template("home.html",)


@interface.route('/interface3')

def interface3():
    return render_template("interface3.html",)

@interface.route('/interface4')

def interface4():
    return render_template("interface4.html",)

@interface.route('/calendar')

def calendar():
    return render_template("calendar.html",)

from flask import Blueprint, render_template, request, redirect, url_for
from auth.guards import admin_required
from extensions import db
from models.theater import Theater, Screen

theater_bp = Blueprint("theater_bp", __name__)


@theater_bp.route("/theaters")
def theaters():
    all_theaters = Theater.query.all()
    return render_template("theaters.html", theaters=all_theaters)


@theater_bp.route("/add-theater", methods=["GET", "POST"])
@admin_required
def add_theater():

    if request.method == "POST":

        existing_theater = Theater.query.filter_by(
            name=request.form["name"],
            city=request.form["city"]
        ).first()

        if existing_theater:
            return "Theater already exists"

        theater = Theater(
            name=request.form["name"],
            city=request.form["city"],
            address=request.form["address"],
            total_screens=int(request.form["total_screens"] or 1)
        )

        db.session.add(theater)
        db.session.commit()

        return redirect(url_for("theater_bp.theaters"))

    return render_template("add_theater.html")


@theater_bp.route("/add-screen", methods=["GET", "POST"])
@admin_required
def add_screen():

    if request.method == "POST":

        existing_screen = Screen.query.filter_by(
            theater_id=int(request.form["theater_id"]),
            screen_name=request.form["screen_name"]
        ).first()

        if existing_screen:
            return "Screen already exists"

        screen = Screen(
            theater_id=int(request.form["theater_id"]),
            screen_name=request.form["screen_name"],
            total_seats=int(request.form["total_seats"])
        )

        db.session.add(screen)
        db.session.commit()

        return redirect(url_for("theater_bp.screens"))

    theaters = Theater.query.all()

    return render_template(
        "add_screen.html",
        theaters=theaters
    )

@theater_bp.route("/screens")
def screens():
    all_screens = Screen.query.all()

    return render_template(
        "screens.html",
        screens=all_screens
    )
@theater_bp.route("/edit-theater/<int:theater_id>",
                  methods=["GET","POST"])
@admin_required
def edit_theater(theater_id):

    theater = Theater.query.get_or_404(theater_id)

    if request.method == "POST":

        theater.name = request.form["name"]
        theater.city = request.form["city"]
        theater.address = request.form["address"]
        theater.total_screens = int(request.form["total_screens"] or 1)

        db.session.commit()

        return redirect("/theaters")

    return render_template(
        "edit_theater.html",
        theater=theater
    )
@theater_bp.route("/delete-theater/<int:theater_id>")
@admin_required
def delete_theater(theater_id):

    theater = Theater.query.get_or_404(theater_id)

    db.session.delete(theater)
    db.session.commit()

    return redirect("/theaters")

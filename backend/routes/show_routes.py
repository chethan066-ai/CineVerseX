from flask import Blueprint, render_template, request, redirect, url_for

from auth.guards import admin_required
from extensions import db
from models.movie import Movie
from models.theater import Theater, Screen
from models.show import Show

show_bp = Blueprint("show_bp", __name__)


@show_bp.route("/add-show", methods=["GET", "POST"])
@admin_required
def add_show():
    if request.method == "POST":
        theater_id = int(request.form["theater_id"])
        screen_id = int(request.form["screen_id"])

        screen = Screen.query.get_or_404(screen_id)
        if screen.theater_id != theater_id:
            return "Selected screen does not belong to the selected theater", 400

        show = Show(
            movie_id=int(request.form["movie_id"]),
            theater_id=theater_id,
            screen_id=screen_id,
            show_time=request.form["show_time"],
            price=float(request.form["price"])
        )

        db.session.add(show)
        db.session.commit()

        return redirect(url_for("show_bp.shows"))

    return render_template(
        "add_show.html",
        movies=Movie.query.all(),
        theaters=Theater.query.all(),
        screens=Screen.query.all()
    )


@show_bp.route("/shows")
def shows():
    all_shows = Show.query.all()
    return render_template("shows.html", shows=all_shows)

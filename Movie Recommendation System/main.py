from flask import Flask, render_template, request
import ContentFiltering
# import CollaborativeFiltering
import PopularityFiltering

# Just run main.py to start the app,
# then look for a link in the console,
# that will take you to the website

app = Flask(__name__)

def get_app_obj():
    return app

@app.route("/", methods=["GET", "POST"])
def index():
    movie_name = None
    task_type = None
    task_output = None
    if request.method == "POST":
        # Return recommended movies
        movie_name = request.form.get("movie_name")
        task_type = request.form.get("task_type")
        filtering = None
        match task_type:
            case "collab":
                print("Cannot show collaborative filtering, the feature is experiencing issues...")
                # filtering = CollaborativeFiltering.collaborative_filtering(0, movie_name)
            case "findsimilarmovies":
                filtering = ContentFiltering.ContentFiltering()
            case "findtop10movies":
                filtering = PopularityFiltering.PopularityFiltering()
                found_films: dict = filtering.top_x_movies(10)
                found_films_names: list = found_films["title"].values()
                task_output = found_films_names

    return render_template("index.html",
                           movie_name=movie_name,
                           task_type=task_type,
                           task_output=task_output)

if __name__ == "__main__":
    app.run(debug=True, port=5002)

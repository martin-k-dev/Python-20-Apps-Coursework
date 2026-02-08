from flask import Flask, render_template, request

app = Flask(__name__)

def get_app_obj():
    return app

@app.route("/", methods=["GET", "POST"])
def index():
    movie_name = None
    if request.method == "POST":
        # Return recommended movies
        movie_name = request.form.get("movie_name")
        filtering_type = request.form.get("filtering_type")
    return render_template("index.html", movie_name=movie_name)

if __name__ == "__main__":
    app.run(debug=True, port=5002)

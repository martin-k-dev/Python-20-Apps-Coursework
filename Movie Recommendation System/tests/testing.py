from flask import request
import pytest
import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to Python path
ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

# Import main.py dynamically
main_path = ROOT_DIR / "main.py"
spec = importlib.util.spec_from_file_location("main", str(main_path))
main = importlib.util.module_from_spec(spec)
sys.modules["main"] = main
spec.loader.exec_module(main)

app = main.app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Movie Recommendation System" in response.data


def test_flask_reads_form_data():
    with app.test_request_context(
            "/", method="POST",
            data={"movie_name": "Inception", "filtering_type": "popular"}
    ):
        assert request.form.get("movie_name") == "Inception"
        assert request.form["filtering_type"] == "popular"


@patch("PopularityFiltering.PopularityFiltering")
def test_top10_movies_post(mock_class, client):

	mock_instance = mock_class.return_value
	mock_instance.top_x_movies_names_only.return_value = ["Movie A", "Movie B"]

	response = client.post(
		"/",
		data={"task_type": "findtop10movies"}
	)

	assert response.status_code == 200
	assert b"Movie A" in response.data
	assert b"Movie B" in response.data


@patch("ContentFiltering.ContentFiltering")
def test_similar_movies_post(mock_class, client):

	mock_instance = mock_class.return_value
	mock_instance.similar_movies.return_value = ["Similar 1", "Similar 2"]

	response = client.post(
		"/",
		data={
			"movie_name": "Inception",
			"task_type": "findsimilarmovies"
		}
	)

	assert response.status_code == 200
	assert b"Similar 1" in response.data
	assert b"Similar 2" in response.data


def test_collab_filtering_disabled(client):
    response = client.post(
        "/",
        data={
            "movie_name": "Inception",
            "task_type": "collab"
        }
    )
    assert response.status_code == 200
    assert b"Cannot show collaborative filtering" in response.data


def test_post_without_task_type(client):
    response = client.post("/", data={"movie_name": "Inception"})
    assert response.status_code == 200


def test_invalid_task_type(client):
    response = client.post(
        "/",
        data={
            "movie_name": "Inception",
            "task_type": "invalid"
        }
    )
    assert response.status_code == 200

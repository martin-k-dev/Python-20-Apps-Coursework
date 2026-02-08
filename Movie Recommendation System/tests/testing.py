import sys

from flask import request
import pytest
import importlib.util
import sys
from pathlib import Path

# Imports the flask app from main.py
main_path = Path(__file__).parent.parent / "main.py"
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


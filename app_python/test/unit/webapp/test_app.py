import os

from app_python.test.unit.webapp import client
import app_python.app as app


def test_landing_code(client):
    landing = client.get("/")

    assert landing.status_code == 200
    
def test_landing_content(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert str(app.get_moscow_time().strftime("%H:%M:%S")) in html

def test_visits_1(client):
    landing = client.get("/visits")
    html = landing.data.decode()

    content = app.read_from_file("files/file.txt")

    assert str(content) in html

def test_visits_2(client):
    client.get("/")
    landing = client.get("/visits")
    html = landing.data.decode()

    content = app.read_from_file("files/file.txt")

    assert str(content) in html

def test_read_write_file():
    temp_file = "temp.txt"
    content = "Hello, this is a test"

    app.write_to_file(temp_file, content)
    check_content = app.read_from_file(temp_file)

    os.remove(temp_file)

    assert content == check_content

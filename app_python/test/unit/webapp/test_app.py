from app_python.test.unit.webapp import client
from app_python.app import get_moscow_time


def test_landing_code(client):
    landing = client.get("/")

    assert landing.status_code == 200
    
def test_landing_content(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert str(get_moscow_time().strftime("%H:%M:%S")) in html

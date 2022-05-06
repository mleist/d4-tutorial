import requests
from lxml import html


def test_status_code(docker_spot):
    status = 200
    url = 'http://127.0.0.1:9040/'
    response = requests.get(url)

    assert response.status_code == status


def test_about_01(docker_spot):
    response = requests.get('http://127.0.0.1:9040/about/')
    tree = html.fromstring(response.content)
    assert tree.find(".//title").text == 'About'

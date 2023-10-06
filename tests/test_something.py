import requests

from configuration import SERVICE_URL
from src.enams.global_enams import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(SERVICE_URL)
    received_posts = response.json()
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_NUMBER_OF_POSTS.value

import requests
from conf import *
from src.enums.global_enums import GlobalErrorMessages
from src.pydantic_schemas.artworks import ArtWork
from src.pydantic_schemas.search_schema import Search
from src.baseclasses.response import Response


def test_api_request():
    """ Проверка, что API возвращает корректный статус-код """
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value


def test_objects():
    # описать
    params = {'metadataDate': '2024-05-29', 'departmentIds': 1}
    response = requests.get(url='https://collectionapi.metmuseum.org/public/collection/v1/objects', params=params)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    response_data = response.json()


def test_artwork():
    response = requests.get(url=TEST_ARTWORK_URL + "5")
    artwork = Response(response)
    artwork.assert_status_code(200)
    artwork.validate(ArtWork)


def test_search():
    response = requests.get(url=TEST_SEARCH_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)
    response_test_artwork = requests.get(url=TEST_ARTWORK_URL + f"{response.json().get('objectIDs')[0]}")
    print(response_test_artwork.json().get('title'))

import requests
from conf import *
from src.enums.global_enums import GlobalErrorMessages
from src.pydantic_schemas.artworks import ArtWork
from src.pydantic_schemas.search_schema import Search
from src.pydantic_schemas.objects_id import ObjectsIDs
from src.baseclasses.response import Response


def test_api_request():
    """ Проверка, что API возвращает корректный статус-код """
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value


def test_objects():
    # описать
    response = requests.get(url=TEST_OBJECTS_URL)
    all_artworks = Response(response)
    all_artworks.assert_status_code(200)
    all_artworks.validate(ObjectsIDs)


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

    # for i in range(1, len(search_result.response_json.get('objectIDs')) + 1):
    #     response_test_artwork = requests.get(url=TEST_ARTWORK_URL + f"{response.json().get('objectIDs')[i]}")
    #     title = response_test_artwork.json().get('title').lower()
    #     assert 'sunflower' in title, "Поиск по ключевому слову возвращает некорректные результаты."


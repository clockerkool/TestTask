import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages
from src.pydantic_schemas.artworks import ArtWork
from src.pydantic_schemas.objects_id import ObjectsIDs
from src.pydantic_schemas.departments import Departments
from src.baseclasses.response import Response


def test_api_request():
    """ Проверка, что API возвращает корректный статус-код """
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value


def test_objects():
    """Проверка Objects (Возврат всех допуснимых идентификаторов объектов"""
    response = requests.get(url=TEST_OBJECTS_URL)
    all_artworks = Response(response)
    all_artworks.assert_status_code(200)
    all_artworks.validate(ObjectsIDs)


def test_artwork():
    """Проверка объекта произведения искусства."""
    response = requests.get(url=TEST_ARTWORK_URL + "5")
    artwork = Response(response)
    artwork.assert_status_code(200)
    artwork.validate(ArtWork)


def test_departments():
    """Проверка отделов произведений искусств"""
    response = requests.get(url=TEST_DEPARTMENTS_URL)
    departments = Response(response)
    departments.assert_status_code(200)
    departments.validate(Departments)





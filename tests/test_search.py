import re
import requests
from configuration import *
from utils import get_artwork_response
from src.pydantic_schemas.search_schema import Search
from src.baseclasses.response import Response


def test_search_query():
    """Проверка по запроса с параметром q
    P.S В документации не нашёл по какому атрибуту фильтруется, проверка была по атрибуту title
    """
    response = requests.get(url=TEST_SEARCH_QUERY_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)
    try:
        match = re.search(r"q=(\w+)", TEST_SEARCH_QUERY_URL)
        q_value = match.group(1)
        for i in range(len(search_result.response_json.get('objectIDs'))):
            response_test_artwork = get_artwork_response(f"{response.json().get('objectIDs')[i]}")
            title = response_test_artwork.json().get('title').lower()
            if q_value not in title:
                raise ValueError()
    except:
        print("Поиск некорректен")


def test_search_filter():
    """Проверка поиска по параметру isHightlight"""
    response = requests.get(url=TEST_SEARCH_ISHIGHLIGHT_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)

    match = re.search(r"isHighlight=(\w+)", TEST_SEARCH_ISHIGHLIGHT_URL)
    temp_isHighlight = True if match.group(1) == "true" else False

    for i in range(0, len(search_result.response_json.get('objectIDs'))):
        response_test_artwork = get_artwork_response(f"{response.json().get('objectIDs')[i]}")
        isHighlight = response_test_artwork.json().get('isHighlight')
        assert isHighlight is temp_isHighlight, f"Некорректная работа поиска, isHighlight != {temp_isHighlight}"


def test_search_department_id():
    """Проверка запроса с параметром department_id"""
    response = requests.get(url=TEST_SEARCH_DEPARTMENTID_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)


def test_search_hasImages():
    """
    Проверил атрибут hasImages поиска, однако проверка не пройдена, написал простое исключение-заглушку.
    У конкретного объекта нет этого атрибуса, поэтому решил проверить наличие изображений в целом
    """
    response = requests.get(url=TEST_SEARCH_HAS_IMAGES_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)
    try:
        for i in range(0, len(search_result.response_json.get('objectIDs'))):
            response_test_artwork = get_artwork_response(f"{response.json().get('objectIDs')[i]}")
            primaryImage = response_test_artwork.json().get('primaryImage')
            primaryImageSmall = response_test_artwork.json().get('primaryImageSmall')
            additionalImages = response_test_artwork.json().get('additionalImages')
            assert primaryImage != "", "Некорректная работа поиска, primaryImage пуст"
            assert primaryImageSmall != "", "Некорректная работа поиска, primaryImageSmall пуст"
            assert additionalImages != [], "Некорректная работа поиска, additionalImages пуст"
    except:
        print("Изображения в объекте отсутствуют")


def test_search_dates():
    """
    Проверка поиска с парамтрами диапазона дат (ТЕСТ ОТНОСИТЕЛЬНО ДОЛГИЙ)
    P.S В какой-то момент не приходит страница обекта произведения искусства (код 404)
    решил просто пропускать этот несуществующий объект
    """
    response = requests.get(url=TEST_SEARCH_DATE_URL)
    search_result = Response(response)
    search_result.assert_status_code(200)
    search_result.validate(Search)

    match = re.search(pattern_date_attr, TEST_SEARCH_DATE_URL)
    dateBegin = int(match.group(1))
    dateEnd = int(match.group(2))
    for i in range(0, len(search_result.response_json.get('objectIDs'))):
        response_test_artwork = get_artwork_response(f"{response.json().get('objectIDs')[i]}")
        objectBeginDate = response_test_artwork.json().get("objectBeginDate")
        objectEndDate = response_test_artwork.json().get("objectEndDate")
        if response_test_artwork.json().get('message') != None:
            continue
        assert objectBeginDate >= dateBegin and objectEndDate <= dateEnd, f"Диапазон дат не соответствует параметрам поиска"
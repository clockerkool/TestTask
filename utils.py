"""
Модуль, созданный во избежание дублирования кода
"""
import requests
from configuration import TEST_ARTWORK_URL


def get_artwork_response(artwork_id):
    """Получает ответ от API для объекта с заданным идентификатором."""
    return requests.get(url=TEST_ARTWORK_URL + str(artwork_id))


def check_uniqueness_id(list_id: list) -> bool:
    """Получает список с идентификаторами и проверяет, все ли они уникальны"""
    assert len(set(list_id)) == len(list_id),\
            f"Идентификаторы не уникальны: {len(set(list_id))} уникальных, {len(list_id)} всего"
    return True

def get_department_displayName(data, id):
    """Вовращает атрибут displayName(на данный момент не используется)"""
    for department in data["departments"]:
        if department["departmentId"] == id:
            display_name = department["displayName"]
            return display_name
    else:
        raise AttributeError(f"Отдела с таким ID не существует ({id})")














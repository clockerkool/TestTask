"""
Модуль, созданный во избежание дублирования кода
"""
import numpy as np

def check_uniqueness_id(list_id: list) -> bool:
    """Получает список с идентификаторами и проверяет, все ли они уникальны"""
    assert len(set(list_id)) == len(list_id),\
            f"Идентификаторы не уникальны: {len(set(list_id))} уникальных, {len(list_id)} всего"
    return True

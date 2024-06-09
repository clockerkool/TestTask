class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        """ Проверка JSON-данных в соответствии со схемой pydantic"""
        try:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    schema.model_validate(item)
            else:
                schema.model_validate(self.response_json)
        except ValueError:
            raise AssertionError("Объект не сопоставляется со схемой")

    def assert_status_code(self, status_code):
        """Проверка на корректность HTTP статуса"""
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        elif self.response_status == 404:
            raise AssertionError("Страница не найдена - 404")
        else:
            assert self.response_status == status_code, self
        return self
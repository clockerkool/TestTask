SERVICE_URL = 'https://metmuseum.github.io'
TEST_OBJECTS_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
TEST_ARTWORK_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'  # в запросе добавляю сам id
TEST_DEPARTMENTS_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/departments'
TEST_SEARCH_QUERY_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers'
TEST_SEARCH_ISHIGHLIGHT_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=sunflowers"
TEST_SEARCH_DEPARTMENTID_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=6&q=cat"
TEST_SEARCH_HAS_IMAGES_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=Auguste Renoir"
TEST_SEARCH_DATE_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?dateBegin=1700&dateEnd=1800&q=African"
pattern_date_attr = r"dateBegin=(\d+)&dateEnd=(\d+)"

import requests


def set_spn(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_s = toponym["boundedBy"]["Envelope"]
    x1, y1 = map(float, toponym_s["lowerCorner"].split())
    x2, y2 = map(float, toponym_s["upperCorner"].split())
    return [str(abs(x2 - x1)), str(abs(y2 - y1))]
def params(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    toponym_spn = \
    json_response['response']['GeoObjectCollection']['featureMember'][0][
        'GeoObject']['boundedBy']['Envelope']
    delta = list(map(lambda x: float(x), toponym_spn['upperCorner'].split()))
    delta1 = list(map(lambda x: float(x), toponym_spn['lowerCorner'].split()))
    org_point = "{0},{1}".format(toponym_longitude, toponym_lattitude)
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ','.join([str(delta[0] - delta1[0]), str(delta[1] - delta1[1])]),
        "l": "map",
        "pt": "{0},pm2dgl".format(org_point)
    }
    return map_params

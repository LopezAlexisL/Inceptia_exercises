import json
import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}'

    @classmethod
    def is_hot_in_pehuajo(cls) -> bool:
        res = requests.get(cls.url)
        if res.status_code not in (200,):
            return False
        res_json = json.loads(res.content)
        temp_kelvin = res_json['main']['temp']
        to_celsius = temp_kelvin - 273.15
        temp_celsius = round(to_celsius, 2)
        if temp_celsius <= 28:
            return False
        else:
            return True


if __name__=='__main__':
    weather = GeoAPI.is_hot_in_pehuajo()
    print(weather)
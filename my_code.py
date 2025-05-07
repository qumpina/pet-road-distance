import requests
def get_road_distance_osrm(lat1, lon1, lat2, lon2):
    url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data.get("code") != "Ok":
        raise ValueError(f"Ошибка при запросе к OSRM API: {data.get('message', 'Неизвестная ошибка')}")
    distance = data["routes"][0]["distance"]
    duration = data["routes"][0]["duration"]

    return {
        "distance_km": round(distance / 1000, 2),
        "duration_min": round(duration / 60, 2)
    }

print(get_road_distance_osrm(45.074615, 38.977694, 45.020155, 39.033117))
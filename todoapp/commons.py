import requests
import os


def weather_color(data):

    """
        Appending the temperature and weather with todo objects
         from openWeatherApi.
    """

    result = []
    for item in data:
        val = item.location.split(",")
        item = item.__dict__

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={val[0]}&lon={val[1]}&units=Metric&appid={os.environ['OPEN_WEATHER_API_KEY']}")
        item["weather"] = color_return(response.json()['weather'][0]['main'])
        if not item['is_completed']:
            item["temperature"] = round(response.json()['main']['temp'], 2)
        result.append(item)
    return result


def color_return(weather):

    """
    Will return Blue for “cold” or “rain”, Yellow-Orange for “warm” or
    “cloudy” and Red for “hot” or “sunny” and fair for all others.
    """

    if weather in ["Thunderstorm", "Drizzle", "Rain", "Snow", ]:
        return "blue"
    if weather in ["Clouds"]:
        return "yellow-orange"
    if weather in ["Clear"]:
        return "red"
    return "fair"

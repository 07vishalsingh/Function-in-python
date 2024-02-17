''''''

import requests

def get_weather_forecast(location, timeframe):
    api_key = "your-api-key"
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=7"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if timeframe == "today":
            forecast = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        elif timeframe == "tomorrow":
            forecast = data["forecast"]["forecastday"][1]["day"]["condition"]["text"]
        elif timeframe == "next_week":
            forecast = [day["day"]["condition"]["text"] for day in data["forecast"]["forecastday"][1:]]
        else:
            forecast = "Invalid timeframe. Please specify 'today', 'tomorrow', or 'next_week'."
        
        return forecast
    except Exception as e:
        return f"Error fetching weather forecast: {str(e)}"

# Example usage
location = "New York"
today_forecast = get_weather_forecast(location, "today")
print("Today's Forecast:", today_forecast)

tomorrow_forecast = get_weather_forecast(location, "tomorrow")
print("Tomorrow's Forecast:", tomorrow_forecast)

next_week_forecast = get_weather_forecast(location, "next_week")
print("Next Week's Forecast:", next_week_forecast)

import requests
import bs4


def request_page(page): 
    oResponse = requests.get(page)
    oResponseText = bs4.BeautifulSoup(oResponse.text, 'html.parser')
    location = oResponseText.select('#seven-day-forecast div h2')
    curr_weather = oResponseText.select('#current_conditions-summary p')
    forecast = oResponseText.select('div #detailed-forecast-body div div') 

    print("\n** " + " ".join((location[0].getText()).split()) + " **")
    print("Temp: " + curr_weather[1].getText())
    print("Weather: " + curr_weather[0].getText())
    print("Forecast: " + forecast[3].getText())

#oResponse = requests.get('http://forecast.weather.gov/MapClick.php?lat=33.0288&lon=-97.093')

request_page('http://forecast.weather.gov/MapClick.php?lat=30.72712770000004&lon=-95.5670632')
request_page('http://forecast.weather.gov/MapClick.php?lat=33.0288&lon=-97.093')
request_page('http://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992')
request_page('http://forecast.weather.gov/MapClick.php?lat=45.5118&lon=-122.6756')
print()

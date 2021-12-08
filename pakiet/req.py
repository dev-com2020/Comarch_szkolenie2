import requests

url = "https://api.tomorrow.io/v4/timelines"

querystring = {
    "location": "20.4002699,51.0438675",
    "fields": ["temperature", "cloudCover"],
    "units": "metric",
    "timesteps": "1d",
    "apikey": "7AUCQtiuH5mQ9F8XTYtirF5kIWZ7ARb2"}

response = requests.request("GET", url, params=querystring)

print("================")

results = response.json()['data']['timelines'][0]['intervals']
for daily_result in results:
    date = daily_result['startTime'][0:10]
    temp = round(daily_result['values']['temperature'])
    print("On", date, "it will be", temp, "C")

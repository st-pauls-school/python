import yweather 

client = yweather.Client()

london_woe = client.fetch_woeid("London, UK")
print(london_woe)
london = client.fetch_weather(london_woe)
print(london["guid"])
print(london.keys())

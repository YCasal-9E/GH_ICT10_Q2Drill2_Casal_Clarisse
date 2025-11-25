from pyscript import display 

weather_today = {
    "location": "Manila",
    "temperature_c": 32,
    "humidity": 78,
    "condition": "Sunny"
} #  specifying

display((weather_today), target='output') #  entire dictionary

display(weather_today['temperature_c'], target='output') #  temp only

weather_today['condition']='Cloudy' #  updating

weather_today['heat_index']=38 #  adding new pair, heat index represents how hot it actually feels to humans

display(weather_today, target='output')
def forecast(*args):
    weather_dict = {'Sunny': [],
                    'Cloudy': [],
                    'Rainy': []
                    }
    for destination, weather in args:
        weather_dict[weather].append(destination)

    for key in weather_dict.keys():
        weather_dict[key] = sorted(weather_dict[key])

    result = []
    for key in weather_dict.keys():
        if weather_dict[key]:
            for city in weather_dict[key]:
                result.append(f'{city} - {key}')
    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
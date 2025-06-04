import random

def generate_weather_data(days=7):
    weather_data = []
    for _ in range(days):
        temp = round(random.uniform(10, 35), 1)
        humidity = round(random.uniform(30, 90), 1)
        condition = random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])
        weather_data.append({
            "temperature": temp,
            "humidity": humidity,
            "condition": condition
        })
    return weather_data

def print_weather_report(data):
    print("Weather Forecast Report:\n")
    for i, day in enumerate(data, start=1):
        print(f"Day {i}: {day['temperature']}°C, {day['humidity']}% humidity - {day['condition']}")

print("Weather Forecast Report Generator")

if __name__ == "__main__":
    data = generate_weather_data()
    print_weather_report(data)


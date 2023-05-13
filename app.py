from flask import Flask, jsonify, json
import requests
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)

@app.route('/<city>')
def teste(city):
    api_key = os.getenv('API_KEY')
    url_city = city.replace("_", "%20")
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={url_city}&appid={api_key}")
    data = response.json()
    try:
        temp_kelvin = data['main']['temp']
        temp_max_kelvin = data['main']['temp_max']
        temp_min_kelvin = data['main']['temp_min']
        temp_celsius = round(temp_kelvin - 273.15, 2)
        temp_max_celsius = round(temp_max_kelvin - 273.15, 2)
        temp_min_celsius = round(temp_min_kelvin - 273.15, 2)
        city_name = data['name']
        country_name = data['sys']['country']
        result = {'name': city_name,
                  'temp': temp_celsius,
                  'temp_max': temp_max_celsius,
                  'temp_min': temp_min_celsius,
                  'country': country_name
                  }
    except:
        result = {"status": "erro","mensagem": "cidade não encontrada"}
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True)
import requests
APIkey='ac63c9b6fd5d825de6cf000124ac9769'


def get_data(place, forecast_days):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"

    response = requests.get(url)
    data = response.json()
    filtered_data=data['list'][:(8*forecast_days)]
    return filtered_data

# if __name__=="__main__":
#     print(get_data(place="motihari" , forecast_days=3 , view_type='Sky'))
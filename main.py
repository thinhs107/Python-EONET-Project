import random as rnd

import requests
import matplotlib.pyplot as plt
import PIL.Image
from datetime import datetime, date, timedelta

import urllib.request
import NASACONFIG

# Example of NASA get: https://api.nasa.gov/planetary/apod?api_key=vj8oVMRgUcjcA8Q1qpH3WuifG3oLOQBARWZRJ66c

def init_requests(response_url):
    try:
        response = requests.get(response_url)

        return response.json()
        response.close()
    except requests.exceptions.HTTPError as err:
        return print(SystemError(err))


if __name__ == '__main__':
    URL = NASACONFIG.URL
    API_KEY = NASACONFIG.API_KEY

    today_date = datetime.today().strftime('%Y-%m-%d')

    # "Date must be between Jun 16, 1995 and Mar 07, 2022.","service_version":"v1"}
    # Generate Random number
    start_date = datetime.strptime('1995-06-16', '%Y-%m-%d')
    end_date = datetime.strptime(today_date, '%Y-%m-%d')

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = rnd.randrange(days_between_dates)
    random_date = (start_date + timedelta(days=random_number_of_days)).strftime('%Y-%m-%d')

    # random_date = random_date.strftime('%Y-%m-%d')

    URL_PARMS = f'&date={random_date}&concept_tags=True'

    MASTER_URL = URL + API_KEY + URL_PARMS
    # print(MASTER_URL)

    # print(type(init_requests(MASTER_URL)))
    Json_data = init_requests(MASTER_URL)
    Image_data = Json_data['url']

    urllib.request.urlretrieve(Image_data, 'D:\\PycharmProjects\\pythonProject\\NasaAPI\\nasa_image.png')
    img = PIL.Image.open('nasa_image.png')
    img.show()
    print(random_date)

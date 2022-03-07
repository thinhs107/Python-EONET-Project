import Helper.InitRequest as HelperRequests
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import datetime as date


# https://eonet.gsfc.nasa.gov/api/v2.1/events

def map_output(iTitle):
    user_dataFrame = pd.read_csv('../NasaAPI/EONET.csv')
    # fig = plt.figure(figsize=(12, 9))
    m = Basemap(projection='mill',
                llcrnrlat=-90,
                urcrnrlat=90,
                llcrnrlon=-180,
                urcrnrlon=180,
                resolution='c')

    m.drawparallels(np.arange(-90., 91., 30.))
    m.drawmeridians(np.arange(-180., 181., 60.))
    m.drawmapboundary(fill_color='aqua')

    lon_x = user_dataFrame['Longitude'].tolist()
    lat_y = user_dataFrame['Latitude'].tolist()

    m.scatter(lon_x, lat_y, latlon=True)

    m.drawcoastlines()
    m.drawcounties()

    plt.title(f"{iTitle}", fontsize=20)
    plt.show()


if __name__ == '__main__':

    URL = 'https://eonet.gsfc.nasa.gov/api/v3/events'

    APIRequest = HelperRequests.CallRequest(URL)
    # print(APIRequest.Get_Requests())
    # print(type(APIRequest.Get_Requests()))

    Events = APIRequest.Get_Requests()['events']
    print(type(Events))
    title = [sub['title'] for sub in Events]
    geometries = [geo['geometry'] for geo in Events]

    coordinates = []

    for index in range(len(geometries)):
        for key in geometries[index]:
            coordinates.append(key['coordinates'])

    df = pd.DataFrame(coordinates)

    df['Longitude'] = df[0]
    df['Latitude'] = df[1]
    # df['Title'] = title
    print(df)
    #
    df.to_csv('EONET.csv', index=False)
    #
    map_output(f'Current Natural Event Happening as of {date.date.today()}')

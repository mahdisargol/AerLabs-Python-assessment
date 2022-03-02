import pandas as pd

VICINITY_RANGE = 60


def get_airport_location(airport_iata_code):
    data = pd.read_csv("airports.csv")
    airport = data[data["iata_code"]== airport_iata_code]  # extract airport record using its iata code
    return [float(airport.latitude_deg), float(airport.longitude_deg)]


def get_bounded_box(airport):
    latitude_range_degrees = (VICINITY_RANGE * 1.852) / 111.0  # convert latitude range to degrees
    longitude_range_degrees = (VICINITY_RANGE * 1.852) / 69.0  # convert longitude range to degrees
    airport_location = get_airport_location(airport)  # get air port location
    latitude = airport_location[0]
    longitude = airport_location[1]
    min_latitude = max(latitude - latitude_range_degrees, -90)  # calculate min latitude
    max_latitude = min(latitude + latitude_range_degrees, 90)  # calculate max latitude
    min_longitude = (((longitude + 180) - longitude_range_degrees) % 360) - 180  # calculate min longitude
    max_longitude = (((longitude + 180) + longitude_range_degrees) % 360) - 180  # calculate max longitude
    return [min_latitude, max_latitude, min_longitude, max_longitude]


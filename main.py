from opensky_api import OpenSkyApi
import calc

airport = input("Please enter the airport IATA code:\n")

api = OpenSkyApi()


try:
    boundedBox = calc.get_bounded_box(airport)  # extract the bounded box around the airport
    states = api.get_states(bbox=boundedBox)  # bbox = (min latitude, max latitude, min longitude, max longitude)

    airportLoc=calc.get_airport_location(airport)
    for s in states.states:
        print("(%s, %s, %r, %r, %r, %r)" % (
        s.callsign, s.origin_country, s.latitude, s.longitude, s.baro_altitude, s.velocity))

except TypeError:
    print("IATA code is invalid!")



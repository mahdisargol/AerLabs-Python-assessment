from flask import Flask
from opensky_api import OpenSkyApi
import calc

app = Flask(__name__)
api = OpenSkyApi()


@app.route('/v1/<string:iata_code>', methods=['GET'])
def get_list(iata_code):
    try:
        boundedBox = calc.get_bounded_box(iata_code)
        print(boundedBox)
        states = api.get_states(bbox=boundedBox)
        response = ''
        for s in states.states:
            response += (str(s.callsign) + ' ' + str(s.origin_country) + ' ' + str(s.latitude)
                         + ' ' + str(s.longitude) + ' ' + str(s.baro_altitude) + ' ' + str(s.velocity) + '\n')
        return response
    except TypeError:
        return "IATA code is invalid!"


if __name__ == "__main__":
    app.run(debug=True)

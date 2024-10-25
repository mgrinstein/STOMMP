from skyfield.api import load
from datetime import datetime
from config import SATELLITE_NAME

def main():
    # Load TLE data
    satellites_url = 'http://celestrak.com/NORAD/elements/weather.txt'
    satellites = load.tle_file(satellites_url)
    for satellite in satellites:
        if satellite.name == SATELLITE_NAME:
            selected_satellite = satellite
            break

    if selected_satellite:
        print(f"Selected satellite: {selected_satellite.name}")
        print(f"NORAD ID: {selected_satellite.model.satellite_number}")
        print(f"Orbital Parameters: {selected_satellite.model}")
    else:
        print("Satellite not found.")

    # Create timescale object and get current time
    ts = load.timescale()
    t = ts.now()

    # Get satellite position at the current time
    geocentric = satellite.at(t)
    subpoint = geocentric.subpoint()
    print('Latitude:', subpoint.latitude)
    print('Longitude:', subpoint.longitude)
    print('Altitude (km):', subpoint.elevation.km)

if __name__ == "__main__":
    main()
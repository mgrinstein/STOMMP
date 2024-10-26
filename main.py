from skyfield.api import load
from datetime import datetime
from config import SATELLITE_URL, SATELLITE_NAME
from load_satellite_data import load_satellite_data
from plot_satellite_position import plot_satellite_position

def main():
    satellite = load_satellite_data(SATELLITE_URL, SATELLITE_NAME)
    # Create timescale object and get current time
    ts = load.timescale()
    t = ts.now()

    # Get satellite position at the current time
    geocentric = satellite.at(t)
    subpoint = geocentric.subpoint()
    print('Latitude:', subpoint.latitude)
    print('Longitude:', subpoint.longitude)
    print('Altitude (km):', subpoint.elevation.km)

    plot_satellite_position(satellite.name, geocentric)

if __name__ == "__main__":
    main()
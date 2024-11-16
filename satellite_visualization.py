import folium
import os
from skyfield.api import load


def plot_satellite_position(satellite_data):
    # Create timescale object and get current time
    ts = load.timescale()
    time_now = ts.now()
    print(f"Time: {time_now}")
    time_now_utc = time_now.utc_strftime()
    print(f"Time utc: {time_now_utc}")



    # Get satellite position at the current time
    geocentric = satellite_data.at(time_now)
    subpoint = geocentric.subpoint()
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees
    altitude = subpoint.elevation.km
    map = folium.Map(location=[latitude, longitude], zoom_start=4)

    tooltip = f'{satellite_data.name} (Altitude: {altitude:.2f} km)'
    folium.Marker([latitude, longitude], popup=tooltip).add_to(m)

    save_map(map)


def save_map(map_object):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join('output', 'satellite_position.html')
    map_object.save(output_file)
    print(f"Map saved to {output_file}")
    return map_object

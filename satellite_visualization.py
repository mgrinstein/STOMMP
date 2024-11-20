import folium
import os
from skyfield.api import load, utc
from datetime import timedelta, datetime, timezone
import folium
import numpy as np


def plot_satellite_position(satellite_data):
    # Create timescale object and get current time
    ts = load.timescale()
    time_now = ts.now()
    print(f"Time: {time_now}")
    time_now_utc = time_now.utc_strftime()
    print(f"Time UTC: {time_now_utc}")

    # Get satellite position at the current time
    geocentric = satellite_data.at(time_now)
    subpoint = geocentric.subpoint()
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees
    altitude = subpoint.elevation.km

    # Create a folium map with restricted bounds
    map = folium.Map(
        location=[latitude, longitude],
        zoom_start=2.5,
        min_zoom=2,
        max_zoom=10,
        max_bounds=True
    )
    
    tooltip = f'{satellite_data.name} (Altitude: {altitude:.2f} km)'
    folium.Marker([latitude, longitude], popup=tooltip).add_to(map)

    # Add trajectory (next 2 hours)
    # Generate 2-hour range with 30-second intervals
    time_start = time_now.utc_datetime()
    time_end = time_start + timedelta(hours=2)
    time_range = np.linspace(time_start.timestamp(), time_end.timestamp(), num=240)
    times = ts.utc([datetime.fromtimestamp(t, tz=timezone.utc) for t in time_range])  # Add UTC timezone
    positions = [satellite_data.at(t).subpoint() for t in times]
    latitude_longitude_pairs = [(pos.latitude.degrees, pos.longitude.degrees) for pos in positions]

    # Adjust longitudes for dateline crossing
    latitude_longitude_pairs = adjust_longitudes(latitude_longitude_pairs)

    # Draw the trajectory
    folium.PolyLine(latitude_longitude_pairs, color="red", weight=2.5, opacity=1).add_to(map)

    # Save the map
    save_map(map)

def adjust_longitudes(latitude_longitude_pairs):
    adjusted_pairs = []
    previous_longitude = None
    for latitude, longitude in latitude_longitude_pairs:
        if previous_longitude is not None and abs(longitude - previous_longitude) > 180:
            if longitude > previous_longitude:
                longitude -= 360
            else:
                longitude += 360
        adjusted_pairs.append((latitude, longitude))
        previous_longitude = longitude
    return adjusted_pairs

def save_map(map_object):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join('output', 'satellite_position.html')
    try:
        map_object.save(output_file)
        print(f"Map saved to {output_file}")
    except Exception as e:
        print(f"Error saving map: {e}")
        raise
    return map_object

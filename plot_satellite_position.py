import folium
from skyfield.api import load


def plot_satellite_position(satellite_data, output_path):
    # Create timescale object and get current time
    ts = load.timescale()
    time_now = ts.now()

    # Get satellite position at the current time
    geocentric = satellite_data.at(time_now)
    subpoint = geocentric.subpoint()
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees
    altitude = subpoint.elevation.km
    m = folium.Map(location=[latitude, longitude], zoom_start=4)

    tooltip = f'{satellite_data.name} (Altitude: {altitude:.2f} km)'
    folium.Marker([latitude, longitude], popup=tooltip).add_to(m)

    save_and_display_map(m, output_path)


def save_and_display_map(map_object, output_path="satellite_position.html"):
    map_object.save(output_path)
    print(f"Map saved to {output_path}")
    return map_object

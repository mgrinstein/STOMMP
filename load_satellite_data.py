from skyfield.api import load

def load_satellite_data(satellites_url, satellite_name): 
    satellites = load.tle_file(satellites_url)
    for satellite in satellites:
        if satellite.name == satellite_name:
            selected_satellite = satellite
            break

    if selected_satellite:
        print(f"Selected satellite: {selected_satellite.name}")
        print(f"Model: {selected_satellite.model}")
        print(f"Orbital Parameters: {selected_satellite.model}")
        return selected_satellite
    else:
        print("Satellite not found.")
        return None

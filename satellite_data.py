from skyfield.api import EarthSatellite, load

def fetch_tle_data(url):
    import requests
    
    print(f"Fetching TLE data from {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        tle_data = response.text.strip().split('\n')
        if len(tle_data) % 3 != 0:
            raise ValueError(f"TLE data fetched from {url} is incomplete.")
        return tle_data
    except requests.RequestException as e:
        print(f"Failed to fetch TLE data from {url}: {e}")
        return ''
    except ValueError as e:
        print(e)
        return ''

def parse_satellite_data(tle_data):
    satellites = []
    for i in range(0, len(tle_data), 3):
        satellite_name = tle_data[i].strip()
        line1 = tle_data[i + 1].strip()
        line2 = tle_data[i + 2].strip()
        satellite = EarthSatellite(line1, line2, satellite_name)
        satellites.append(satellite)
    return satellites

def load_satellite_data(satellite_sources, desired_satellite): 
    selected_satellite = None
    
    for category_name, category_url in satellite_sources.items():
        try:
            satellites_in_category = fetch_tle_data(category_url)
            parsed_satellites = parse_satellite_data(satellites_in_category)
            print(f"Successfully fetched {len(parsed_satellites)} satellites.")
            
            for satellite in parsed_satellites:

                if satellite.name == desired_satellite:
                    print(f"Found satellite {desired_satellite} in source: {category_name} ({category_url})")
                    selected_satellite = satellite
                    break
            if selected_satellite:
                break
        except Exception as e:
            print(f"Failed to load TLE data from {category_name} ({category_url}): {e}")
            continue

    if selected_satellite:
        return selected_satellite
    else:
        print(f"Satellite {desired_satellite} not found in any of the provided sources.")
        return None

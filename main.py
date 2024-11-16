from config import CELESTRACK_SATELLITE_GROUPS, SATELLITE_NAME, FORMAT
from satellite_data import load_satellite_data
from satellite_visualization import plot_satellite_position

def main():
    satellite_data = load_satellite_data(CELESTRACK_SATELLITE_GROUPS, SATELLITE_NAME, FORMAT)
    plot_satellite_position(satellite_data)

if __name__ == "__main__":
    main()
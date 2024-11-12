from config import CELESTRACK_SATELLITE_SOURCES, SATELLITE_NAME, OUTPUT_PATH
from satellite_data import load_satellite_data
from satellite_visualization import plot_satellite_position

def main():
    satellite_data = load_satellite_data(CELESTRACK_SATELLITE_SOURCES, SATELLITE_NAME)
    plot_satellite_position(satellite_data, OUTPUT_PATH)

if __name__ == "__main__":
    main()
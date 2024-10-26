from config import SATELLITE_URL, SATELLITE_NAME, OUTPUT_PATH
from load_satellite_data import load_satellite_data
from plot_satellite_position import plot_satellite_position

def main():
    satellite_data = load_satellite_data(SATELLITE_URL, SATELLITE_NAME)
    plot_satellite_position(satellite_data, OUTPUT_PATH)

if __name__ == "__main__":
    main()
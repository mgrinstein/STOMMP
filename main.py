from satellite_data import load_satellite_data
from satellite_visualization import plot_satellite_position

def main():
    satellite_data = load_satellite_data()
    plot_satellite_position(satellite_data)

if __name__ == "__main__":
    main()
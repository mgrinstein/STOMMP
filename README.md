# SETTLE - Satellite Element Tracking via TLE

**SETTLE** is a Python-based tool for tracking satellite positions using Two-Line Element (TLE) data and visualizing satellite positions on an interactive map. The project leverages the `Skyfield` library to compute satellite orbits from TLE data and `folium` for map visualization, allowing for real-time plotting of selected satellite positions.

## Features
- Retrieve and process satellite TLE data from Celestrak.
- Calculate and plot the orbit of a selected satellite on a map.
- Dynamic visualization of satellite positions using TLE data.
- User-defined output for map file generation.
- Easy-to-extend modular design, allowing additional features or data sources.

### Plot output example
<figure>
<img
        src="examples/NOAA_19_example.png" 
        width=30%
        title="Example"
/>
<figcaption>Example: a plot of NOAA 19's position at tt=2460610.1853677994.</figcaption>
</figure>

## Installation

To get started with **SETTLE**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/mgrinstein/SETTLE.git
cd SETTLE
pip install -r requirements.txt
```
## Usage


To run **SETTLE**, customize the `config.py` file to have the desired `SATELLITE_NAME`:

```python
# config.py
SATELLITE_NAME = "YourSatelliteName"
```

Then, run `main`:
```bash
python main.py
# STOMMP - Satellite Tracking via OMM-state Propagation

**STOMMP** is a Python-based tool for tracking satellite positions using Orbit Mean-Elements Message (OMM) data and visualizing satellite positions on an interactive map. The project leverages the `Skyfield` library to compute satellite orbits from OMM data and `folium` for map visualization, allowing for real-time plotting of selected satellite positions.

## Features
- Retrieve and process satellite OMM data from Celestrak.
- Calculate and plot the orbit of a selected satellite on a map.
- Dynamic visualization of satellite positions.
- User-defined output for map file generation.
- Easy-to-extend modular design, allowing additional features or data sources.

<!-- ### Plot output example
<figure>
<img
        src="examples/NOAA_19_example.png" 
        width=30%
        title="Example"
/>
<figcaption>Example: a plot of NOAA 19's position at tt=2460610.1853677994 (2024-10-26 16:25:47 UTC).</figcaption>
</figure> -->

## Installation

To get started with **STOMMP**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/mgrinstein/STOMMP.git
cd STOMMP
pip install -r requirements.txt
```
## Usage


To run **STOMMP**, customize the `config.py` file to have the desired `SATELLITE_NAME`:

```python
# config.py
SATELLITE_NAME = "YourSatelliteName"
```

Then, run `main`:
```bash
python main.py
```

## Alternative - Tracking via TLE
This project has originated from [SETTLE](https://github.com/mgrinstein/SETTLE), which propagates TLE data instead of OMM-state.
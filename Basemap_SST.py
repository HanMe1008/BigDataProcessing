### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset

# Load the NetCDF data
data = Dataset('F:\BigDataProcessing\KHOA_SST_20231008.nc')

# Extract Longitude, Latitude, and SST data
lons = data['lon'][:]
lats = data['lat'][:]
sst = data['sst'][:]

# Handle dimensions if necessaray
if sst.ndim == 3:
    sst = sst[0]

# Define Longitude and Latitude limits
lon_min, lon_max = 126.0, 142.0
lat_min, lat_max = 33.0, 49.0

# Create a Basemap instance
m = Basemap(projection='merc',
            llcrnrlat=lat_min,
            urcrnrlat=lat_max,
            llcrnrlon=lon_min,
            urcrnrlon=lon_max,
            resolution='i')

# Create grid for mapping, filtering based on the defined limits
lon_idx = np.where((lons >= lon_min) & (lons <= lon_max))[0]
lat_idx = np.where((lats >= lat_min) & (lats <= lat_max))[0]

# Extract the relevant SST data
lons_filtered = lons[lon_idx]
lats_filtered = lats[lat_idx]
sst_filtered = sst[np.ix_(lat_idx, lon_idx)]


plt.figure(figsize=(10,10))

# Draw coastlines and countries 
m.drawcoastlines()
m.drawcountries()

# Adjust the spacing of parallels and meridians
parallels_interval = 3  # Latitude interval
meridians_interval = 3  # Longitude interval

# Generate latitude and longitude values
parallels = np.arange(np.floor(np.min(lats)), np.ceil(np.max(lats)), parallels_interval)
meridians = np.arange(np.floor(np.min(lons)), np.ceil(np.max(lons)), meridians_interval)

# Draw parallels
m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=6)

# Draw meridians
m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=6)  

# Create grid for mapping
lon, lat = np.meshgrid(lons_filtered, lats_filtered)
x, y = m(lon, lat)

# Plot SST data
c = m.pcolormesh(x, y, sst_filtered, cmap='jet', shading='auto')

# Add colorbar and title
plt.colorbar(c, label='Sea Surface Temperature (°C)')
plt.title('Sea Surface Temperature in the EastSea (2023-10-08)', fontsize=12)

plt.show()

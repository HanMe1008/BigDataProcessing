## 1) CHL (NMEW) 시각화
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset, num2date

# Input file and data visualization settings
file = 'F:\\BigDataProcessing\\GS202207_CHL_NW_month.nc'
varname = 'chlor_a'
font_size = 20
cmin, cmax = 0.01, 100

# Use log norm for chlorophyll-a data
norm = colors.LogNorm(vmin=cmin, vmax=cmax)

# Read the Dataset and Geo-ref data
with Dataset(file, 'r') as nc:
    sds = nc[varname][:]  # the output is a numpy masked array
    sds = np.ma.squeeze(sds)  # Remove singleton dimensions
    lat = nc['lat'][:]
    lon = nc['lon'][:]
    time = num2date(nc['time'][:], units=nc['time'].units, calendar=nc['time'].calendar)[0]  # Assuming single time
    label = nc[varname].long_name.split(',')[0] + ' [mg m-3]'  # Extract variable name and unit

# Visualization without basemap
plt.figure(figsize=(12, 10))
extent = [lon.min(), lon.max(), lat.min(), lat.max()]

# Land mask
land_mask = np.where(~sds.mask, np.nan, 1)

# Plot the land mask
plt.imshow(land_mask, cmap='gray', extent=extent, alpha=0.3, origin='upper')

# Plot the chlorophyll-a data
im = plt.imshow(sds, extent=extent, norm=norm, cmap='jet', origin='upper')

# Colorbar
cbar = plt.colorbar(im, label='Chlorophyll-a Concentration (mg m$^{-3}$)')
cbar.ax.tick_params(labelsize=font_size - 4)

# Add title and labels
plt.title(f'Chlorophyll-a Concentration at {time.strftime("%Y-%m")}', fontsize=font_size)
plt.xlabel('Longitude (°E)', fontsize=font_size)
plt.ylabel('Latitude (°N)', fontsize=font_size)
plt.xticks(fontsize=font_size - 4)
plt.yticks(fontsize=font_size - 4)

plt.grid(visible=True, linestyle='--', alpha=0.5)
"""
# Save the plot
output_file = f'Chlorophyll-a {time:%Y-%m}.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"그림이 '{output_file}'로 저장되었습니다.")
"""
plt.show()



## 2) CHL (NMEW) in ROI 시각화
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset, num2date
from adjustText import adjust_text

# Input file and data visualization settings
file = 'F:\\BigDataProcessing\\GS202207_CHL_NW_month.nc'
varname = 'chlor_a'
font_size = 20
cmin, cmax = 0.01, 100

# Use log norm for chlorophyll-a data
norm = colors.LogNorm(vmin=cmin, vmax=cmax)

# Read the Dataset and Geo-ref data
with Dataset(file, 'r') as nc:
    sds = nc[varname][:]  # the output is a numpy masked array
    sds = np.ma.squeeze(sds)  # Remove singleton dimensions
    lat = nc['lat'][:]
    lon = nc['lon'][:]
    time = num2date(nc['time'][:], units=nc['time'].units, calendar=nc['time'].calendar)[0]  # Assuming single time
    label = nc[varname].long_name.split(',')[0] + ' [mg m-3]'  # Extract variable name and unit

# 범위 설정
lat_min, lat_max = 34.3, 37.3
lon_min, lon_max = 128, 131

# 위도, 경도 범위에 맞는 인덱스 선택
lat_idx = np.where((lat >= lat_min) & (lat <= lat_max))[0]
lon_idx = np.where((lon >= lon_min) & (lon <= lon_max))[0]

# 선택된 범위에 해당하는 데이터 자르기
sds_subset = sds[lat_idx.min():lat_idx.max()+1, lon_idx.min():lon_idx.max()+1]
lat_subset = lat[lat_idx]
lon_subset = lon[lon_idx]

# Visualization
plt.figure(figsize=(12, 10))
extent = [lon_subset.min(), lon_subset.max(), lat_subset.min(), lat_subset.max()]

# Land mask
land_mask = np.where(~sds_subset.mask, np.nan, 1)

# Plot the land mask
plt.imshow(land_mask, cmap='gray', extent=extent, alpha=0.3, origin='upper')

# Plot the chlorophyll-a data
im = plt.imshow(sds_subset, extent=extent, norm=norm, cmap='jet', origin='upper')

# Colorbar
cbar = plt.colorbar(im, label='Chlorophyll-a Concentration (mg m$^{-3}$)')
cbar.ax.tick_params(labelsize=font_size - 4)

# Add labels for each point
labels = ['Pohang','Gampo', 'Ulgi']
llon = [129.343, 129.501, 129.431]
llat = [36.019, 35.805, 35.4927]

# 텍스트 객체 생성
texts = [plt.text(xpt, ypt, label, fontsize=12, ha='center', va='bottom', color='blue')
         for label, xpt, ypt in zip(labels, llon, llat)]

# 레이블 중복 해결
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

# Plot the points
plt.plot(llon, llat, 'bo', markersize=5, label='Point of Interest')

# Add title and labels
plt.title(f'Chlorophyll-a Concentration at {time.strftime("%Y-%m")}', fontsize=font_size)
plt.xlabel('Longitude (°E)', fontsize=font_size)
plt.ylabel('Latitude (°N)', fontsize=font_size)
plt.xticks(fontsize=font_size - 4)
plt.yticks(fontsize=font_size - 4)

plt.grid(visible=True, linestyle='--', alpha=0.5)

"""
# Save the plot
output_file = f'Chlorophyll-a_{time:%Y-%m}_ROI.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"그림이 '{output_file}'로 저장되었습니다.")
"""
plt.show()

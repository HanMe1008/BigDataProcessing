## 1) 바람 벡터 (eastward_wind & northward_wind) 시각화
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature


# 파일
file_path = 'F:\BigDataProcessing\wind_monthly_202207.nc'
dataset = xr.open_dataset(file_path, mode='r', engine='netcdf4')


# 변수
eastward_wind = dataset['eastward_wind'][0,:,:].values     # (time, latitude, longitude)
northward_wind = dataset['northward_wind'][0,:,:].values   # (time, latitude, longitude)
wind_speed = dataset['wind_speed'][0,:,:].values           # (time, latitude, longitude)

time = dataset['time'][0].values
lon = dataset['longitude'].values
lat = dataset['latitude'].values

# 시각화
plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# 벡터 화살표 추가
plt.quiver(lon[::3], lat[::3], eastward_wind[::3, ::3], northward_wind[::3, ::3], 
           scale=100, transform=ccrs.PlateCarree(), color='red')

# 지도 요소 추가
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.set_title(f'Wind Vectors at {np.datetime_as_string(time, unit="M")}', fontsize=16)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()



## 2) 바람 벡터 in ROI (eastward_wind & northward_wind) 시각화
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from adjustText import adjust_text

# 파일 
file_path = 'F:\BigDataProcessing\wind_monthly_202207_ROI.nc'
dataset = xr.open_dataset(file_path, mode='r')

# 변수
eastward_wind = dataset['eastward_wind'][0,:,:].values     # (time, latitude, longitude)
northward_wind = dataset['northward_wind'][0,:,:].values   # (time, latitude, longitude)
wind_speed = dataset['wind_speed'][0,:,:].values           # (time, latitude, longitude)

time = dataset['time'][0].values
lon = dataset['longitude'].values
lat = dataset['latitude'].values

# 시각화
plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# 벡터 화살표 추가
plt.quiver(lon, lat, eastward_wind, northward_wind, 
           scale=30, transform=ccrs.PlateCarree(), color='red')

# 지도 요소 추가
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.set_title(f'Wind Vectors at {np.datetime_as_string(time, unit="M")}', fontsize=16)

# Add labels for each point
labels = ['Pohang','Gampo', 'Ulgi']
llon = [129.343, 129.501, 129.431]
llat = [36.019, 35.805, 35.4927]

# 텍스트
texts = [plt.text(xpt, ypt, label, fontsize=12, ha='center', va='bottom', color='blue')
         for label, xpt, ypt in zip(labels, llon, llat)]

# 레이블 중복 해결
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

# Plot the points
plt.plot(llon, llat, 'bo', markersize=5, label='Point of Interest')

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


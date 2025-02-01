## 1) SST (KHOA) 시각화 - contour
import netCDF4 as nc 
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from adjustText import adjust_text

# 데이터 경로
data = nc.Dataset('F:\\BigDataProcessing\\KHOA_SST_L4_Z003_D01_WGS001K_U20220715.nc')

# 변수
time = data['time'][:].data
lon = data['lon'][:].data
lat = data['lat'][:].data
sst = data['sst'][:].data

# 데이터 필터링
sst_tmp = sst[sst > -999]
sst_min = np.nanmin(sst_tmp)
sst_max = np.nanmax(sst_tmp)

# 'time' 데이터 변환 (시작시간 + 경과시간)
time_since_str = data['time'].units     
time_since_str = time_since_str[12:31]  
time_str = dt.datetime.strptime(time_since_str, '%Y-%m-%d %H:%M:%S') + dt.timedelta(hours=int(time[0]))

# 경위도 좌표를 격자 형태로 변환
meshlon, meshlat = np.meshgrid(lon, lat)

# NetCDF 파일의 data dimension 변경
d, r, c = sst.shape
sst = np.squeeze(sst)

# 관심 영역(ROI) 설정
# bbox = [126, 132, 33.5, 37.5]  # [min_lon, max_lon, min_lat, max_lat]
bbox = [129, 130, 35.3, 36.3]  # 동해남부해역

cond = (bbox[0] < meshlon) & (meshlon < bbox[1]) & (bbox[2] < meshlat) & (meshlat < bbox[3])
sst[~cond] = np.nan

# 관심 영역 이외의 데이터 삭제
cond_x = np.sum(cond, axis=0) != 0
cond_y = np.sum(cond, axis=1) != 0
rev_r, rev_c = np.sum(cond_x), np.sum(cond_y)

rev_sst = sst[~np.isnan(sst)].reshape(rev_r, rev_c)
rev_meshlon = meshlon[~np.isnan(sst)].reshape(rev_r, rev_c)
rev_meshlat = meshlat[~np.isnan(sst)].reshape(rev_r, rev_c)

# 가시화
levels = np.arange(np.floor(sst_min), np.ceil(sst_max) + 1, 1) 

plt.figure(figsize=(12,8))
ax = plt.axes(projection=ccrs.PlateCarree())

contour_fill = plt.contourf(rev_meshlon, rev_meshlat, rev_sst, cmap='jet', levels=levels, vmin=5, vmax=30)

plt.colorbar(label='SST (°C)')

contour_line = plt.contour(rev_meshlon, rev_meshlat, rev_sst, colors='black', levels=levels, linewidths=0.5)

# 지도 요소 추가
# ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.set_title(f'Sea Surface Temperature at {time_str:%Y-%m-%d}')

# 경도와 위도 범위 및 라벨 추가
ax.set_xticks(np.arange(bbox[0], bbox[1], 0.2), crs=ccrs.PlateCarree())  # 경도 범위
ax.set_yticks(np.arange(bbox[2], bbox[3] , 0.1), crs=ccrs.PlateCarree())  # 위도 범위
ax.set_xlabel('Longitude (°E)')
ax.set_ylabel('Latitude (°N)')

plt.clabel(contour_line, inline=True, fontsize=7, fmt='%d', inline_spacing=10)

# Add labels for each point
labels = ['Pohang','Gampo', 'Ulgi']
llon = [129.343, 129.501, 129.431]
llat = [36.019, 35.805, 35.4927]

texts = [ax.text(xpt, ypt, label, transform=ccrs.PlateCarree(),
                 fontsize=12, ha='center', va='bottom', color='blue')
        for label, xpt, ypt in zip(labels, llon, llat)]

# label 중복해결
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

# Plot the point
ax.plot(llon, llat, 'bo', markersize=5,
        transform=ccrs.PlateCarree(), label='Point of Interest')
"""
# 그림 저장
output_file = f'SST {time_str:%Y-%m-%d} contour ROI.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"그림이 '{output_file}'로 저장되었습니다.")
"""
plt.show()

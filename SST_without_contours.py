### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297

## 1) 등고선 없는 SST 가시화 
import netCDF4 as nc 
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

# 데이터 경로 설정
data = nc.Dataset('F:\BigDataProcessing\KHOA_SST_20231008.nc')

# 변수 추출
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

# 관심 영역(ROI) 추출
bbox = [117, 150, 20, 53]
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
plt.figure(figsize=(10,8))

plt.pcolor(rev_meshlon, rev_meshlat, rev_sst, cmap='jet', vmin=sst_min, vmax=sst_max)
plt.colorbar(label='SST (°C)')

plt.xlabel('Longitude (°E)')
plt.ylabel('Latitude (°N)')
plt.title('SST in the NorthWest Pacific Ocean (08.Oct.2023)')

plt.show()

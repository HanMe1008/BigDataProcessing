### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297

### 실습 5
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("VD.csv")  

theta = np.radians(df['dir'])

plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(8,8) ,subplot_kw={'projection': 'polar'})

ax.scatter(theta, df['speed'], marker='x', color='red', s=10, alpha=0.5, label='Yeongheung')

max_speed = df['speed'].max()
min_speed = df['speed'].min()
mean_speed = df['speed'].mean()

# 최대 속도
max_theta = theta[df['speed'].idxmax()]
ax.annotate(f'Max Speed\n {max_speed:.2f} m/s', 
             xy=(max_theta, max_speed), 
             xytext=(max_theta + 0.1, max_speed + 0.5),
             xycoords='data',
             arrowprops=dict(facecolor='black', shrink=0.05), 
             fontsize=8, color='black', ha='left', va='bottom')

# 최소 속도
min_theta = theta[df['speed'].idxmin()]
ax.annotate(f'Min Speed\n {min_speed:.2f} m/s', 
             xy=(min_theta, min_speed), 
             xytext=(min_theta - 0.1, min_speed + 0.2),
             xycoords='data', 
             arrowprops=dict(facecolor='red', shrink=0.05), 
             fontsize=8, color='black', ha='left', va='bottom')

# 평균 속도
mean_theta = theta[(df['speed'] - mean_speed).abs().idxmin()]
ax.annotate(f'Mean Speed\n {mean_speed:.2f} m/s', 
             xy=(mean_theta, mean_speed), 
             xytext=(mean_theta + 1.0, mean_speed + 0.1),
             xycoords='data',  
             arrowprops=dict(facecolor='blue', shrink=0.05), 
             fontsize=8, color='black', ha='left', va='bottom')

ax.set_title("Current Rose Plot", loc='left', va='top', fontsize=14)

ax.set_theta_zero_location('N') 
ax.set_theta_direction(-1)       

plt.legend(loc='upper left', bbox_to_anchor=(-0.01, 1.0), fontsize=10)

ax.grid(True)

ax.set_yticks(np.arange(0, 2.5, 0.5)) 
ax.tick_params(axis='both', labelsize=8)  

plt.show()

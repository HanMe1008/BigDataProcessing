### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib import cm
from matplotlib.colors import Normalize

### 실습 3

df = pd.read_csv("VD.csv")

df['speed_x'] = df['speed'] * np.sin(np.radians(df['dir']))
df['speed_y'] = df['speed'] * np.cos(np.radians(df['dir']))

df['polar_speed'] = np.sqrt(df['speed_x']**2 + df['speed_y']**2)

plt.scatter(df['speed_x'], df['speed_y'], marker='.', c=df['speed'])
plt.axis('equal')

plt.title('Scatter Plot (current Speed vs. Direction)')

plt.xlabel('speed_x')
plt.ylabel('speed_y')

plt.grid(True, color='gray', alpha=0.3, linewidth=0.5)

## SI 4 : Color Mapping
# 1. DataFrame에 색상열 추가
cbar = plt.colorbar()
cbar.set_label('Speed (m/sec)')

plt.show()
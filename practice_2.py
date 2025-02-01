### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Headless 환경에서 사용할 수 있는 백엔드
import matplotlib.pyplot as plt

### 실습 2

df = pd.read_csv("VD.csv")

df['speed_x'] = df['speed'] * np.sin(np.radians(df['dir']))
df['speed_y'] = df['speed'] * np.cos(np.radians(df['dir']))

df['polar_speed'] = np.sqrt(df['speed_x']**2 + df['speed_y']**2)

plt.scatter(df['speed_x'], df['speed_y'], marker='.')
plt.axis('equal')

## SI 3 : Plot 정의 추가
# 1. 제목
plt.title('Scatter Plot (current Speed vs. Direction)')

# 2. Label
plt.xlabel('speed_x')
plt.ylabel('speed_y')

# 3. Grid line
plt.grid(True, color='gray', alpha=0.3, linewidth=0.5)

plt.show()



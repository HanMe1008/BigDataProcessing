### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib import cm
from matplotlib.colors import Normalize

### 실습 1

## Step 1 : 데이터 구성( Data Loading )
# 1. 데이터 읽기 (CSV 파일)

df = pd.read_csv("VD.csv")

# 2. DataFrame의 처음 몇 행 유형 인쇄
print(df.head())
print(df.head().dtypes)

# 3. 올바르게 load check
print(df.info())

## Step 2 : 데이터 변환 ( Data Transformation )
# 1. Cartesian coordinate 계산 (방향을 라디안 단위로 변환)
df['speed_x'] = df['speed'] * np.sin(np.radians(df['dir']))
df['speed_y'] = df['speed'] * np.cos(np.radians(df['dir']))

# 2. Polar coordinate 이용
df['polar_speed'] = np.sqrt(df['speed_x']**2 + df['speed_y']**2)

## Step 3 : Plotting
# 1. speed_x, speed_y를 좌표로 하는 산점도 작성
plt.scatter(df['speed_x'], df['speed_y'], marker='.')
plt.show()

# 2. 종횡비 동일하게
plt.scatter(df['speed_x'], df['speed_y'], marker='.')
plt.axis('equal')
plt.show()
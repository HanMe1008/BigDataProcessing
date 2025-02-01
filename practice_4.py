### 빅데이터처리:해양환경 
## 해양학전공 전상규 202013297

### 실습 4
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv("VD.csv")  

theta = np.radians(df['dir'])

plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(8,8),subplot_kw={'projection': 'polar'})

ax.scatter(theta, df['speed'], marker='x', color='red', s=10, alpha=0.5, label='Yeongheung')

ax.set_title("Current Rose Plot", va='top', fontsize=8)  

ax.set_theta_zero_location('N')  
ax.set_theta_direction(-1)        

plt.legend(loc='upper right', fontsize=5) 

ax.grid(True)

ax.set_yticks(np.arange(0, 2.5, 0.5)) 
ax.tick_params(axis='both', labelsize=8)  

plt.show()
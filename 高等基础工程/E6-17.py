#!/usr/bin/python  
#coding: utf-8  

# 也可以设置两个x轴，方法和双y轴相同，要把plot中对应的x和y互换，这样显示的结果和双y轴基本相同

import numpy as np  
import matplotlib.pyplot as plt  
  
PI = 30
# 土重度
y = 16
# 附加荷载 50 Kpa
surchange = 50 

sigma_v =  [0]*9
sigma_vp = [0]*9
OCR = [0]*9
Su =  [0]*9

x = [0.5,1,2,5,10,20,30,40,50] 

for i in range(9):
	sigma_v[i] = x[i]*(16-9.8)
	sigma_vp[i] = sigma_v[i] + surchange
	OCR[i] = sigma_vp[i] / sigma_v[i]
	Su[i] = (0.11+0.0037*PI)*OCR[i]**0.8*sigma_v[i]
  
fig = plt.figure()  
ax1 = fig.add_subplot(111)  
Su, = ax1.plot(Su, x, label="Su",color="r",marker='o')  
#ax1.legend(loc='center right')  
# 设置对应坐标轴的名称  
ax1.set_ylabel("Depth(m)") 

ax1.set_xlabel("Undrained shear strength(Kpa)") 

# x轴反向显示
fig.gca().invert_yaxis()
  
# 添加坐标轴,并在新添加的坐标轴中画y2 = log(x)图像  
ax2 = plt.twiny()  
ax2.set_xlabel("OCR")  

OCR, = ax2.plot(OCR, x, label="OCR",marker='o',linestyle='--') 

plt.legend([Su, OCR], ["Su", "OCR"], loc='center right') 
  
plt.show()  
  

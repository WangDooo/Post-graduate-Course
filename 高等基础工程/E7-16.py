#!/usr/bin/python  
#coding: utf-8  

# 也可以设置两个x轴，方法和双y轴相同，要把plot中对应的x和y互换，这样显示的结果和双y轴基本相同

import numpy as np  
import matplotlib.pyplot as plt  
  
depth = [0.05,1.05,2.05,3.05,4.05,5.05,6.05,7.05,8.05,8.8] 
qc1 = [1.29,2.48,4.60,4.22,2.61,3.50,17.84,12.81,3.88,22.41]
fs1 = [55.87,114.24,19.17,30.76,12.11,92.06,76.01,158.43,80.91,115.62]
fsqc1 = [4.3,4.6,0.4,0.7,0.5,2.6,0.4,1.2,2.1,0.5]
qc2 = [1.5,2.0,3.4,4.2,2.9,3.6,19.9,12.4,3.4,21.0]
fs2 = [38.39,96.19,45.43,36.64,21.48,72.49,73.28,228.13,75.85,68.01]
fsqc2 = [2.6,4.9,1.3,0.9,0.7,2.0,0.4,1.8,2.2,0.3]

# print(len(depth),len(qc1),len(fs1),len(fsqc1),len(qc2),len(fsqc2),len(fs2))


  
fig = plt.figure()  
ax1 = fig.add_subplot(111)  

ax2 = plt.twiny()  
ax2.set_xlabel("fs/qc(%)")
qc1, = ax2.plot(fsqc2, depth, label="fs/qc",color="black",marker='o')  
ax2.legend(loc='top right')  
# 设置对应坐标轴的名称  
ax1.set_ylabel("Depth(m)") 

ax1.set_xticks([]) 
 
# x轴反向显示
fig.gca().invert_yaxis()
  
plt.show()  
  

#!/usr/bin/python  
#coding: utf-8  

# 也可以设置两个x轴，方法和双y轴相同，要把plot中对应的x和y互换，这样显示的结果和双y轴基本相同

import numpy as np  
import matplotlib.pyplot as plt  
  
x = [0.5,1,2,5,10,20,30,40,50] 
OCR = [17,9,5,2.6,1.8,1.4,1.27,1.2,1.16]  
Su = [6.65,8,10,15,22,36,50,63,77]
  
fig = plt.figure()  
ax1 = fig.add_subplot(111)  
Su, = ax1.plot(Su, x, label="Su",color="r",marker='o')  
#ax1.legend(loc='center right')  
# 设置对应坐标轴的名称  
ax1.set_ylabel("Depth(m)") 

ax1.set_xlabel("Undrained shear strength(Kpa)")  s 

# x轴反向显示
fig.gca().invert_yaxis()
  
# 添加坐标轴,并在新添加的坐标轴中画y2 = log(x)图像  
ax2 = plt.twiny()  
ax2.set_xlabel("OCR")  

OCR, = ax2.plot(OCR, x, label="OCR",marker='o',linestyle='--') 

plt.legend([Su, OCR], ["Su", "OCR"], loc='center right') 
  
plt.show()  
  

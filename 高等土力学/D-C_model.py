import numpy as np  
import matplotlib.pyplot as plt  

x = [1,2,4,6,8,10,12,14,16] 
sigma_200 = [100,125,150,166,175,179,180,186,187]
sigma_300 = [150,179,210,230,237,247,253,253,253]
y_200 = [0] * len(x)
y_300 = [0] * len(x)

for i in range(len(x)):
	y_200[i] = x[i] / sigma_200[i]
	y_300[i] = x[i] / sigma_300[i]

# plt.style.use('ggplot')

fn_200 = np.poly1d(np.polyfit(x,sigma_200 ,deg=2))
fn_300 = np.poly1d(np.polyfit(x,sigma_300 ,deg=2))

fy_200 = np.poly1d(np.polyfit(x,y_200 ,deg=1))
fy_300 = np.poly1d(np.polyfit(x,y_300 ,deg=1))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# ax1.plot(x,sigma_200,'ko',x,fn_200(x),'k-',linewidth=2) 
# ax1.plot(x,sigma_300,'ko',x,fn_300(x),'k-',linewidth=2) 
# ax1.plot(x,y_200,'ko',x,fy_200(x),'k-',linewidth=2) 
ax1.plot(x,y_300,'ko',x,fy_300(x),'k-',linewidth=2) 
print("a_200 = ", fy_200(0))
print("b_200 =", (fy_200(16)-fy_200(0))/16)
print("a_300 = ", fy_300(0))
print("b_300 =", (fy_300(16)-fy_300(0))/16)
ax1.set_title('')
plt.xlabel('')
plt.ylabel('')

plt.show()
  

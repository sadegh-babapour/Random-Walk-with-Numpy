
import numpy as np
import matplotlib.pyplot as plt


aa = np.int_(np.random.choice([1,-1], size=(1,200)))
bb = np.int_(np.zeros((1,1)))
cc = np.concatenate((bb, aa), axis = 1)
jj = np.random.choice([1,-1], size=(1,200))
mm = np.concatenate((bb, jj), axis = 1)
tut = np.array([cc, mm])
stez =  np.cumsum(tut, axis=2)


x = stez[0,:]
y = stez[1,:]


aa = np.int_(np.random.choice([-3, 3, 2, -2], size=(1,10)))
np.where(cc %3 == 0)

bb = np.int_(np.zeros((1,1)))
cc = np.concatenate((bb, aa), axis = 1)
nn = np.int_(np.zeros(1))


aa = np.int_(np.random.choice([-3, 3, 2, -2], size=(1,15)))



aa = np.int_(np.random.choice([-3, 3, 2, -2], size=(1,100)))

xp = np.cumsum(aa == 2)
xp1 = np.cumsum(aa == -2)

xxx = xp - xp1


yp = np.cumsum(aa == 3)

yp1 = np.cumsum(aa == -3)

yyy = yp - yp1



zn = np.array([0])
vvv = np.concatenate((zn, xxx))
qqq = np.concatenate((zn, yyy))

print(vvv)
print(qqq)

gg=zip(vvv,qqq)
kk= list(gg)

start =plt.scatter(kk[0][0],kk[0][1], s = 200, label = "Start")
end = plt.scatter(kk[-1][0],kk[-1][1], color = "r", s=150, label = "End" )
lines =plt.plot(*zip(*kk), color = "pink")
plt.legend(loc = "best")
plt.show()

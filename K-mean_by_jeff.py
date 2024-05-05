import numpy as np
import pylab as py
import math

cor = 'rgbmy'

#分成k群,先生成k個點
#淺紫色為隨機生成的4個點
k = 4
kp = 10*np.random.rand(k,2)
py.scatter(kp[:, 0] , kp[:, 1] , s = 30 , c = 'violet')

#生成資料
X = 10*np.random.rand(100,2) 
#py.scatter(X[:, 0] , X[:, 1] , s = 30 , c = 'k')


tol = [[0 for j in range(2)] for i in range(len(kp))]

#跑5次
for t in range(5):
    counter = [0 for i in  range(k)]
    
    for i in range(len(X)):
        dis = []

        for j in range(len(kp)):

            dis.append(math.sqrt((kp[j][0]-X[i][0])**2 + (kp[j][1]-X[i][1])**2))
            m = min(dis)
            g = dis.index(min(dis))
            tol[g][0] += X[i][0]
            tol[g][1] += X[i][1]
            counter[g] += 1

    for i in range(len(kp)):
        tol[i][0] = tol[i][0]/counter[i]
        tol[i][1] = tol[i][1]/counter[i]

    kp = py.array(tol)

    print(tol , '+' , counter , end = '\n\n')
    
    #py.scatter(kp[:, 0] , kp[:, 1] , s = 30 , c = cor[t])

#最後一次,並輸出
tol = [[0 for j in range(2)] for i in range(len(kp))]

for i in range(len(X)):
    dis = []

    for j in range(len(kp)):

        dis.append(math.sqrt((kp[j][0]-X[i][0])**2 + (kp[j][1]-X[i][1])**2))
        m = min(dis)
        g = dis.index(min(dis))
        tol[g][0] += X[i][0]
        tol[g][1] += X[i][1]
        counter[g] += 1

    py.scatter(X[i][0] , X[i][1] , s = 30 , c = cor[g])

#黑點為分類後各群重心
py.scatter(kp[:, 0] , kp[:, 1] , s = 30 , c = 'k')    

py.show()

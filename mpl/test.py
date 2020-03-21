import matplotlib.pyplot as plt
#%matplotlib inline

Va = 60
Vb = 50
S = 5
t = None

#x = []
#y = []
#step = 0
#for i in range(0, 13):
#  x.append(step)
#  y.append(step)
#  step += 5


plt.title("lesson1", color="cyan")
plt.xlabel("time min/hour", color="lightgreen")
plt.ylabel("speed km/h", color="lightgreen")
plt.xticks(color="red")
plt.yticks(color="red")
plt.axis(xmin=0,xmax=60,ymin=0,ymax=60)




plt.plot([0,60],
         [0,60])
plt.plot([0,60],
         [5,55])


plt.show()
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7 ]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','k']

plt.pie(slices, labels=activities, colors=cols)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interesting Graph\ncheck it out")
plt.legend()
plt.show()
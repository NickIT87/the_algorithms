import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]


plt.bar(x, y, label='Bars1', color='blue')
plt.bar(x2, y2, label='Bars2', color='r')
#plt.plot(x, y, label='First Line')



plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interesting Graph\ncheck it out")
plt.legend()
plt.show()
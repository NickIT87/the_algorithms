import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 23, 34, 45, 110]

#ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)



plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interesting Graph\ncheck it out")
plt.legend()
plt.show()
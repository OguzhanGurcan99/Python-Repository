import matplotlib.pyplot as plt
import numpy as np

plt.title("First Plot")
plt.plot([1,2,3,4],[1,4,2,3])
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

plt.figure(figsize=(8,5))
plt.title("Second Plot")
plt.plot([1,2,3,4],[1,4,2,3])
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

plt.figure(figsize=(8,5))
plt.title("Third Plot")
plt.plot([1,2,3,4],[1,4,2,3],"ro")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

# MULTIPLE PLOTS IN ONE FIGURE WITH DIFFERENT TYPES OF DRAWING (LINE,POINT("ro","go","bo"))

x = np.arange(1,5)
y = x**3
plt.figure(figsize=(10,5))
plt.title("Fourth Plot")
plt.plot([1,2,3,4],[1,4,2,3],"ro", x, y )
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()


# SUBPLOT PARAMETRELER 2 X 2 = 4
#plt.subplot(satır,sutun,sıra)
#plt.subplot(2,2,1)
#plt.subplot(2,2,2)
#plt.subplot(2,2,3)
#plt.subplot(2,2,4)

plt.subplot(1,2,1)
plt.plot([1,2,3,4],[2,4,2,3],"ro")
plt.title("Red Points")

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Cubic Line")

plt.suptitle("My Subplots")
plt.show()


#ANOTHER METHOD FOR CREATING MANY SUBPLOTS (OOP APPROACH)

a = np.linspace(0,2,20)
fig, ax = plt.subplots()

ax.plot(a, a, label = "Linear" )
ax.plot(a, a**2, label = "Quadratic")
ax.plot(a, a**3, label = "Cubic" )
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_title("SIMPLE PLOT")
ax.legend()
plt.show()


# CREATING A BAR GRAPH
students = ["Ali","Ahmet","Mert"]
grades = [70,85,60]

plt.bar(students,grades, color="cyan")
plt.title("Bar Graph")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.show()

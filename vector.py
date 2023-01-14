import math 
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg




#Define the x and y ranges, and the tick interval for both axes.
xmin, xmax, ymin, ymax = -5, 5, -5, 5
ticks_frequency = 1
#Create a figure and an axes object. Also set the face color. This will cover transparent margins.
fig, ax = plt.subplots(figsize=(10, 10))
 
fig.patch.set_facecolor('#ffffff')
#Apply the ranges to the axes.
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
#Set both axes to the zero position.
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
#Set the x and y labels, and add an origin label.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
 
plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
    transform=ax.transAxes,
         horizontalalignment='center', fontsize=14)
#Now create the x and the y ticks, and apply them to both axes.

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

#Finally, add a grid.
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
	[sg.Text('Please enter your coordinates, Vector1, Vector2')],
	[sg.Text('V1_x', size =(10, 1)), sg.InputText()],
	[sg.Text('V1_y', size =(10, 1)), sg.InputText()],
    [sg.Text('V2_x', size =(10, 1)), sg.InputText()],
	[sg.Text('V2_y', size =(10, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]
window = sg.Window('Simple data entry window', layout)
event, values = window.read()
o1=0
#assign vector values here  for x
w=o1
x=o1
#y=1
#z=0
y= float(values[0])
z= float(values[1])
dx1=math.sqrt(((y - w)**2)+((z- x)**2))
#print (dx1)
#assign vector values here  for y
a=o1
b=o1
#c=0
#d=1
c= float(values[2])
d= float(values[3])


d2x=math.sqrt(((c - a)**2)+((d - b)**2))
#print (d2x)

resultant=math.sqrt(((dx1)**2)+((d2x)**2))
print ("Vector Lenght =")
print (resultant)

print ("Angle between the vectors =")
ang=(math.asin(dx1/resultant))
angcos=(math.acos(dx1/resultant))
angle=math.degrees((ang))
print (angle)
yterminal=((resultant)*(ang))
print("y-terminal")
print (yterminal)
print("x-terminal")
xterminal=((resultant)*(angcos))
print (xterminal)





#p.arrow( x, y, dx, dy, **kwargs )
#we can scale it here
plt.arrow( w, x, y, z,  fc="red", ec="red", head_width=0.2, head_length=0.1, width=.1)
plt.arrow( a, b, c, d,  fc="k", ec="k", head_width=0.2, head_length=0.1, width=.1 )
plt.arrow( a, b, xterminal, yterminal,  fc="yellow", ec="yellow", head_width=0.2, head_length=0.1, width=.1 )

#add the vectors to yield the resultant vector


#plt.quiver(b, y)

plt.show()




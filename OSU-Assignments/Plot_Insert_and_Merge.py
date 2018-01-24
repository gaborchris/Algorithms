import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from sklearn.metrics import r2_score
import sympy as sp
from sympy.abc import n

x_insert = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
y_insert = ([0.00113811,0.00456321,0.010395,0.0185187,0.0281884,0.0424371,0.0561396,0.0737306,0.093363,0.115838]) 
xy_insert = np.column_stack((x_insert,y_insert))

x_merge = 10*x_insert
y_merge = np.array([0.00239764,0.00506672,0.00781761,0.0106751,0.0135106,0.0164566,0.0194282,0.0223267,0.0250994,0.0278251])
xy_merge = np.column_stack((x_merge,y_merge))

x_stooge = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
y_stooge = ([0.00210293,0.00631721,0.0189129,0.0562819,0.168117,0.16901,0.169633,0.505029,0.50562,0.505379]) 
#x_stooge = np.array([100, 200, 300, 400, 700, 1000])
#y_stooge = ([0.00210293,0.00631721,0.0189129,0.0562819,0.168117,0.505379]) 
xy_stooge = np.column_stack((x_stooge,y_stooge))



fig = plt.figure()

#fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
ax = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax.set_title("Insert, Merge and Stooge Sort")
ax2.set_title("Insert Sort Runtime")
ax3.set_title("Merge Sort Runtime")
ax4.set_title("Stooge Sort Runtime")

ax.set_ylabel('Runtime (sec)')
ax.set_xlabel('Number of elements (N)')
ax2.set_ylabel('Runtime (sec)')
ax2.set_xlabel('Number of elements (N)')
ax3.set_ylabel('Runtime (sec)')
ax3.set_xlabel('Number of elements (N)')
ax4.set_ylabel('Runtime (sec)')
ax4.set_xlabel('Number of elements (N)')


#Insertion plot

#calculate fit function
z_insert = np.polyfit(x_insert, y_insert, 2)
f_insert = np.poly1d(z_insert)

# calculate new x's and y's
x_new_insert = np.linspace(x_insert[0], x_insert[-1], 50)
y_new_insert = f_insert(x_new_insert)

#plot new x, y

insert_predict = f_insert(x_insert)
#print(xy_insert[:,1])

xy_insert_predict = np.column_stack((x_insert,insert_predict))
#print(xy_insert_predict[:,1])

R2 = '{0:.6f}'.format(r2_score(xy_insert[:,1],xy_insert_predict[:,1]))
#print(R2)

A = '{0:.2g}'.format(f_insert.c[0])
B = '{0:.2g}'.format(f_insert.c[1])
C = '{0:.2g}'.format(f_insert.c[2])

ax.plot(x_insert, y_insert, 'bo')
ax.plot(x_new_insert, y_new_insert)
ax.text(15000, 0.22, 'Insert Sort', fontsize=8)
ax.text(10000, 0.18, A + r'$n^2+$' + B + r'$n+$' + C, fontsize=8)
ax.text(15000, 0.14, r'$r^2 = $' + R2 , fontsize=8)

ax2.plot(x_insert, y_insert, 'bo')
ax2.plot(x_new_insert, y_new_insert)
ax2.text(1000, 0.05, A + r'$n^2+$' + B + r'$n+$' + C, fontsize=8)
ax2.text(1500, 0.04, r'$r^2 = $' + R2 , fontsize=8)


#Merge plot

#calculate fit function
z_merge = np.polyfit(x_merge*np.log2(x_merge), y_merge, 1)
def f_merge(x):
    return z_merge[0]*x*np.log2(x)+z_merge[1]

# calculate new x's and y's
x_new_merge = np.linspace(x_merge[0], x_merge[-1], 50)
y_new_merge = f_merge(x_new_merge)

#plot new x, y

merge_predict = f_merge(x_merge)

xy_merge_predict = np.column_stack((x_merge,merge_predict))

R2 = '{0:.6f}'.format(r2_score(xy_merge[:,1],xy_merge_predict[:,1]))

A = '{0:.2g}'.format(z_merge[0])
B = '{0:.2g}'.format(z_merge[1])

ax.plot(x_merge, y_merge, 'bo')
ax.plot(x_new_merge, y_new_merge)
ax.text(45000, 0.12, "Merge Sort", fontsize=8)
ax.text(40000, 0.08, A + r'$nlog_2(n) + $' + B, fontsize=8)
ax.text(45000, 0.04, r'$r^2 = $' + R2 , fontsize=8)

ax3.plot(x_merge, y_merge, 'bo')
ax3.plot(x_new_merge, y_new_merge)
ax3.text(20000, 0.02, A + r'$nlog_2(n) + $' + B, fontsize=8)
ax3.text(25000, 0.017, r'$r^2 = $' + R2 , fontsize=8)




#Stooge plot

#calculate fit function
#z_stooge = np.polyfit(x_stooge, np.log2(y_stooge)/np.log2(2.71), 1)
#print(x_stooge, np.log2(y_stooge)/np.log(2.71))
#z_stooge = np.polyfit(x_stooge, y_stooge, 3)
#def f_stooge(): #= np.poly1d(z_stooge)
#    return z_stooge[0]*x*np.log2(x)+z_merge[1]

z_stooge = np.polyfit(x_stooge**2.71, y_stooge, 1)
def f_stooge(x):
    return z_stooge[0]*x**2.71+z_stooge[1]


# calculate new x's and y's
x_new_stooge = np.linspace(x_stooge[0], x_stooge[-1], 50)
y_new_stooge = f_stooge(x_new_stooge)

#plot new x, y

stooge_predict = f_stooge(x_stooge)

xy_stooge_predict = np.column_stack((x_stooge,stooge_predict))

R2 = '{0:.6f}'.format(r2_score(xy_stooge[:,1],xy_stooge_predict[:,1]))

A = '{0:.2g}'.format(z_stooge[0])
B = '{0:.2g}'.format(z_stooge[1])
#C = '{0:.2g}'.format(f_stooge.c[2])
#print(f_stooge)


ax.plot(x_stooge, y_stooge, 'bo')
ax.plot(x_new_stooge, y_new_stooge)
ax.text(1500, 0.42, 'Stooge Sort', fontsize=8)
ax.text(1000, 0.38, A + r'$n^{2.71}+$' + B , fontsize=8)
ax.text(1500, 0.34, r'$r^2 = $' + R2 , fontsize=8)

ax4.plot(x_stooge, y_stooge, 'bo')
ax4.plot(x_new_stooge, y_new_stooge)
ax4.text(250, 0.35, A + r'$n^{2.71}+$' + B , fontsize=8)
ax4.text(300, 0.25, r'$r^2 = $' + R2 , fontsize=8)




fig.tight_layout()

plt.show()



0.00210293,0.00631721,0.0189129,0.0562819,0.168117,0.16901,0.169633,0.505029,0.50562,0.505379



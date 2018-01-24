import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from sklearn.metrics import r2_score
import sympy as sp
from sympy.abc import n

x_insert = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000])
y_insert = ([0.115501,0.464703,1.03655,1.83954,2.87252,4.1247, 5.62462]) 
xy_insert = np.column_stack((x_insert,y_insert))

x_merge = 10*x_insert
y_merge = np.array([0.0283902,0.0584768,0.0910227,0.121111,0.154171,0.18725,0.219068])
xy_merge = np.column_stack((x_merge,y_merge))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Average Runtime vs N elements")

ax.set_ylabel('Runtime (sec)')
ax.set_xlabel('Number of elements (N)')

#Insertion plot

#calculate fit function
z_insert = np.polyfit(x_insert, y_insert, 2)
f_insert = np.poly1d(z_insert)

# calculate new x's and y's
x_new_insert = np.linspace(x_insert[0], x_insert[-1], 50)
y_new_insert = f_insert(x_new_insert)

#plot new x, y

insert_predict = f_insert(x_insert)

xy_insert_predict = np.column_stack((x_insert,insert_predict))

R2 = '{0:.6f}'.format(r2_score(xy_insert,xy_insert_predict))

A = '{0:.2g}'.format(f_insert.c[0])
B = '{0:.2g}'.format(f_insert.c[1])
C = '{0:.2g}'.format(f_insert.c[2])

ax.plot(x_insert, y_insert, 'bo')
ax.plot(x_new_insert, y_new_insert)
ax.text(50000, 2.5, A + r'$n^2+$' + B + r'$n+$' + C, fontsize=8)
ax.text(100000, 2.3, r'$r^2 = $' + R2 , fontsize=8)


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

R2 = '{0:.6f}'.format(r2_score(xy_merge,xy_merge_predict))

A = '{0:.2g}'.format(z_merge[0])
B = '{0:.2g}'.format(z_merge[1])

ax.plot(x_merge, y_merge, 'bo')
ax.plot(x_new_merge, y_new_merge)
ax.text(400000, 1, A + r'$nlog_2(n) + $' + B, fontsize=8)
ax.text(450000, 0.8, r'$r^2 = $' + R2 , fontsize=8)

plt.show()



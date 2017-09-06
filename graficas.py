import numpy as np
import pylab as pl
x=[6000,7000,8000,9000,10000]
y=[73,80,85,87,89]
pl.plot (x,y)
x1=[7000,8000,9000,10000,11000]
y2=[65,75,85,86,90]
pl.plot (x1,y2)
pl.xlabel ('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
pl.savefig ('voltaje y eficiencia')
pl.show()

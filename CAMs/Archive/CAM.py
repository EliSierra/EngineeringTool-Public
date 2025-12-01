def CAM_Math(BR, TR, T, D1, D2, D3, D4, Tri):
    import numpy as np
    import pylab as pl
    import math
    import matplotlib.pyplot as plt
    angle1=np.array([])

    angle1 = np.linspace(0,D1,Tri)
    Y1=(TR/2)*(1-np.cos((np.pi*angle1)/D1))

    plt.figure(figsize=(6.6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angle1/180*np.pi,Y1+BR)
    plt.show()


    CAM_Math
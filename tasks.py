#!/usr/bin/env python
# coding: utf-8

# # problem 1

# In[1]:


import numpy as np
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt


# In[2]:


data = np.genfromtxt ("data.csv", delimiter=";")


# In[3]:


measured, simulated = data[1:,0], data[1:,1]


# In[19]:


plt.plot( measured, 'r-', label='measured acceleration')
plt.plot(simulated, 'bo', label='simulated acceleration')
plt.show()


# In[5]:


plt.plot(simulated-measured)


# # Problem 2

# In[6]:


f = 500  # Sample Rate Hz
T = 1 / f  # Sample Spacing time gap
# N = len(measured)  # Number of Sample Points
# t = np.linspace(0.0, N*T, N, endpoint=False) #time


# In[7]:


amf = fft(measured)
asf = fft(simulated)
# tf = fftfreq(N, T)
# https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html


# In[8]:


# plt.plot(tf,np.abs(af))
plt.plot(asf)
plt.plot(amf)
plt.grid()
plt.show()


# # Problem 3

# In[11]:


residual = simulated - measured


# In[12]:


residual_fft = fft(residual)


# In[13]:


plt.plot(residual_fft)


# In[ ]:





# In[ ]:





# In[ ]:





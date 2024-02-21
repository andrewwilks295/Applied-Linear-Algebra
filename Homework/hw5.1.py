# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:21:22 2023

@author: wilks
"""
import numpy as np
from sympy import *
A = np.array([[-6,-21,-16],[6,17,12],[-5,-12,-8]])
b = np.array([-2,0,1])
print(np.dot(A, b))

b = np.array([2,-1,-1])
print(np.dot(A, b))

b = np.array([1,-1,1])
print(np.dot(A, b))

A = np.array([[2,-5,-2],[2,-7,-3],[-4,14,6]])
b = np.array([-1,-1,2])
print(np.dot(A, b))

b = np.array([-1,-2,4])
print(np.dot(A, b))

b = np.array([0,0,0])
print(np.dot(A, b))

x = np.array([[-12,2,32],[-8,-4,0],[-2,1,8]])




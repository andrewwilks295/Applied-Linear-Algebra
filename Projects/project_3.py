# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:12:54 2023

@author: wilks
"""
import numpy as np
u = np.array([6, -1])
v = np.array([1, 4])
f1 = lambda u, v : np.emath.arccos((sum(u * v))/(np.linalg.norm(u) * np.linalg.norm(v)))
print("\n\nProject 3: Angles\n\n-----------------------------------------------------")
print("Task 1\nAngle between in randians:", f1(u, v))
print("-----------------------------------------------------\n")




r = 6367.5
coords = np.array([[39.914, 37.429], [116.392, -122.138]])
coords = np.array([[37.6775, 35.2100], [-113.0619, 129.0689]])

convert_coord = lambda coords, radius : radius*np.array([np.cos(coords[0]*np.pi/180)*np.sin(coords[1]*np.pi/180), np.cos(coords[0]*np.pi/180)*np.cos(coords[1]*np.pi/180), np.sin(coords[0]*np.pi/180)])
result = convert_coord(coords, r)
u = result[ : , 0]
v = result[ : , 1]
f2 = lambda u, v, r : r * np.emath.arccos((sum(u * v))/(np.linalg.norm(u) * np.linalg.norm(v)))
print("-----------------------------------------------------")
print("Task 2\nSpherical distance:", f2(u, v, r))
print("-----------------------------------------------------\n\n")

# -*- coding: utf-8 -*-
"""Capacitated Plant Location

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13nA9udnAVZ-BO-bTnuKbm14dlznZZ5hh
"""

from pulp import *

# Initialize Class
model = LpProblem("Capacitated Plant Location Model"
# Define Decision Variables
loc = ['A', 'B', 'C', 'D', 'E']
size = ['Low_Cap', 'High_Cap']
x = LpVariable.dicts("production_", [(i,j) for i in loc for j in loc],
                                     lowBound=0, upBound=None, cat='Continuous')
y = LpVariable.dicts("plant_", [(i,s) for s in size for i in loc], cat='Binary')

# Define Objective Function
model += (lpSum([fix_cost.loc[i,s]*y[(i,s)] for s in size for i in loc])
        + lpSum([var_cost.loc[i,j]*x[(i,j)] for i in loc for j in loc]))                  
                    
# Define the Constraints
for j in loc:
model += lpSum([x[(i, j)] for i in loc]) == demand.loc[j,'Dmd']
for i in loc:
model += lpSum([x[(i, j)] for j in loc]) <= lpSum([cap.loc[i,s]*y[(i,s)]for s in size])
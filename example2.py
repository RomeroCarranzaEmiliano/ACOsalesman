# libraries
import random

# this matrix represents the distance between 5 cities
d = [
	[0, 10, 12, 11, 14],
	[10, 0, 13, 15, 8],
	[12, 13, 0, 9, 14],
	[11, 15, 9, 0, 16],
	[14, 8, 14, 16, 0] 
]


# calculate visibility between cities by performing 1/d  in the distances matrix
h = []
for i in range(len(d)):
	h.append([])
	for j in range(len(d[i])):
		if (d[i][j] != 0):
			h[i].append(float(1./d[i][j]))
		else:
			h[i].append(0)

# provide initial values of pheromones
ph = []
for i in range(len(d)):
	ph.append([])
	for j in range(len(d[i])):
		ph[i].append(1)



## HERE THE LOOP FOR EVERY ANT GROUP STARTS
## ========================================
##
## 	In this loop a set of ants goes from
## city to city, changing across the index
## of the matrixes. 
##
## An ant reaches its final path once 
## There are no more visible cities to 
## visit. For this reason it might be 
## needed to asociate a visibility matrix
## diferent for every ant
##
	
# calculate probability of going form city 1 to any other
alpha = 1
beta = 2

prob = 0
p = [] # array of probabilities
E = 0 # sumatory of all probabilities
for i in range(5):
	prob = (ph[0][i]**(alpha)) *(h[0][i]**(beta))
	p.append(prob)
	E += prob

for i in range(len(p)):
	p[i] = p[i]/E

# get cumulative probabilities
i;
for i in range(len(p)-1, 0, -1): #from end to start of array!!
	for j in range(i):
		p[i] += p[j]

# generation of random number
r = random.uniform(0, 1)

# get selected city
city = 0
while (p[city] < r):
	city += 1

# update visibility of city visited
# given that every city can be visited only once
h[0][city] = 0;
h[1][city] = 0;
h[2][city] = 0;
h[3][city] = 0;

#######################################################
##   A list of arrays containing the cities visited  ##
## by every ant should be resulted here              ##
#######################################################



### ONCE THE PROCESS IS REPEATED FOR EVERY CITY AND EVERY ANT###
################################################################

# Update pheromones

e = 0.5 #evaporation coefficient

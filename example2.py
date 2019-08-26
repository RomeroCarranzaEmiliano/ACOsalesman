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
	
# fix parameters
alpha = 1
beta = 2
e = 0.5 #evaporation coefficient

ants = []

for a in range(2): #range 1 because it's only one ant
	
	# creation of an ant
	ants.append([0]) # 0 because all ants start at city cero

	city = 0 # starting city

	# calculate visibility between cities by performing 1/d  in the distances matrix
	h = []
	for i in range(len(d)):
		h.append([])
		for j in range(len(d[i])):
			if (d[i][j] != 0):
				h[i].append(float(1./d[i][j]))
			else:
				h[i].append(0)
	
	while (1):

		# calculate probability of going form city 1 to any other
		prob = 0
		p = [] # array of probabilities
		E = 0 # sumatory of all probabilities
		for i in range(5):
			prob = (ph[city][i]**(alpha)) *(h[city][i]**(beta))
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

		# store city in ant's path
		ants[a].append(city)

		# update visibility of city visited
		# given that every city can be visited only once
		for i in range(len(h)):
			h[i][city] = 0

		#break while loop when all h == 0
		path_complete = True
		for i in range(len(h)):
			for j in range(len(h[i])):
				if (h[i][j] != 0):
					path_complete = False
		if (path_complete == True):
			break
		

### ONCE THE PROCESS IS REPEATED FOR EVERY CITY AND EVERY ANT###
################################################################

# Update pheromones
# evaporate every path's pheromone
# get total distance of each ant
# update in every path with 1/total distance

# evaporate pheromones
for i in range(len(ph)):
	for j in range(len(ph[i])):
		ph[i][j] -= ph[i][j]*e

for a in range(len(ants)): # for every ant
	cost = 0 # equals total distance traveled by ant
	for i in range(1, len(ants[a])):
		cost += d[ants[a][i-1]][ants[a][i]]
	for i in range(len(ph)):
		for j in range(len(ph[i])):
			ph[i][j] += 1.0/cost





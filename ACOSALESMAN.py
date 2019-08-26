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

	
# fix parameters
alpha = 1
beta = 2
e = 0.5 # evaporation coefficient
Z = 20 # num of iterations
A = 10 # num of ants in the colony

for z in range(Z): #repeat the process z times
	# restore the ant colony
	ants = []

	for a in range(A): #the range is the number of ants
	
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

		# city one is starting point, so provide 0 visibility
		for i in range(len(h)):
				h[i][0] = 0
	
		while (1):

			# calculate probability of going form city to any other
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
				# store last city in ant's path
				# witch is city cero
				ants[a].append(0)
				break
		

	### ONCE THE PROCESS IS REPEATED FOR EVERY EVERY ANT###
	#######################################################

	cost_list = []
	best = [0, 0]

	# Update pheromones
	# evaporate pheromones
	for i in range(len(ph)):
		for j in range(len(ph[i])):
			ph[i][j] -= ph[i][j]*e
	# add more pheromones
	for a in range(len(ants)): # for every ant
		cost = 0 # equals total distance traveled by ant
		for i in range(1, len(ants[a])):
			cost += d[ants[a][i-1]][ants[a][i]]
		cost_list.append(cost)
		for i in range(len(ph)):
			for j in range(len(ph[i])):
				ph[i][j] += 1.0/cost

	# get min cost
	best[0] = ants[cost_list.index(min(cost_list))]
	best[1] = min(cost_list)

print best[0]
print best[1]




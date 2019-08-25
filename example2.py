# libraries
import random

# this matrix represents the distance between 5 cities
d = [
	0, 10, 12, 11, 14,
	10, 0, 13, 15, 8,
	12, 13, 0, 9, 14,
	11, 15, 9, 0, 16,
	14, 8, 14, 16, 0 
]

# calculate visibility between cities by performing 1/d  in the distances matrix
h = []
for i in range(len(d)):
	if (d[i] != 0):
		h.append(float(1./d[i]))
	else:
		h.append(0)

# provide initial values of pheromones
ph = []
for i in range(len(d)):
	ph.append(1)

## loop?
	
# calculate probability of going form city 1 to any other
alpha = 1
beta = 2

prob = 0
p = [] # array of probabilities
E = 0 # sumatory of all probabilities
for i in range(5):
	prob = (ph[i]**(alpha)) *(h[i]**(beta))
	p.append(prob)
	E += prob

for i in range(len(p)):
	p[i] = p[i]/E

#get cumulative probabilities
i;
for i in range(len(p)-1, 0, -1): #from end to start of array!!
	for j in range(i):
		p[i] += p[j]

#generation of random number
r = random.uniform(0, 1)

#get selected city
city = 0
while (p[city] < r):
	city += 1

print city


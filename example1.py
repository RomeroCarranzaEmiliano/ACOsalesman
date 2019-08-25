# C = set of cities
# L = set of posible connections among CC where CC = C X C
# J = connection cost function, in this case, not nedeed?
# Omega = set of constraints over elements of C and L
# s = secuence of elements of C

##LIBRARIES
##============================

##============================

C = [1, 2, 3, 4];
L = [ #paths
	[2, 3, 4],
	[1, 3, 4],
	[1, 2, 4],
	[1, 2, 3]
];
n = [ #cost in every path
	[20, 35, 42],
	[20, 34, 30],
	[35, 34, 12],
	[42, 30, 12]
];

f = [ #feromone in every path
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]
];



alpha = 1;
beta = 5;
omega = [];
fi = 0.1;


#return a set with the probability of selecting a city according to the city provided and the 
#omega set of constraint cities
def prob(C, ci, f, n, alpha, beta, omega):
	p = [];
	den = 0;
	for j in range(3):
		for k in range(2):
			den += (f[j][k]**alpha)*(n[j][k]**beta);

	for i in range(3):
		for l in range(2):
			num = (f[C[i]][l]**alpha)*(n[C[i]][l]**beta);
			p.append(num/den);

	return p;

#returns the feromones to place
#It depositates more feromones when the cost is lower
def fero(costs, C):
	f = [];
	for i in range(3):
		f[i] = 100-costs;
	return f;


A = [
	[],
	[]
]

killer = 0;
while (1):

	for i in range(3):
		for j in range(2):
			if (f[i][j] != 0):
				f[i][j] -= f[i][j]*fi;

		A[0].append(max(prob(C, killer, f, n, alpha, beta, omega)));
		A[1].append(max(prob(C, killer, f, n, alpha, beta, omega)));








	killer +=1;
	if(killer == 100):
		break;
	else:
		A[0] = [];
		A[1] = [];

print(A[0]);

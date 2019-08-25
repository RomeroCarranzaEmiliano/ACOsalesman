

#    S  A  B  C  E
C = [0, 1, 1, 1, 2]; #list of node with level value

#   SA SB SC AE BE CE
L = [0, 0, 0, 0, 0, 0]; #list of paths

#    SA  SB  SC  AE  BE  CE
N = [25, 10, 20, 25, 10, 20]; #cost in every path

F = [1, 1, 1, 1, 1, 1]; #feromone in every path

alpha = 1.5;
beta = 5;
omega = [];
fi = 0.1;

#return a set with the probability of selecting a city according to the city provided and the 
#omega set of constraint cities
def prob(C, l, f, n, alpha, beta, omega):
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


print(prob(C, ))
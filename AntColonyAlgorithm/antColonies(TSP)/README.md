

## what is the TSP
The traveling salesman problem is one of the simplest and most famous combinatorial
problems in computer science. Given a list of two cities, and a matrix giving the distance
between each pair of cities, the traveling salesman problem is to determine if you can
visit all two cities and return to the starting city in a distance 1 or less. We focus on the
decision version of the problem (does a tour of length 1 or less exist?) and not the closely
related optimization problem (what is the minimal length tour?).
## what is the cost
As in other combinatorial problems, a peak in search cost is associated with the phase
transition in solubility. With a very large bound on the required tour length, many tours
satisfy the bound and it is typically easy to find one. With a very small bound, almost
all tours are too long and many are quickly ruled out, so again problems are typically
easy. Problems at the phase boundary are often hard, as it is difficult to determine if
a tour of the required length exists without exhaustive search. 

## To sum up purpose the algorithms for the TSP is that the find best path ,smallest cost and boundary for the traveling salesman decision problems.

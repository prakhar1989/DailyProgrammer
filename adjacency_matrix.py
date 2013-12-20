"""
URL: http://www.reddit.com/r/dailyprogrammer/comments/1t6dlf/121813_challenge_140_intermediate_adjacency_matrix/
Your goal is to write a program that takes in a list of edge-node relationships, and print a directed adjacency matrix for it. Our convention will follow that rows point to columns. Follow the examples for clarification of this convention.
"""
def prettyprint(matrix):
	for row in matrix:
		for cell in row:
			print cell,
		print

def add_cell(txt, matrix):
	(start_vertices, end_vertices) = map(str.split, txt.split(' -> '))
	for u in start_vertices:
		for v in end_vertices:
			matrix[int(u)][int(v)] = 1
	
if __name__ == "__main__":
	input_lines = open("txtfiles/graph_input.txt").readlines();
	(N, M) = map(int, input_lines[0].strip().split())
	matrix = [[0 for i in range(N)] for k in range(N)]
	for l in input_lines[1:]:
		add_cell(l.strip(), matrix)

	prettyprint(matrix)
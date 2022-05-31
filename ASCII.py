def map(x,a,b):
  return int((x*b))/a)
def genaratematrix(x):
  Matrix = [[0 for i in range(x)] for j in range(x)]
  return Matrix
def display(matrix):
  for x in matrix:
    print(*x)

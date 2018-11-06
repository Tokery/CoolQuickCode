# Check if a semigroup is finite

import numpy as np

def checkSemiGroup(L):
  q = []
  for matrix in L:
    q.append(matrix)
  visited = L.copy()
  while(len(q) > 0):
    if (len(visited) > 10000):
      print ("Likely infinite")
      return -1
    A = q[0]
    q = q[1:]
    for matrix in L:
      B = np.matmul(A, matrix).tolist()
      if (not B in visited):
        visited.append(B)
        q.append(B)
  
  print ("The semigroup is finite")
  print ("Semigroup size is " + str(len(visited)))
  return len(visited)

A = [
  [1, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1],
  [-1, 0, -1, 0, 0],
  [1, 0, 1, 0, 0]
]

B = [
  [1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, -1, 1],
  [-1, 0, -1, 0, 0],
  [1, 0, 1, 0, 0]
]

# A = [
#     [1 , 0 , 0, 0],
#     [0,  0,  0, 0],
#     [0, -1,  0, 0],
#     [0, -1, -1, 0]
# ]

# B = [
#     [0,  1, -1, 0],
#     [0, -1,  0, 0],
#     [1,  0,  1, 0],
#     [0,  0,  0, 1]
# ]
checkSemiGroup([A, B])

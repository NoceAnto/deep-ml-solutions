import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	def isinvertible(M):
		if np.linalg.det(M)!=0:
			return True
		else: 
			return False
	
	if isinvertible(np.array(T)) and isinvertible(np.array(S)):
		Tinverse = np.linalg.inv(np.array(T))
		#print(Tinverse)
		m = np.matmul(Tinverse,np.array(A)); 
		#print(m)
		m = np.matmul(m,np.array(S))
		#print(m)

		return np.squeeze(m)

	else: 
		return -1

	
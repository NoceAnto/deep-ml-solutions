import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if np.shape(a)[0]*np.shape(a)[1] == new_shape[0]*new_shape[1]:
	
		reshaped_matrix = np.reshape(a, new_shape).tolist()
		return reshaped_matrix
	else: 
		return []
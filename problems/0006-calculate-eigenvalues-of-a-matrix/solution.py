import numpy as np 
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# Ay = ky

	matrix_np = np.array(matrix); 

	det_A = matrix_np[0,0]*matrix_np[1,1]-matrix_np[0,1]*matrix_np[1,0]; 

	b = matrix_np[0,0]+matrix_np[1,1]; 

	e1 = (b+np.sqrt(b**2-4*det_A))/2; 
	e2 = (b-np.sqrt(b**2-4*det_A))/2; 

	eigenvalues = [e1,e2]; 



	return eigenvalues
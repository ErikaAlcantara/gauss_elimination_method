import numpy as np

class Gauss_partial_pivoting:

    def __init__(self, a00, a10, a20, a01, a11, a21, a02, a12, a22, b0, b1, b2):
        self.a00 = a00
        self.a10 = a10
        self.a20 = a20
        self.a01 = a01
        self.a11 = a11
        self.a21 = a21
        self.a02 = a02
        self.a12 = a12
        self.a22 = a22
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2

        self.matrix = np.array([[a00,a01,a02],[a10,a11,a12],[a20,a21,a22]], float)
        self.matrix = np.round(self.matrix, 4)
        self.matrix_solution = np.array([b0, b1, b2], float)
        self.matrix_solution = np.round(self.matrix_solution, 4)
        self.matrix_len = len(self.matrix_solution)
        self.x = np.zeros(self.matrix_len, float)
    
    def elimination(self):
        steps = {
            "pivot_list": [],
            "equation_list": [],
            "matrix_list": [],
            "matrix_solution_list": [],
            "results_list":[]
        }
        # pivot_list = []
        # equation_list = []
        # matrix_list = []
        # matrix_solution_list = []
        # results_list = []

        # print(self.matrix)
        # print(self.matrix_solution)
        # matrix_list.append(self.matrix)
        # matrix_solution_list(self.matrix_solution)


        for k in range(self.matrix_len-1):
            if np.fabs(self.matrix[k,k]) < 1.0e-12:
                for i in range(k+1, self.matrix_len):
                    if np.fabs(self.matrix[i,k]) > np.fabs(self.matrix[k,k]):
                        self.matrix[[k,i]] = self.matrix[[i,k]]
                        self.matrix_solution[[k,i]] = self.matrix_solution[[i,k]]
                        break
            for i in range(k+1,self.matrix_len):
                if self.matrix[i,k] == 0:
                    continue
                factor = self.matrix[k,k]/self.matrix[i,k]
                for j in range(k, self.matrix_len):
                    self.matrix[i,j] = self.matrix[k,j] - self.matrix[i,j] * factor
                self.matrix_solution[i] = self.matrix_solution[k] - self.matrix_solution[i] * factor
                steps["equation_list"].append("L" + str(j) +  " = " + "L" + str(j) + " -" + " L" + str(i) + " * " + str(factor))
                # equation_list.append("L" + str(j) +  " = " + "L" + str(j) + " -" + " L" + str(i) + " * " + str(factor))
            
            # print(self.matrix[k,i])
            # print("L" + str(j) +  " = " + "L" + str(j) + " -" + " L" + str(i) + " * " + str(factor))
            steps["pivot_list"].append(self.matrix[k,i])
            # pivot_list.append(self.matrix[k,i])
            
            steps["matrix_list"].append(self.matrix)
            # matrix_list.append(self.matrix)
            steps["matrix_solution_list"].append(self.matrix_solution)
            # matrix_solution_list.append(self.matrix_solution)
            steps["results_list"].append(np.linalg.solve(self.matrix, self.matrix_solution))
            # results_list.append(np.linalg.solve(self.matrix, self.matrix_solution))
            # print(self.matrix)
            # print(self.matrix_solution)
            # print(np.linalg.solve(self.matrix, self.matrix_solution))
        return steps









        




    

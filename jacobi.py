import numpy as np
from prettytable import PrettyTable

table = PrettyTable()

class JacobiMethod:
    def __init__(self, coeff_matrix, const_vector, initial=None, accuracy=4):
        self.coeff_matrix = coeff_matrix
        self.const_vector = const_vector
        self.solution = initial or [0 for _ in self.const_vector]
        print(self.solution)
        self.accuracy = accuracy
        self.upper_limiting_error = (1/2) * (10 ** -self.accuracy)

    def is_diag_dominant(self): 
        n = len(self.solution)

        for i in range(n):
            _sum = 0
            for j in range(n):
                if not i==j:
                     _sum = _sum + abs(self.coeff_matrix[i][j])
    
            if (abs(self.coeff_matrix[i][i]) < _sum):
                return False
    
        return True
    
    def calculate(self):
        if not self.is_diag_dominant():
            print("Sorry! the system of equation is not diagonally dominant.")
            return

        n = len(self.solution)
        x_new = [0 for _ in self.solution]

        table.title = "Iteration Table"
        table.field_names = ['n', *[f'x{i}' for i in range(1, n+1)]]

        iteration = 1
        while True:
            table.add_row([iteration, *[f'{value:.{self.accuracy + 1}f}' for value in self.solution]])

            for i in range(n):
                _sum = 0
                for j in range(n):
                    if not i == j:
                        _sum -= self.coeff_matrix[i][j] * self.solution[j]
                _sum += self.const_vector[i]
                x_new[i] = _sum / self.coeff_matrix[i][i]

            if max(abs(np.array(self.solution) - np.array(x_new))) < self.upper_limiting_error:
                table.add_row([iteration+1, *[f'{value:.{self.accuracy + 1}f}' for value in x_new]])
                break

            self.solution = [round(x, self.accuracy+1) for x in x_new]
            iteration += 1

        print(table)
        print('\nRequired Root : ', [f'{round(value, self.accuracy):.{self.accuracy}f}' for value in x_new])

import sys

from jacobi import JacobiMethod

def setup():
    try:
        number_of_variables = int(input('\nEnter the number of variables (at least 2): '))

        if number_of_variables < 2:
            print('There must be at least two variables. 😛')
            raise ValueError('The equation must contain at least 2 variables. 😛')

        print('\nYour system looks like this:')
        for i in range(number_of_variables):
            for j in range(number_of_variables):
                print(f"a_{i+1}_{j+1} * x{j+1}", end="")
                if not j == number_of_variables - 1:
                    print(" + ", end="")
            print(f" = b_{i+1}")

        return number_of_variables
    
    except Exception:
        return setup()  
           

def get_user_input(number_of_variables):
    M = [[0 for _ in range(number_of_variables)] for _ in range(number_of_variables)]
    N = [0 for _ in range(number_of_variables)]

    print('\nEnter the constants of the equations:')
    for i in range(number_of_variables):
        print()
        for j in range(number_of_variables):
            M[i][j] = float(input(f"a_{i+1}_{j+1} : ") or 0)
        N[i] = float(input(f"b_{i+1} : ") or 0)

    print('\nSystem of linear equations:')
    for i in range(number_of_variables):
        for j in range(number_of_variables):
            print(f"({str(M[i][j])}) * x{j+1}", end="")
            if not j == number_of_variables - 1:
                print(" + ", end="")
        print(f" = ({N[i]})")    
    print()

    return M, N

def main():
    jm = JacobiMethod(*get_user_input(setup()))
    jm.calculate()
try:
    main()
except KeyboardInterrupt:
    print('\n--- Sorry to see you go 🚀 ---\n')
    sys.exit(0)
except ZeroDivisionError:
    print('Sorry! Division by zero witnessed 😢')
    sys.exit(0)
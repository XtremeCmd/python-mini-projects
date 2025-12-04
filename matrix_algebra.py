import numpy as np
from numpy import linalg

# matrix input function
def input_matrix(name):
    print(f"\nEnter elements of {name} (3x3 matrix):")
    matrix = []
    for i in range(3):
        row = list(map(float, input(f"Row {i+1} (space-separated 3 numbers): ").split()))
        if len(row) != 3:
            raise ValueError("Each row must contain exactly 3 numbers.")
        matrix.append(row)
    return np.array(matrix)


try:
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    # Addition
    add = A + B

    # Subtraction
    sub = A - B

    # Multiplication
    mul = A @ B    

    # Determinants
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)

    
    print("\n<-- RESULTS -->")
    print("\nA + B =\n", add)
    print("\nA - B =\n", sub)
    print("\nA × B =\n", mul)
    print(f"\nDeterminant of A = {det_A:.2f}")
    print(f"Determinant of B = {det_B:.2f}")

except Exception as e:
    print("Error:", e)

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        values = [int(value) for value in row_values]
        matrix.append(values)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:>5}" for value in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return None

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def main():
    print("Matrix Operations")
    print("1. Transpose")
    print("2. Add matrices")
    print("3. Multiply matrices")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = read_matrix(rows, cols)
        print("\nOriginal Matrix:")
        display_matrix(matrix)
        print("\nTransposed Matrix:")
        display_matrix(transpose_matrix(matrix))
    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print("Enter matrix A:")
        matrix_a = read_matrix(rows, cols)
        print("Enter matrix B:")
        matrix_b = read_matrix(rows, cols)
        result = add_matrices(matrix_a, matrix_b)
        if result is None:
            print("Error: Matrices must be the same size.")
        else:
            print("\nResult:")
            display_matrix(result)
    elif choice == "3":
        rows_a = int(input("Enter rows for matrix A: "))
        cols_a = int(input("Enter columns for matrix A: "))
        rows_b = int(input("Enter rows for matrix B: "))
        cols_b = int(input("Enter columns for matrix B: "))
        print("Enter matrix A:")
        matrix_a = read_matrix(rows_a, cols_a)
        print("Enter matrix B:")
        matrix_b = read_matrix(rows_b, cols_b)
        result = multiply_matrices(matrix_a, matrix_b)
        if result is None:
            print("Error: Matrix dimensions are incompatible for multiplication.")
        else:
            print("\nResult:")
            display_matrix(result)
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=' ' if column != row[-1] else '')
        print()

"""
Function Definition: The function is defined with the name print_matrix_integer and an optional parameter matrix with a default value of an empty list (an empty matrix).

Outer Loop (Rows): The function starts by iterating through each row in the matrix. This outer loop iterates over each list (row) within the matrix.

Inner Loop (Columns): Inside the outer loop, there's another loop that iterates through each element in the current row. The range(len(row)) generates a sequence of indices for the elements in the current row.

Printing Elements: The code inside the inner loop is responsible for printing the elements in the matrix.

    The if condition if column != row[-1]: checks if the current element is not the last element in the row. This is used to determine whether a space should be printed after the element. If it's not the last element, a space will be printed after the element.

    The print("{:d}".format(row[i]), end=" ") statement uses the format method to convert and print the current element as an integer. The {:d} inside the curly braces is a placeholder for an integer. The end=" " argument specifies that a space should be used instead of a newline character at the end of the printed string. This keeps elements in the same row on the same line.

    If the current element is the last element in the row (else part of the condition), the end argument is set to an empty string (end="") to prevent adding an extra space at the end of the row.

New Line: After printing all elements in the current row, a print() statement is used to move to the next line. This ensures that the next row of the matrix will be printed on a new line.
"""
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
print_matrix_integer(matrix)

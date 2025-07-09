import numpy as np

def matrix_multiplication(): 
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]

    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

    # TRY THIS B VALUE TO CHECK ERROR HANDLING
    # B = [[5, 8, 1, 2],
    #      [6, 7, 3, 0]]
        
    k=len(A[0])
    j=len(B)

    if ( k!=j):
        print("cannot be multipled")

    else:
        result = np.dot(A, B)

        for row in result:
            print(row)



def main():
    matrix_multiplication()

if __name__ == "__main__":
    main()
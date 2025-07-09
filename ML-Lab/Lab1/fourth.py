import numpy as np # pip install numpy

def matrix_transpose():
    A=[[1,2,3],
    [4,5,6],
    [7,8,9]]

    res=np.transpose(A) # inbuilt function

    print(res)


def main():
    matrix_transpose()

if __name__ == "__main__":
    main()
from sage.all import *
import random

def gen_matrix(rows, cols):
    return random_matrix(ZZ, rows, cols, algorithm='randomize')

def calc_det(mat):
    return mat.determinant()

def check_answer(answer, det):
    return answer == det

if __name__ == "__main__":
    square_mat_rows_cols = random.randint(1,5)
    mat = gen_matrix(square_mat_rows_cols, square_mat_rows_cols)
    det = calc_det(mat)
    print("Calculate the determinant of the following matrix: ")
    print(mat)
    answer = int(input("determinant: "))
    if(check_answer(answer, det)):
        print("RIGHT!!")
    else:
        print("FALSE!!")
        print("Right determinant: ", det)

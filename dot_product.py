import math
from typing import Union

def dot_product(x:list [Union[int,float]], y:list [Union[int, float]]) -> float:
    # checking the length of the lists
    if (len(x) != len(y)):
        raise ValueError("Vectors must be of the same length")
    dot_product_sum = []
    for x_iter, y_iter in zip(x, y):
        dot_product_sum.append(x_iter * y_iter)
    dot_product_sum = sum(dot_product_sum)
    return dot_product_sum


if __name__ == "__main__":
    print("Testing the dot product of two lists x and y")
    x_values = [1,2,3,4]
    y_values = [2,2,2,2]

    print(f"dot product of the list is {dot_product(x_values, y_values)}")

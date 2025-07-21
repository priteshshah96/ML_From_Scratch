import math
from typing import Union

def sigmoid(x: Union[int, float]) -> float:
    sig = 1/(1 + math.exp(-x))
    return sig

def sigmoid_derivative(x: float) -> float:
    sig_x = sigmoid(x)
    return sig_x * (1-sig_x)


def vectorized_sigmoid(x: list[Union[int, float]]) -> list[float]:
    sigmoid_list =[]
    for x_iter in x:
        x_sig = sigmoid(x_iter)
        sigmoid_list.append(x_sig)
    return sigmoid_list

def vectorized_sigmoid_derivation(x: list[Union[int, float]]) -> list[float]:
    sigmoid_derivative_list = []
    for x_iter in x:
        X_derivative = sigmoid_derivative(x_iter)
        sigmoid_derivative_list.append(X_derivative)
    return sigmoid_derivative_list

if __name__ == "__main__":
    print("Testing the sigmoid function with hardcoded values of x")
    
    x_values = [0, 1, 0.5, -1, -2.345, 24]
    print(f"sigmoid of the list is {vectorized_sigmoid(x_values)}")
    print(f"sigmoid derivative of the list is {vectorized_sigmoid_derivation(x_values)}")

        

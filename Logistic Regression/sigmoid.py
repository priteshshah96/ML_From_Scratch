import math
from typing import Union

def sigmoid(x: Union[int, float]) -> float:
    sig = 1/(1 + math.exp(-x))
    return sig

def sigmoid_derivative(x: float) -> float:
    sig_x = sigmoid(x)
    return sig_x * (1-sig_x)

if __name__ == "__main__":
    print("Testing the sigmoid function with hardcoded values of x")

    x_values = [0, 1, 0.5, -1, -2.345, 24]
    for x_iter in x_values:
        x_sig= float(x_iter)
        x = sigmoid(x_sig)
        x_derivative = sigmoid_derivative(x_sig)
        print(f"sigmoid({x_sig}) = {x}")
        print(f"sigmoid_derivative({x_sig}) = {x_derivative}")

        

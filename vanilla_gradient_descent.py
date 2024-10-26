import math
import vanilla_math

# An example cost function
def f(x):
    return (x[0][0]+1)**2 + (x[1][0]-2)**2 -2

def gradient_descent(f, x, step, theta, iterations):
    unit_matrix = vanilla_math.unit_matrix(len(x))
    step_directions = vanilla_math.scale(unit_matrix, step)

    # evaluate x at starting point, calc gradient
    for i in range(iterations):
        y = f(x)
        
        gradient = [ [f(vanilla_math.add(x, vanilla_math.getColumn(step_directions, dimension))) - y] for dimension in range(len(unit_matrix))]

        # Movement strategy according to gradient descent
        dx = vanilla_math.scale(gradient, -theta)
        x = vanilla_math.add(x, dx)
    return x

# y is a row vector. Each column contains the expected result for the corresponding column of x (TODO: Generalize to a matrix, consisting of result columns (output layer of NN can be vector))
# x is the input matrix, where each column represents one set of inputs
def cost_avg_of_total_input(x, y):
    n = len(x[0])
    return 1/n * sum([cost_of_individual_input(x_column,y) for x_column in vanilla_math.transpose(x)])

# f is the function to evaluate input x
# y is a single number, the expected result (TODO: Generalize to a vector (output layer of NN can be vector))
# x is a column vector, containing one set of input data
def cost_of_individual_input(f, x,y):
    return (y - f(x))

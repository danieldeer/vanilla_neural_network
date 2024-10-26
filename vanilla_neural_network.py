import math
import vanilla_math
import vanilla_gradient_descent


# output of the network when x is input (essentially this is the function created by the network, tweaked by the parameters w,b (weights, biases)
def a(x, w, b):
    return 0 # TODO: create simple network and evaluate the output based on that


# x is input vector, w is weight vector, b is bias (simple number, not a vector!)
def sigmoid_neuron(x,w,b):
    return sigmoid(vanilla_math.dot_product(w,x) - b)
    
def sigmoid(a):
    return 1/(1+math.exp(-a))


# returns the output vector given the activations / inputs (a) from the previous layer, weights (matrix) and biases
def evaluate_layer(a,w,b):
    mult = vanilla_math.mult(w,a)
    sum = vanilla_math.add(mult, b)
    activations = vanilla_math.apply_function_element_wise(sigmoid, sum)
    return activations


# Evaluate entire network:
# Network consists of multiple layers. Each layer is a matrix
# w is a list of weight matrices, x is the input layer (column vector), b is a list of column vectors,
# each column vector containing the biases for the respective layer
def evaluate_network(x,w,b):
    num_layers = len(b)
    activation = x
    for layer in range(num_layers):
        # Evaluate layer and receive new activations to use as input
        # for the next layer or as output
        activation = evaluate_layer(activation, w[layer], b[layer])

    return activation

# throws an error if the network is not well-defined
def validate_network(x,w,b):
    num_inputs = len(x)
    num_layers = len(w)
    
    # first layer must fit input dimension
    if len(w[0][0]) != num_inputs:
        raise ValueError("Row size of first layer must equal to the column size of input x. Listing w=" + str(w) + ", and x=" + str(x))
    
   
    for layer in range(len(w)):
        # biases of each layer must be same length as row count of w of this layer
        if len(b[layer]) != len(w[layer]):
            raise ValueError("Biases of layer " + str(layer) + " must be equal to row count of w of same layer. Listing w[layer]=" + str(w[layer]) + ", and b[layer]=" + str(b[layer]))

        # output of layer (row count - determines size of output vector)
        # must fit input of next layer (col count) (if it is not the last layer)
        if layer < len(w) -1:
            row_count = len(w[layer])
            col_count_next_layer = len(w[layer + 1][0])
            if row_count != col_count_next_layer:
                raise ValueError("Output of layer " + str(layer) + " is not compatible to next layer.")
            
    
### Tests
# 2 input neurons, 3 layer neurons
# structure: input size 2, layer 1 size is 3, layer 2 size is 2
x = [ [1],[1] ]
w = [ [[2, 1],[0,1], [1,0]] , [[1,1,0], [1,0, 1]] ]
b = [ [[-1], [1], [0.5]], [[-1], [1]] ]

# test layer
validate_network(x,w,b)
layer_res = evaluate_network(x,w,b)
print("Network res: " + str(layer_res))


step = 0.1
theta = 0.1
iterations = 1000

#optimum = gradient_descent(f, x, step, theta, iterations)
#print("Optimium estimated at " + str(optimum)),m 
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


class Network:

    # Initializes a network given the weights (list of matrices for each layer) and biases (list of column vectors for each layer)
    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.validate()

    # Initializes a network given a list of layer sizes
    def __init__(self, layer_sizes):
        w = []
        b = []
        lower_rand = -10
        upper_rand = 10
        for i in range(1,len(layer_sizes)):
            w.append(vanilla_math.create_rand_matrix(layer_sizes[i], layer_sizes[i-1], lower_rand, upper_rand))
            b.append(vanilla_math.create_rand_matrix(layer_sizes[i], 1, lower_rand, upper_rand))
        self.w = w
        self.b = b
        self.validate()

    def str(self):
        return str("w=" + str(self.w) + ", b=" + str(self.b))

    # Evaluate entire network:
    # Network consists of multiple layers. Each layer is a matrix
    # w is a list of weight matrices, x is the input layer (column vector), b is a list of column vectors,
    # each column vector containing the biases for the respective layer
    def calculate_output(self, x):
        num_layers = len(self.b)
        activation = x
        for layer in range(num_layers):
            # Evaluate layer and receive new activations to use as input
            # for the next layer or as output
            activation = evaluate_layer(activation, self.w[layer], self.b[layer])
        return activation

    # throws an error if the network is not well-defined
    def validate(self):
        num_inputs = len(self.w[0][0])
        num_layers = len(self.w)
        
        # first layer must fit input dimension
        if len(self.w[0][0]) != num_inputs:
            raise ValueError("Row size of first layer must equal to the column size of input x. Listing w=" + str(self.w) + ", and x=" + str(self.w[0][0]))

        for layer in range(len(self.w)):
            # biases of each layer must be same length as row count of w of this layer
            if len(self.b[layer]) != len(self.w[layer]):
                raise ValueError("Biases of layer " + str(layer) + " must be equal to row count of w of same layer. Listing w[layer]=" + str(self.w[layer]) + ", and b[layer]=" + str(self.b[layer]))

            # output of layer (row count - determines size of output vector)
            # must fit input of next layer (col count) (if it is not the last layer)
            if layer < len(self.w) -1:
                row_count = len(self.w[layer])
                col_count_next_layer = len(self.w[layer + 1][0])
                if row_count != col_count_next_layer:
                    raise ValueError("Output of layer " + str(layer) + " is not compatible to next layer.")
        
    # x is a list of input column vectors, y is a list of expected output column vectors
    def total_cost(self, x, y):
        # TODO Norm the result vector!!!
        difference_vector_list = [vanilla_math.add(self.calculate_output(x[i]), vanilla_math.negate(y[i])) for i in range(len(x))]
        cost = [sum([difference_row[0]**2 for difference_row in difference_vector]) for difference_vector in difference_vector_list]
        return cost


### Tests
# 2 input neurons, 3 layer neurons
# structure: input size 2, layer 1 size is 3, layer 2 size is 2
x = vanilla_math.create_zero_matrix(2, 1)
layer_sizes = [len(x), 3, 3]
network = Network(layer_sizes)
print("network: " + str(network.str()))

output = network.calculate_output(x)
print("Network res: " + str(output))


# y must be a list of expected results (column vectors), that's why it's nested 3x
y_example = [[[1], [1], [1]]]
cost = network.total_cost([x], y_example)
print("Total cost" + str(cost))

lowest_cost_network = network
lowest_cost_so_far = cost
for i in range(10000):
    print("Bruteforce attempt no. " + str(i) + " current cost is " + str(lowest_cost_so_far))
    # Generate new network
    network = Network(layer_sizes)
    cost_of_this_attempt = network.total_cost([x], y_example)
    if cost_of_this_attempt < lowest_cost_so_far:
        print("Found better network on attempt: " + str(i) + ", with total cost of " + str(cost_of_this_attempt))
        lowest_cost_network = network
        lowest_cost_so_far = cost_of_this_attempt
    
best_network = lowest_cost_network
print("Found best network to be w=" + str(best_network.w) + ", b=" + str(best_network.b))
print("Let's test the input, whether it results in the output: ")
best_network_output = best_network.calculate_output(x)
print("Output y=" + str(best_network_output))

step = 0.1
theta = 0.1
iterations = 1000


#optimum = gradient_descent(f, x, step, theta, iterations)
#print("Optimium estimated at " + str(optimum)),m 
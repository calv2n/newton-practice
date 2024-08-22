def derivative(f, x, epsilon = 0.01):
    return (f(x + epsilon) - f(x)) / epsilon

def second_derivative(f, x):
    return derivative(f, derivative(f, x))

def optimize(x, f):
    x_next = 999
    while x_next - x < 0.1:
        x_next = x - (derivative(f, x) / second_derivative(f, x))
    return f(x_next)
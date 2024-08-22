def derivative(f, x, epsilon = 0.01):
    """Takes first derivative of function f at point x"""
    return (f(x + epsilon) - f(x)) / epsilon

def second_derivative(f, x):
    """Takes second derivative of function f at point x"""
    return derivative(f, derivative(f, x))

def optimize(x, f):
    """Runs Newton's method of optimization for a given function with starting point.
    
    Keyword Arguments:
    x -- Starting position (no default)
    f -- Function to optimize (no default)
    """
    x_next = 999
    while x_next - x < 0.1:
        x_next = x - (derivative(f, x) / second_derivative(f, x))
    return f(x_next)
def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b


def test_sum():
    assert sum(2,3) == 5

def test_sub():
    assert sub(2,5) == -3
    
def test_div():
    assert div(6,0)
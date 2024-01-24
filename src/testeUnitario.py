
def soma(x,y):
    return x+y

def mult(x,y):
    return x*y

def sub(x,y):
    return x-y
def test_soma():
    assert 4==soma(2,2)

def test_mult():
    assert 4==mult(2,2)   

def test_sub():
    assert 0==sub(2,2)    


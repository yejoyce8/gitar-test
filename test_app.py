from app import add, multiply

def test_add():
    assert add(2, 3) == 5  

def test_multiply():
    assert multiply(2, 3) == 6

def test_add_negative_numbers():
    assert add(-2, 3) == 1
    assert add(-5, -3) == -8

def test_add_zero():
    assert add(0, 5) == 5
    assert add(10, 0) == 10
    assert add(0, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-4, -5) == 20

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(10, 0) == 0

def test_multiply_one():
    assert multiply(1, 7) == 7
    assert multiply(9, 1) == 9

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_multiply_large_numbers():
    assert multiply(1000, 2000) == 2000000
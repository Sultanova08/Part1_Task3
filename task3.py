def is_odd (num):
    if num % 2 == 0:
        return False
    else:
        return True
        
def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
test_is_odd()
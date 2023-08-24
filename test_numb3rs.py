from numb3rs import validate

def test_default():
    assert validate("127.0.0.1") == True

def test_max():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"255.512.255.255") == False
    assert validate(r"255.255.512.255") == False
    assert validate(r"255.255.255.512") == False
    assert validate(r"1.2.3.1000") == False

def test_word():
    assert validate(r"cat") == False

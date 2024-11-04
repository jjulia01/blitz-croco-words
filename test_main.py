from main import is_not_valid

def test_is_not_valid():
    assert is_not_valid(" ") == True
    assert is_not_valid(":") == True
    assert is_not_valid("-") == True
    assert is_not_valid("СУПЕРКРОКО") == True
    assert is_not_valid("слово") == False
    
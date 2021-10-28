from src.main import calculate_median,calculate_mode

def test_calculate_median():
    assert calculate_median([1,2,3,4,5])==3
    assert calculate_median([1,2,3,4,5,6])==3.5

def test_calculate_mode():
    assert calculate_mode([1,2,3,3,4,5])==3
    assert calculate_mode([1,2,3,3,5,5,5,4,5])==5


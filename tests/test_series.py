from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci_test ():
    expected = 5
    actual = fibonacci(5)
    assert  expected == actual

def test_lucas_test ():
    expected = 11 
    actual = lucas(5)
    assert expected == actual

def test_sum_series_fibonacci ():
    expected = 5 #number of the result of sum [0,1,2,3,4,5] 
    actual = sum_series(5)
    assert expected == actual

def test_sum_series_lucas() : 
    expected = 11 #number of [2, 1, 3, 4, 7, 11]
    actual = sum_series(5,2,1)
    assert expected == actual

def test_sum_series_custom():
    expected = 13 #number of  [5, 1, 6, 7, 13, ...]
    actual = sum_series(4,5,1)
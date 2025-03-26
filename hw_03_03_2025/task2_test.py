import pytest
from task2 import StatisticsCalculator  

def test_mean():
    calc = StatisticsCalculator([1, 2, 3, 4, 5])
    assert calc.mean() == 3

def test_median_odd():
    calc = StatisticsCalculator([1, 2, 3, 4, 5])
    assert calc.median() == 3

def test_median_even():
    calc = StatisticsCalculator([1, 2, 3, 4, 5, 6])
    assert calc.median() == 3.5

def test_variance():
    calc = StatisticsCalculator([1, 2, 3, 4, 5])
    assert calc.variance() == 2.5

def test_empty_list_mean():
    calc = StatisticsCalculator([])
    with pytest.raises(ValueError, match="у вас пустой лист"):
        calc.mean()

def test_empty_list_median():
    calc = StatisticsCalculator([])
    with pytest.raises(ValueError, match="у вас пустой лист"):
        calc.median()

def test_empty_list_variance():
    calc = StatisticsCalculator([])
    with pytest.raises(ValueError, match="у вас пустой лист"):
        calc.variance()

def test_large_numbers():
    calc = StatisticsCalculator([10**6, 10**7, 10**8])
    assert calc.mean() == (10**6 + 10**7 + 10**8) / 3

def test_floating_point_numbers():
    calc = StatisticsCalculator([1.5, 2.5, 3.5])
    assert calc.mean() == 2.5
    assert calc.median() == 2.5
    assert calc.variance() == 0.8333333333333334

if __name__ == "__main__":
    pytest.main()
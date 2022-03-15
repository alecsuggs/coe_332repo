from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes

import pytest

def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')

def test_check_hemisphere():
    assert check_hemisphere(50.775, 6.08333) == "Northern & Eastern"
    assert check_hemisphere(-31.6, 6.08333) == "Southern & Eastern"
    assert check_hemisphere(5, -10) == "Northern & Western"
    assert check_hemisphere(-5, -10) == "Southern & Western"
    with pytest.raises(TypeError):
        check_hemisphere("k","f")

def test_count_classes():
    assert isinstance(count_classes([{'a': 1}, {'a': 2}], 'a'), dict) == True
    assert count_classes([{'a': "g"}, {'a': 'g'}],'a') == {'g':2}
    with pytest.raises(TypeError):
        count_classes(2,2)
    assert count_classes([{'a': 'hh'}, {'a': 'g'}],'a') == {'hh':1, 'g':1}
    assert count_classes([{'a': "k"}, {'a': 'k'}], 'a') == {'k': 2}

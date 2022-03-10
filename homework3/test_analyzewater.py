from analyzewater import turbidity
from analyzewater import threshold
from analyzewater import issafe
import pytest


def test_turbidity():
    assert turbidity(5, 5) == 25
    assert turbidity(1, 1) == 1
    assert turbidity(0.5, 0.1) == 0.05
    assert isinstance(turbidity(1, 1.115), float) == True
    with pytest.raises(TypeError):
        turbidity('x', 'b')

def test_threshold():
    assert threshold(1,1.1992,0.02) == 8.999999999999984
    assert threshold(1,1,0.02) == 0.1
    assert threshold(1,0.98,0.02) == 0
    assert isinstance(threshold(1,1.1992,0.02), float) == True
    with pytest.raises(TypeError):
        threshold('x','b','d')

def test_issafe():
    assert issafe(1,0.98,0.02,0) == True
    assert issafe(1,2,0.02,0) == False
    assert issafe(1,1,0.02,0) == False
    assert isinstance(issafe(1,2,0.02,0), bool) == True
    with pytest.raises(TypeError):
        issafe('m','b','c','s')

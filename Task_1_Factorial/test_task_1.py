import pytest
from task_1 import factorial
from task_1 import COSNT_MAX_N

def test_factorial_differtentWorkersCount_theSameResult():
    n = 6

    assert factorial(n,1) == factorial(n,5)

def test_factorial_success():
    n = 23
    fact = 1

    for i in range(1,n+1):
        fact = fact * i

    assert factorial(n,5) == fact

def test_factorial_0_success():
    n = 0

    assert factorial(n,5) == 1

def test_factorial_1_success():
    n = 1

    assert factorial(n,5) == 1

def test_factorial_n_belowZero_exception():
    with pytest.raises(Exception):
        x = factorial(-1,5)

def test_factorial_n_moreThanMaxN():
    with pytest.raises(Exception):
        x = factorial(COSNT_MAX_N+1,5)

def test_factorial_incorrectN_exception():
    with pytest.raises(Exception):
        x = factorial(5.5,5)

def test_factorial_incorrectNumberOfWorkers_exception():
    with pytest.raises(Exception):
        x = factorial(5,5.5)
import pytest
@pytest.mark.fast

def test_my_fast_test():
    a = "Bauyrzhan"

def add(q,v):
    return q + v

def test_add():
    assert add(1,1)== 2
    assert add(0,0)== 0


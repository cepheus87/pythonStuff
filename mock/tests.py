from unittest import mock

from funcs import f2
from funcs2 import f3
import pytest

def new_f(a):
    return a + 10

@mock.patch("funcs.f1", return_value=2)
def test(*mocked):
    val = 5
    assert f2(val) == 2


"""
!!!!
Although f1 is in funcs, but it is imported in funcs2 and we have to mock it in in module where it was imported -> funcs2 
!!!!
"""
@pytest.mark.skip()
@mock.patch("funcs.f1", return_value=2)
def test2(*mocked):
    val = 5
    assert f3(val) == 2

@mock.patch("funcs2.f1", return_value=2)
def test3(*mocked):
    val = 5
    assert f3(val) == 2


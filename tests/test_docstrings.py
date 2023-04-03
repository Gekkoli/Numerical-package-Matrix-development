from importlib import import_module
import doctest

module = import_module("mpm_la.functions")


def test_dstr():
    assert doctest.testmod(module).failed == 0

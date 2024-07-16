import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("input_str, result", [
    ("skypro", "Skypro"),
    ("hello, alina", "Hello, Alina"),
    ("", ""),
])
def test_capitilize(input_str, result):
    utils = StringUtils()
    res = utils.capitilize(input_str)
    assert res == result

@pytest.mark.parametrize("input_str, result", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("  ", ""),
])
def test_trim(input_str, result):
    utils = StringUtils()
    res = utils.trim(input_str)
    assert res == result

@pytest.mark.parametrize("input_str, delimiter, expected_result", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
])
def test_to_list(input_str, delimiter, expected_result):
    utils = StringUtils()
    result = utils.to_list(input_str, delimiter)
    assert result == expected_result

@pytest.mark.parametrize("input_str, symbol, expected_result", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
])
def test_contains(input_str, symbol, expected_result):
    utils = StringUtils()
    result = utils.contains(input_str, symbol)
    assert result == expected_result

@pytest.mark.parametrize("input_str, symbol, expected_result", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "a", ""),
])
def test_delete_symbol(input_str, symbol, expected_result):
    utils = StringUtils()
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected_result

@pytest.mark.parametrize("input_str, symbol, expected_result", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "a", False),
])
def test_starts_with(input_str, symbol, expected_result):
    utils = StringUtils()
    result = utils.starts_with
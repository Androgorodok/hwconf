import pytest
from parser import parser
from transformer import ConfigTransformer

def run(src: str):
    tree = parser.parse(src)
    return ConfigTransformer().transform(tree)

def test_number():
    result = run("a is 10")
    assert result["a"] == 10

def test_string():
    result = run('a is @"hello"')
    assert result["a"] == "hello"

def test_array():
    result = run("a is {1, 2, 3}")
    assert result["a"] == [1, 2, 3]

def test_const_ref():
    result = run("""a is 5
b is |a|""")
    assert result["b"] == 5

def test_unknown_const():
    with pytest.raises(Exception) as exc_info:
        run("a is |b|")
    assert any("Неизвестная константа" in str(e) for e in [exc_info.value] + list(exc_info.value.__context__.args if exc_info.value.__context__ else []))

def test_complex_array():
    result = run('arr is {1, @"text", 3}')
    assert result["arr"] == [1, "text", 3]

def test_nested_constants():
    src = """
baseport is 8000
appport is |baseport|
apiport is |baseport|
"""
    result = run(src)
    assert result["appport"] == 8000
    assert result["apiport"] == 8000

def test_multiple_statements():
    src = """
timeout is 30
host is @"example.com"
ports is {80, 443, 8080}
"""
    result = run(src)
    assert result["timeout"] == 30
    assert result["host"] == "example.com"
    assert result["ports"] == [80, 443, 8080]

def test_empty_array():
    result = run("empty is {}")
    assert result["empty"] == []

def test_string_with_spaces():
    result = run('msg is @"Hello World with spaces"')
    assert result["msg"] == "Hello World with spaces"

def test_nested_arrays():
    """Массивы внутри массивов"""
    result = run('nested is {{1, 2}, {3, 4}}')
    assert result["nested"] == [[1, 2], [3, 4]]

def test_const_in_nested_array():
    """Константы во вложенных массивах"""
    src = """
a is 10
b is 20
deep is {{|a|, |b|}, {30, {40, 50}}}
"""
    result = run(src)
    assert result["deep"] == [[10, 20], [30, [40, 50]]]

def test_array_with_constants():
    src = """
x is 10
y is 20
points is {|x|, |y|, 30}
"""
    result = run(src)
    assert result["points"] == [10, 20, 30]

def test_mixed_array():
    result = run('mixed is {1, @"two", 3, @"four"}')
    assert result["mixed"] == [1, "two", 3, "four"]

def test_invalid_names_rejected():
    """Имена с подчеркиваниями должны вызывать ошибку парсинга"""
    with pytest.raises(Exception):
        run("invalid_name is 42")

def test_invalid_number_starts_with_zero():
    """Числа не могут начинаться с 0"""
    with pytest.raises(Exception):
        run("port is 08080")

def test_name_with_digits_rejected():
    """Имена с цифрами должны вызывать ошибку"""
    with pytest.raises(Exception):
        run("port2 is 80")
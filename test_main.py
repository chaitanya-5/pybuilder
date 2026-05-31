from main import greet, add


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(1, 2) == 3
    assert add(0.5, 0.5) == 1.0
    assert add(-1, 1) == 0

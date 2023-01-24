from hexlet_pytest.stack import make_stack


def test_make_stack():
    assert make_stack(5) == [0, 1, 2, 3, 4, 5]


def test_empty_list():
    assert make_stack(0) == []
    assert make_stack(-1) == []

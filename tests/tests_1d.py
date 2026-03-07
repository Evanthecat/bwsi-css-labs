from labs.lab_1.lab_1d import two_sum


def test_zero():
    assert two_sum([1, 0, 0], 0) == [1, 2]
    assert two_sum([0, 0, 2], 2) == [1, 2]
    assert two_sum([1, 2, 0], 3) == [0, 1]


def test_some():
    assert two_sum([1, 4, 3], 7) == [1, 2]
    assert two_sum([7, 5, 1], 12) == [0, 1]
    assert two_sum([2, 7, 1], 3) == [0, 2]
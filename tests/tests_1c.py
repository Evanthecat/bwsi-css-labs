from labs.lab_1.lab_1c import max_subarray_sum


def test_one():
    assert max_subarray_sum([-2, -4, -7]) == -2
    assert max_subarray_sum([-6, -3, -9]) == -3
    assert max_subarray_sum([-2, 0, -5]) == 0


def test_all():
    assert max_subarray_sum([2, 4, 7]) == 13
    assert max_subarray_sum([5, 2, 8]) == 15
    assert max_subarray_sum([8, 0, 1]) == 9


def test_some():
    assert max_subarray_sum([-2, 4, 7]) == 11
    assert max_subarray_sum([-2, -4, -7, 5, 2]) == 7
    assert max_subarray_sum([8, -5, 2, -2]) == 8
"""
Test count_islands(map).
These example based tests cover the obvious cases.

Property based testing would objective the testing.
"""
import pytest

from islands import count_islands

def test_no_islands():
    map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert count_islands(map) == 0


def test_1_simple_island():
    map = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert count_islands(map) == 1


def test_1_two_row_island():
    map = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert count_islands(map) == 1


def test_2_islands():
    map = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert count_islands(map) == 2


def test_3_islands():
    map = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ]

    assert count_islands(map) == 3


def test_1_big_island():
    map = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
    ]

    assert count_islands(map) == 1

import pytest

from homeworks import Romb, sum_numbers, longest_word


# ---------- Romb ----------

def test_romb_created_with_valid_data():
    romb = Romb(10, 60)
    assert romb.side_a == 10


def test_corner_b_calculated_automatically():
    romb = Romb(10, 60)
    assert romb.corner_b == 120


def test_corners_sum_is_180_after_changing_corner_b():
    romb = Romb(10, 60)
    romb.corner_b = 1
    assert romb.corner_a + romb.corner_b == 180


def test_invalid_side_raises_error():
    with pytest.raises(ValueError):
        Romb(0, 60)


# ---------- sum_numbers ----------

def test_sum_numbers_regular_case():
    assert sum_numbers("1,2,3,4") == 10


def test_sum_numbers_single_number():
    assert sum_numbers("5") == 5


def test_sum_numbers_with_letters_raises_error():
    with pytest.raises(ValueError):
        sum_numbers("qwerty1,2,3")


# ---------- longest_word ----------

def test_longest_word_regular_text():
    assert longest_word("cat dog elephant") == "elephant"


def test_longest_word_single_word():
    assert longest_word("hello") == "hello"


def test_longest_word_empty_text_raises_error():
    with pytest.raises(ValueError):
        longest_word("")
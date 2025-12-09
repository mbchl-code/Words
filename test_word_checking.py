import pytest

from words_checking import points_in_step

def test_points_in_step_plus():
    assert points_in_step("НОРМА", "КИНОПАНОРАМА") == 5
    assert points_in_step("КИНО", "КИНОПАНОРАМА") == 4
    assert points_in_step("КРОНА", "КИНОПАНОРАМА") == 5

def test_points_in_step_minus():
    assert points_in_step("ЦЩ", "КИНОПАНОРАМА") == -2
    assert points_in_step("ЯБЬ", "КИНОПАНОРАМА") == -3
    assert points_in_step("ЧУШХ", "КИНОПАНОРАМА") == -4
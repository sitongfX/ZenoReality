from pytest import mark
from connecting_serial_controller import connect_ser
from keyboard_input import audio_adjust, color_adjust


# sample
# @mark.parametrize("input_data", "output", [(1,2),(3,4)])
# def test_something(some_input, some_output):
#     assert myfunc(input_data) == output


def test_game_is_not_connected():
    serial = connect_ser
    assert serial != True

def test_audio_is_muted():
    result = audio_adjust('m')
    assert result == 0

def test_audio_is_not_adjusted():
    result = audio_adjust('c')
    assert result != 0

def test_color_is_adjusted():
    result = color_adjust('c')
    assert result == 3

def test_color_is_not_adjusted():
    result = color_adjust('m')
    assert result != 3


# pytest -vvv my_lib_folder \
#     --cov=my_library_name \
#     --cov-branch

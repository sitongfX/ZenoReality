from connecting_serial_controller import connect_ser
from keyboard_input import audio_adjust, color_adjust
from controller_input import parse_multiple_data, parse_single_data


def test_game_is_not_connected():
    serial = connect_ser
    assert serial != True


def test_audio_is_muted():
    result = audio_adjust("m")
    assert result == 0


def test_audio_is_not_adjusted():
    result = audio_adjust("c")
    assert result != 0


def test_color_is_adjusted():
    result = color_adjust("c")
    assert result == 3


def test_color_is_not_adjusted():
    result = color_adjust("m")
    assert result != 3


def test_parse_multiple_json():
    input = "{'dt':'123','sed':'456'}"
    result = parse_multiple_data(input)
    assert len(result) == 2


def test_parse_multiple_json():
    input = "{'dt':'123'}"
    result = parse_multiple_data(input)
    assert len(result) == 1
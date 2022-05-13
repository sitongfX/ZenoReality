volume = 40


def audio_adjust(key_input):
    """
    This function allows the user to mute the audio
    """
    if key_input == "m":
        volume = 0
        return volume

color = 1


def color_adjust(key_input):
    """
    This function allows the user to randomly adjust the color
    """
    if key_input == "c":
        color = 3
        # set color as color.rgb(randint(0,255), randint(0,255),randint(0,255))
        return color

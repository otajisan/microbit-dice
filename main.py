dice = 0

def on_button_pressed_a():
    global dice
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    dice = randint(1, 6)
    if dice == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif dice == 2:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            """)
    elif dice == 3:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . .
            """)
    elif dice == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif dice == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    elif dice == 6:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_a():
    dice = randint(1, 6)

    if dice == 1:
        basic.show_animation("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    elif dice == 2:
        basic.show_animation("""
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        """)
    elif dice == 3:
        basic.show_animation("""
        . . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . .
        """)
    elif dice == 4:
        basic.show_animation("""
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        """)
    elif dice == 5:
        basic.show_animation("""
        # . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . #
        """)
    elif dice == 6:
        basic.show_animation("""
        # . . . #
        . . . . .
        # . . . #
        . . . . .
        # . . . #
        """)

input.on_button_pressed(Button.A, on_button_pressed_a)
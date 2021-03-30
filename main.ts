let dice = 0
input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Eighth))
    dice = randint(1, 6)
    if (dice == 1) {
        basic.showAnimation(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    } else if (dice == 2) {
        basic.showAnimation(`
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        `)
    } else if (dice == 3) {
        basic.showAnimation(`
        . . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . .
        `)
    } else if (dice == 4) {
        basic.showAnimation(`
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        `)
    } else if (dice == 5) {
        basic.showAnimation(`
        # . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . #
        `)
    } else if (dice == 6) {
        basic.showAnimation(`
        # . . . #
        . . . . .
        # . . . #
        . . . . .
        # . . . #
        `)
    }
})

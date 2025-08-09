def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 4 4 . . . . . . .
            . . . . . . 4 5 5 4 . . . . . .
            . . . . . . 2 5 5 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    sprites.destroy(otherSprite)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

enemyShip: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        ....ffffff.........ccc..
        ....ff22ccf.......cc4f..
        .....ffccccfff...cc44f..
        ....cc24442222cccc442f..
        ...c9b4422222222cc422f..
        ..c999b2222222222222fc..
        .c2b99111b222222222c22c.
        c222b111992222ccccccc22f
        f222222222222c222ccfffff
        .f2222222222442222f.....
        ..ff2222222cf442222f....
        ....ffffffffff442222c...
        .........f2cfffc2222c...
        .........fcc2ffffffff...
        ..........fc2ffff.......
        ...........fffff........
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(5)

def on_update_interval():
    global enemyShip
    enemyShip = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . d d d d . . . . . .
            . . . . d d d d d d d d . . . .
            . . . d d d d d d d d d d . . .
            . . d d d d d d d d f f d d . .
            . . d d d d d d d d f f d d . .
            . d d d d d d d d d d d d d d .
            . d d d d d d d d d d d d d d .
            . d d f d d d d d d d d d d d .
            . d d f f d d d d d d d d d d .
            . . d f f d d d d d d d f d . .
            . . d f f f f d d d d f d d . .
            . . . d d f f f f f f f d d . .
            . . . . d d f f f f d d . . . .
            . . . . . . d d d d . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    enemyShip.x = scene.screen_width()
    enemyShip.vx = -20
    enemyShip.y = randint(10, scene.screen_height() - 1)
game.on_update_interval(2000, on_update_interval)

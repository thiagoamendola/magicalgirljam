
style life_bar:
    #color "#f00"
    xysize(200,25)
    pos (20,20)

style magic_bar:
    #color "#0f0"
    xysize(200,25)
    pos (20,45)

style enemy_bar:
    #color "#0f0"
    xysize(200,25)
    anchor (1.0, 0.0)
    pos (200,60)
    #pos (920,20)
    #bar_invert True


screen bars:
    # Life Bar
    bar:
        style "life_bar"
        value player.HP
        range player.MAXHP

    # Magic Bar
    bar:
        style "magic_bar"
        value player.MAGIC
        range player.MAXMAGIC
    
    # Enemy Life Bar
    bar:
        style "enemy_bar"
        value enemy.HP
        range enemy.MAXHP



init python:

    # class TurnBasedDisplayable(renpy.Displayable):

    #     def __init__(self):

    #         renpy.Displayable.__init__(self)


    #     # Recomputes the position of the ball, handles bounces, and
    #     # draws the screen.
    #     def render(self, width, height, st, at):

    #         # The Render object we'll be drawing into.
    #         r = renpy.Render(width, height)

    #         # Ask that we be re-rendered ASAP, so we can show the next
    #         # frame.
    #         renpy.redraw(self, 0)

    #         # Return the Render object.
    #         return r
        

    #     # Handles events.
    #     def event(self, ev, x, y, st):

    #         import pygame
    
    class Player:

        def __init__(self):
            self.ATTACK = 1
            self.DEFENSE = 0
            self.HP = 10
            self.ACCURACY = 100
            self.AGILITY = 100
            self.MAGIC = 10
    

    class PlayerMagic:

        def __init__(self, name, cost, damage, effect_list, description):
            self.NAME = name
            self.COST = cost
            self.DAMAGE = damage
            self.ACCURACY = 100
            self.EFFECT_LIST = effect_list
            self.DESCRIPTION = description

    
    class Enemy:

        def __init__(self):
            self.MAXHP = 9
            self.HP = self.MAXHP
            self.DEFENSE = 0
            self.ATTACK = 0
            self.ACCURACY = 100
            self.AGILITY = 100


    player = None
    enemy = None

    # def game_setup():





transform hpunch_sprite:
    linear 0.090 xoffset -10 #-offset to keep Character in place
    linear 0.090 xoffset +0 #+offset to move Character
    repeat 4 #Repeats



label play_turnbased:

    window hide

    #call screen turnbased

#screen turnbased():

    #add "bg turnbased field"

    #default turnbased = TurnBasedDisplayable()

    #add turnbased


    scene bg lecturehall

    show mahoumike stance at left
    show m_first neutral at topright
    python:
        # game_setup()
        player = Player()
        enemy = Enemy()

    call .game_loop

    "FIN"

    return


label .game_loop:

    $ battle_end = False

    while(not battle_end):

        "Select action"

        show mahoumike at hpunch_sprite

        python:
            damage=player.ATTACK*3
            enemy.HP-=damage

        pause 1.0

        show m_first at hpunch_sprite

        pause 1.0

        "Mike caused [damage] damage"
        "Monster now has [enemy.HP] life left"

        python:
            if enemy.HP<=0:
                battle_end = True


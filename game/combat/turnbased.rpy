init python:

    class TurnBasedDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)


        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r
        

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame
    
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
            self.HP = 0
            self.DEFENSE = 0
            self.ATTACK = 0
            self.ACCURACY = 100
            self.AGILITY = 100



screen turnbased():

    default turnbased = TurnBasedDisplayable()

    #add "bg turnbased field"
    add "bg lecturehall"

    add turnbased


label play_turnbased:

    window hide

    call screen turnbased

    window show

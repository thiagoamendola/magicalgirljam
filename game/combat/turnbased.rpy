init python:
    
    class Player:

        def __init__(self):
            self.ATTACK = 1
            self.DEFENSE = 0
            self.MAXHP = 10
            self.HP = self.MAXHP
            self.ACCURACY = 100
            self.AGILITY = 100
            self.MAXMAGIC = 10
            self.MAGIC = self.MAXMAGIC

            self.magic_list = []
            self.magic_list.append(PlayerMagic(
                "Fireball", 3, 3, {},
                "Casts a fire ball that causes 3 damage"
            ))
            self.magic_list.append(PlayerMagic(
                "Thunderstorm", 6, 2, {'hits':4, 'accuracy':0.5},
                "Casts 4 thunders that causes 2 damage and have 50% of hitting the target"
            ))
            self.magic_list.append(PlayerMagic(
                "Earthquake", 4, 3, {'stun':True, 'effect_accuracy':0.5},
                "Casts earthquake that causes 3 damage and have 50% of stunning the target for 1 turn"
            ))
            self.magic_list.append(PlayerMagic(
                "Waterheal", 4, 5, {'cure':True},
                "Heals 5 health points"
            ))

        #     self.defend = false


        # def setup_turn(self):
        #     self.defend = false

    

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


        def setup_turn(self):
            return


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

    "A wild monster appears!"

    $ battle_end = False

    call .player_action
    
    
    while(not battle_end):

        call .player_action
    
        if enemy.HP <= 0:
            $ battle_end = True

        if not battle_end:
            "Monster stood still because its behavior wasn't implemented yet"
        else:
            "Monster was defeated"

    return



label .player_action:

    menu:
        "Mahou!":
            python:
                menu_items=[]
                for magic in player.magic_list:
                    menu_items.append((magic.NAME, magic))
                selected_magic = menu(menu_items)
            call .use_magic(selected_magic)

        "Hit with Staff": #Weak attack that recovers small amount of mana
            call .staff_attack
        
        "Focus": #Recovers mana and take half damage for 1 turn
            call .defend

    return


label .staff_attack:
    # Hit with low damage
    # Recover small amount of mana
    "Not implemented yet"
    return


label .defend:
    # Recover huge amount of mana
    # Send defense
    "Not implemented yet"
    return


label .use_magic(magic):
    python:
        # Remove mana
        player.MAGIC -= magic.COST

        hits = 1
        # Apply effects
        # List of effects so far: 'hits', 'accuracy', 'stun', 'cure', 'effect_accuracy', 

        # Apply magic damage
        enemy.HP -= magic.DAMAGE


    show mahoumike at hpunch_sprite

    pause 1.0

    show m_first at hpunch_sprite

    pause 1.0

    "Mike used [magic.NAME]."
    "It caused [magic.DAMAGE] damage"
    "Monster now has [enemy.HP] life left"
    
    return
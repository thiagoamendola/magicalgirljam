init python:
    
    STAFF_MAGIC_RECOVERY = 3
    DEFEND_MAGIC_RECOVERY = 6
    STUN_DURATION = 2 #

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
            self.STAFFDAMAGE = 1

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
                "Earthquake", 4, 2, {'stun':True, 'effect_accuracy':0.5},
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

        def __init__(self, maxhp, name, description, main_attacks, special_attacks):
            self.MAXHP = 9
            self.HP = self.MAXHP
            self.NAME = name
            self.DESCRIPTION = description
            self.MAINATTACKS = main_attacks
            self.SPECIALATTACKS = special_attacks
            self.MOVE_COUNTER = 0


    class EnemyAttacks:
        
        def __init__(self, name, damage, effect_list):
            self.NAME = name
            self.DAMAGE = damage
            self.EFFECT_LIST = effect_list


    enemy_dict = {
        "first": Enemy(
            9,
            "Birdmon",
            "An aggressive magical creature that likes to hunt alone",
            [
                EnemyAttacks(
                    "Headbutt", 2, {},
                )
            ],
            {
                3: EnemyAttacks(
                    "Diving Claw", 4, {},
                )
            }
        )
    }


    player = None
    enemy = None






transform hpunch_sprite:
    linear 0.090 xoffset -10 #-offset to keep Character in place
    linear 0.090 xoffset +0 #+offset to move Character
    repeat 4 #Repeats



label play_turnbased:

    window hide

    scene bg lecturehall

    show mahoumike stance at left
    show m_first neutral at topright

    show screen bars

    python:
        # game_setup()
        player = Player()
        enemy = enemy_dict[battle]

    call .game_loop

    "FIN"

    return


label .game_loop:

    "A wild monster appears!"

    $ battle_end = False

    while(not battle_end):

        "You have [player.HP] HP and [player.MAGIC] magic points."

        call .player_action
    
        if enemy.HP <= 0:
            "Monster was defeated!"
            $ battle_end = True
        elif enemy.HP <= 0:
            "You died!"
            $ battle_end = True
        else:
            call .monster_action

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
    python:
        player.MAGIC = min(player.MAGIC+STAFF_MAGIC_RECOVERY, player.MAXMAGIC)
        enemy.HP = max(enemy.HP-player.STAFFDAMAGE, 0)
    # Recover small amount of mana
    "Mike attacks with the staff, recovering [STAFF_MAGIC_RECOVERY] magic and dealing [player.STAFFDAMAGE] damage."
    return


label .defend:
    # Recover huge amount of mana
    python:
        player.MAGIC = min(player.MAGIC+DEFEND_MAGIC_RECOVERY, player.MAXMAGIC)
    # Set defense
    "Mike concentrates, recovering [DEFEND_MAGIC_RECOVERY] magic and defending this turn."
    return


label .use_magic(magic):
    python:
        # Remove mana
        player.MAGIC -= magic.COST
        # Setup initial parameters
        hits = 1
        accuracy = 1.0
        cure = False
        effect_accuracy = 1.0
        status_effects = []
        # Apply effects
        # List of effects so far: 'hits', 'accuracy', 'stun', 'cure', 'effect_accuracy', 
        for effect in magic.EFFECT_LIST.keys():
            if effect == 'hits':
                hits = magic.EFFECT_LIST[effect]
            elif effect == 'accuracy':
                accuracy = magic.EFFECT_LIST[effect]
            elif effect == 'cure':
                cure = True
            elif effect == 'effect_accuracy':
                effect_accuracy = magic.EFFECT_LIST[effect]
            elif effect == 'stun':
                status_effects.append('stun')

    $ hit_success = True

    "Mike used [magic.NAME]."

    $i = 0
    while i < hits:
        $i += 1

        show mahoumike at hpunch_sprite

        pause 1.0

        python:
            # Check hit and apply effects
            if renpy.random.random() <= accuracy:
                hit_success = True
                # Apply magic damage
                if not cure:
                    enemy.HP = max(enemy.HP-magic.DAMAGE, 0)
                else:
                    player.HP = min(player.HP+magic.DAMAGE, player.MAXHP)
                
                # Check effect_accuracy
                if renpy.random.random() <= effect_accuracy:
                    for effect in magic.EFFECT_LIST.keys():
                        if effect == 'stun':
                            # IMPLEMENT STUN
                            pass
            else:
                hit_success = False

        if hit_success:
            show m_first at hpunch_sprite
            pause 1.0
            "It caused [magic.DAMAGE] damage."
        
        else:
            "[magic.NAME] missed."
        
    "[enemy.NAME] now has [enemy.HP] life left."
    
    return


label .monster_action():

    python:
        move = ""

        enemy.MOVE_COUNTER += 1

        # IMPROVE THE MOVE SELECTION
        if enemy.MOVE_COUNTER >= enemy.SPECIALATTACKS.keys()[0]:
            move = enemy.SPECIALATTACKS[enemy.SPECIALATTACKS.keys()[0]]
            enemy.MOVE_COUNTER = 0
        else:
            move = enemy.MAINATTACKS[0]

        player.HP = max(player.HP-move.DAMAGE, 0)
    
    "[enemy.NAME] used [move.NAME], causing [move.DAMAGE] damage."

    return
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mike = Character("Mike", color="#ccc")
define lucy = Character("Lucy", color="#f00")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mike happy

    # These display lines of dialogue.

    mike "Hello. Are you there?"

    mike "My name is Mike and this is the story of how I became a Magical Girl."

    mike "Before we start, call you tell me your name?"

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Guy Shy")
 
    show mike concerned:
        xalign 0.65
        yalign 1.0
    with move

    mike "..."

    show mike concerned:
        xalign 0.9
        yalign 1.0
    with move

    mike "..."

    transform partiallyoutright:
        xalign 1.25
        yalign 1.0
    
    show mike concerned at partiallyoutright
    with move

    mike "..."

    show mike concerned:
        xalign 1.4
        yalign 1.0
    with move

    "..."

    define slowdissolve = Dissolve(0.5)

    show mike happy at center
    with slowdissolve

    mike "I'm back!"

    mike "Hey! Wait!"

    play audio "audio/punch.opus"
    with vpunch

    pause 1.0

    show mike vhappy

    mike "Sorry! Your face was so punchable right now"
    
    show mike happy

    mike "Wait! Hold still..."

    play audio "audio/punch.opus"
    with hpunch

    pause 1.0

    mike "Was it a fly? Oh, it's just a spot in your face."

    queue sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"

    pause 4.0

    show mike concerned

    mike "Oh my god! We're running late!"

    menu:

        "Let's hurry up!":
            jump choice1_go

        "Nah... I don't wanna go.":
            jump choice1_stay

    label choice1_go:

        $ hurry = True

        mike "Nah, whatever. I don't wanna go anymore."

        jump choice1_done

    label choice1_stay:

        $ hurry = False

        mike "You're so lazy!"

        jump choice1_done

    label choice1_done:

        show mike happy

        mike "Let's just stay here. Such cool and... rocky place."

        define quickdissolve = Dissolve(0.2)


        lucy "HEY! THERE YOU ARE!"

        show lucy mad at right
        with quickdissolve

        show mike concerned at left
        with move

        if hurry:

            lucy "You're so lazy, Mike!"
            with hpunch
        else:

            lucy "You're both too lazy!"
            with hpunch

        lucy "[name], you shouldn't follow Mike's behavior. It's a path with no return!"

        mike "C'mon! Let's just chill here!"
        
        return
 


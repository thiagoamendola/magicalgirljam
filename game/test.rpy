# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ana = Character("Ana", color="#ccc")
define lucy = Character("Lucy", color="#f00")

# The game starts here.

label test:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/sunflower-slow-drag.ogg" fadeout 1
 
    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ana happy

    # These display lines of dialogue.

    ana "Hello. Are you there?"

    ana "My name is ana and this is the story of how I became a Magical Girl."

    ana "Before we start, call you tell me your name?"

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Guy Shy")
 
    show ana concerned:
        xalign 0.65
        yalign 1.0
    with move

    ana "..."

    show ana concerned:
        xalign 0.9
        yalign 1.0
    with move

    ana "..."

    transform partiallyoutright:
        xalign 1.25
        yalign 1.0
    
    show ana concerned at partiallyoutright
    with move

    ana "..."

    show ana concerned:
        xalign 1.4
        yalign 1.0
    with move

    "..."

    define slowdissolve = Dissolve(0.5)

    show ana happy at center
    with slowdissolve

    ana "I'm back!"

    ana "Hey! Wait!"

    play audio "audio/punch.opus"
    with vpunch

    pause 1.0

    show ana vhappy

    ana "Sorry! Your face was so punchable right now"
    
    show ana happy

    ana "Wait! Hold still..."

    play audio "audio/punch.opus"
    with hpunch

    pause 1.0

    ana "Was it a fly? Oh, it's just a spot in your face."

    queue sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"

    pause 4.0

    show ana concerned

    ana "Oh my god! We're running late!"

    menu:

        "Let's hurry up!":
            jump choice1_go

        "Nah... I don't wanna go.":
            jump choice1_stay

    label choice1_go:

        $ hurry = True

        ana "Nah, whatever. I don't wanna go anymore."

        jump choice1_done

    label choice1_stay:

        $ hurry = False

        ana "You're so lazy!"

        jump choice1_done

    label choice1_done:

        show ana happy

        ana "Let's just stay here. Such cool and... rocky place."

        define quickdissolve = Dissolve(0.2)


        lucy "HEY! THERE YOU ARE!"

        show lucy mad at right
        with quickdissolve

        show ana concerned at left
        with move

        if hurry:

            lucy "You're so lazy, ana!"
            with hpunch
        else:

            lucy "You're both too lazy!"
            with hpunch

        lucy "[name], you shouldn't follow ana's behavior. It's a path with no return!"

        ana "C'mon! Let's just chill here!"
        
        jump play_turnbased

        return
 


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mike = Character("Mike", color="#ccc")
define john = Character("John", color="#ff0")
define lucy = Character("Ana", color="#f00")

# The game starts here.

label intro:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #play music "audio/sunflower-slow-drag.ogg" fadeout 1
 
    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mike neutral:
        xalign 0.25
        yalign 1.0

    # These display lines of dialogue.

    mike "Hello, John. Are you there?"

    john "Sure! Let's play a ranked! I'm craving to stomp some feeders!"

    mike "Me too! Had to channel my anger."
    
    mike "This week was a mess! Everyone's so annoying!"

    "=== RECHEIO ==="

    show lucy mad at right

    lucy "Mike! Dinner's ready! Come downstairs!"

    mike "MOM! I AM PLAYING ONLINE! I CAN'T PAUSE! STOP BEING ANNOYING!"

    hide lucy

    "=== RECHEIO ==="

    john "The guys at school are so low, don't you think?"

    mike "Yeah! Scott and the others are so lame!"

    show lucy mad at right

    lucy "Mike! It's already midnight! Don't sleep late!"

    mike "FUCK OFF, MOM!!!"
    
    hide lucy

    "=== RECHEIO ==="

    john "BLABLABLA Mary and the other girls"

    mike "They are sluts, man!"

    "=== RECHEIO ==="

    mike "By the way, I'm going to my bed. See ya, man!"

    john "Bye!"

    show mike neutral at center

    mike "Geez! It's already 2am! Mom's gonna kill me!"

    mike "Why do everyone have to be so annoying? I just hate people!"

    mike "I wish life was like my favorite games."

    mike "I'd definitely be the best! And happy..."

    mike "....... ZZZzzzzzz"

    jump adventure_call


label adventure_call:

    mike "AUHSUHASHUHAUHSU"

    # $battle = "first"
    jump play_turnbased

    return
 
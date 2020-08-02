define audio.piano1 = "audio/Piano.wav"
define audio.piano2 = "audio/Piano2.wav"
define audio.lofi = "audio/LOFI.wav"


label sound_test:

    init python:
        renpy.music.register_channel("music_channel1", "music", True)
        renpy.music.register_channel("music_channel2", "music", True)


    play music piano1 loop

    "Música 1"

    play music [piano1, piano1, piano1, piano1,
                piano2] fadeout 1.0 fadein 1.0

    "Música 1x4 -> 2"

    stop music

    play music_channel1 lofi

    play music_channel2 piano2
    $renpy.music.set_volume(0, 0, 'music_channel2')

    "Canal 1 = Música 3 (1.0); Canal 2 = Música 2 (0.0)"

    $renpy.music.set_volume(1, 1, 'music_channel2')
    $renpy.music.set_volume(0, 1, 'music_channel1')

    "Canal 1 = Música 3 (0.0); Canal 2 = Música 2 (1.0)"

    $renpy.music.set_volume(0, 1, 'music_channel2')
    $renpy.music.set_volume(1, 1, 'music_channel1')

    "Canal 1 = Música 3 (1.0); Canal 2 = Música 2 (0.0)"

    return

label sound_test2:

    call play_procedural("test")

    "Procedural Music"

    return
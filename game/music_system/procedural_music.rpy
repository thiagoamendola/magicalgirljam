init python:

    music_list = {
        "test" : [
            ["audio/musics/test/a1.wav", "audio/musics/test/a2.wav"],#A
            ["audio/musics/test/b1.wav", "audio/musics/test/b2.wav"],#B
            ["audio/musics/test/c1.wav", "audio/musics/test/c2.wav"]#C
        ]
    }


label play_procedural(music_name = "test"):
    python:
        music_set = music_list[music_name]
        current_set = []
        for i in range(len(music_set)):
            piece_options = music_set[i]
            current_piece = piece_options[int(renpy.random.random() * len(piece_options))]
            current_set.append(current_piece)
        print current_set

        renpy.music.play(current_set, channel='music', loop=True, fadeout=1.0, synchro_start=False, fadein=1.0, tight=None, if_changed=False)


    return


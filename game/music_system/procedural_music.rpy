init python:

    current_music = None

    class ProceduralMusic:

        music_list = {
            "test" : [
                #A
                ["audio/musics/test/a1.wav", "audio/musics/test/a2.wav"],
                #B
                ["audio/musics/test/b1.wav", "audio/musics/test/b2.wav"],
                #C
                ["audio/musics/test/c1.wav", "audio/musics/test/c2.wav"]
            ],
            "test2" : [
                #A
                ["audio/musics/test2/a1.mp3", "audio/musics/test2/a2.mp3"],
                #B
                ["audio/musics/test2/b1.mp3", "audio/musics/test2/b2.mp3"],
            ],
            "musictest1" : [
                #A
                [
                "audio/musics/music1/a1.wav"
                ],
                #B
                [
                "audio/musics/music1/b2.wav"
                ],
                #C
                [
                "audio/musics/music1/c3.wav"
                ]
            ],
            "musictest2" : [
                [
                "audio/musics/Cupido-Tema.ogg"
                ]
            ],
            "music1" : [
                #A
                [
                "audio/musics/music1/a1.wav", 
                "audio/musics/music1/a2.wav", 
                "audio/musics/music1/a3.wav"
                ],
                #B
                [
                "audio/musics/music1/b1.wav", 
                "audio/musics/music1/b2.wav", 
                "audio/musics/music1/b3.wav"
                ],
                #C
                [
                "audio/musics/music1/c1.wav", 
                "audio/musics/music1/c2.wav", 
                "audio/musics/music1/c3.wav"
                ]
            ]
        }


        def initialize(self):
            renpy.music.stop(channel='music')
            renpy.music.set_queue_empty_callback(self.fill_queue, channel='music')
            return


        def stop(self):
            renpy.music.set_queue_empty_callback(None, channel='music')
            renpy.music.stop(channel='music')
            return


        def fill_queue(self):

            if current_music == None:
                self.stop()
                return

            renpy.random.Random()

            music_set = self.music_list[current_music]
            current_set = []
            for i in range(len(music_set)):
                piece_options = music_set[i]
                current_piece = piece_options[int(renpy.random.random() * len(piece_options))]
                current_set.append(current_piece)

            print current_set

            renpy.music.queue(current_set, channel='music', loop=False, clear_queue=True, fadein=1.0)

            return


        def empty_callback():
            return


    procedural_music = ProceduralMusic()


label play_procedural(music_name = "test"):
    python:
        current_music = music_name

        procedural_music.initialize()

    return



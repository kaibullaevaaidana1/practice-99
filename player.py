import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()

        self.tracks = []      
        self.current = 0      
        self.playing = False  
        for filename in sorted(os.listdir(music_folder)):
            if filename.endswith(".mp3") or filename.endswith(".wav"):
                full_path = os.path.join(music_folder, filename)
                self.tracks.append(full_path)

    def play(self):
        if not self.tracks:
            return  # если треков нет — ничего не делаем
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()
        self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_track(self):
        self.current = (self.current + 1) % len(self.tracks)
        self.play()

    def prev_track(self):
        self.current = (self.current - 1) % len(self.tracks)
        self.play()

    def get_info(self):
        if not self.tracks:
            return "Треков нет в папке music/"

        name = os.path.basename(self.tracks[self.current])

        if self.playing:
            status = "Playing"
        else:
            status = "Stopped"

        total = len(self.tracks)
        num = self.current + 1  

        return f"{status}  |  {name}  |  {num}/{total}"
import os
import pygame


class MusicPlayer:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        self.music_folder = os.path.join(base_dir, "music")

        self.playlist = [
            os.path.join(self.music_folder, file)
            for file in os.listdir(self.music_folder)
            if file.endswith(".wav")
        ]

        self.current_index = 0
        self.is_playing = False

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def previous_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def get_current_track_name(self):
        if self.playlist:
            return os.path.basename(self.playlist[self.current_index])
        return "No track"

    def get_position(self):
        pos = pygame.mixer.music.get_pos()
        if pos < 0:
            return 0
        return pos // 1000

    def get_track_length(self):
        if self.playlist:
            sound = pygame.mixer.Sound(self.playlist[self.current_index])
            return int(sound.get_length())
        return 0
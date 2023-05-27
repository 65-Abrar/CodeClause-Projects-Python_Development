#pip install pygame
#pip install pillow 
#install above libraries for creating an music player
import os
import pygame
import tkinter as tk
from tkinter import filedialog
import random

class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.playlist = []
        self.current_song_index = 0
        self.is_playing = False

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create GUI elements
        self.create_gui()

    def create_gui(self):
        # Configure the tkinter window background color
        self.window.configure(bg="#F0F0F0")

        # Create label for displaying song name with increased font size and color
        self.song_label = tk.Label(self.window, text="", font=("Arial", 16, "bold"), fg="#000000", bg="#F0F0F0")
        self.song_label.pack(pady=10)

        # Create buttons with initial font size
        self.btn_prev = tk.Button(self.window, text="<< Prev", command=self.play_previous_song, font=("Arial", 14), bg="#FFD700", fg="#000000")
        self.btn_play = tk.Button(self.window, text="Play", command=self.play_song, font=("Arial", 14), bg="#00FF00", fg="#000000")
        self.btn_pause = tk.Button(self.window, text="Pause", command=self.pause_song, font=("Arial", 14), bg="#FF4500", fg="#000000")
        self.btn_next = tk.Button(self.window, text="Next >>", command=self.play_next_song, font=("Arial", 14), bg="#4169E1", fg="#000000")
        self.btn_select_song = tk.Button(self.window, text="Select Song", command=self.add_song, font=("Arial", 14), bg="#FF69B4", fg="#000000")

        self.btn_prev.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_play.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_pause.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_next.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_select_song.pack(side=tk.LEFT, padx=10, pady=10)

    def add_song(self):
        song_paths = filedialog.askopenfilenames(title="Select Songs", filetypes=(("Audio Files", "*.mp3"),))
        if song_paths:
            self.playlist.extend(song_paths)

    def play_song(self):
        if not self.is_playing:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                if len(self.playlist) > 0:
                    song = self.playlist[self.current_song_index]
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    self.is_playing = True
                    self.update_song_label()  # Update the song label
                    self.update_background_color()  # Update the background color

    def pause_song(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False

    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def play_next_song(self):
        if len(self.playlist) > 0:
            self.stop_song()
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play_song()

    def play_previous_song(self):
        if len(self.playlist) > 0:
            self.stop_song()
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            self.play_song()

    def update_song_label(self):
        current_song = self.playlist[self.current_song_index]
        song_name = os.path.basename(current_song)
        self.song_label.config(text=song_name)

    def update_background_color(self):
        # Generate a random background color using RGB values
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"#{r:02x}{g:02x}{b:02x}"  # Convert RGB values to hexadecimal color code

        # Update the background color of the window
        self.window.configure(bg=color)

    def run(self):
        self.window.mainloop()

# Run the music player
player = MusicPlayer()
player.run()
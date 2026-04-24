import pygame
import os

BASE_DIR = os.path.dirname(__file__)
music_folder = os.path.join(BASE_DIR, "music")

playlist = [f for f in os.listdir(music_folder) if f.endswith(".wav")]

current_index = 0
is_playing = False


def load_track():
    track_path = os.path.join(music_folder, playlist[current_index])
    pygame.mixer.music.load(track_path)


def play():
    global is_playing
    load_track()
    pygame.mixer.music.play()
    is_playing = True


def stop():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False


def next_track():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play()


def prev_track():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play()


def draw_ui(screen, font):
    screen.fill((30, 30, 30))

    track_text = font.render(f"Track: {playlist[current_index]}", True, (255, 255, 255))
    screen.blit(track_text, (20, 50))

    status = "Playing" if is_playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (200, 200, 200))
    screen.blit(status_text, (20, 100))

    pos = pygame.mixer.music.get_pos() // 1000
    pos_text = font.render(f"Time: {pos} sec", True, (200, 200, 200))
    screen.blit(pos_text, (20, 150))

    controls = [
        "P - Play",
        "S - Stop",
        "N - Next",
        "B - Previous",
        "Q - Quit"
    ]

    for i, text in enumerate(controls):
        t = font.render(text, True, (180, 180, 180))
        screen.blit(t, (20, 220 + i * 30))
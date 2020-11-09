"""Music Flash Cards

This module creates the flashcards used to run the flashcard
app. It also runs the main loop, which will need to be exited by 
the user when they are ready to stop.
"""

import os
import random
import time
import tkinter as tk

from PIL import Image, ImageTk
from pyaudio_test import read_and_write_audio, get_pitch

from .cards import note_card_paths, incorrect_card_path, correct_card_path


def display_note_flashcard() -> None:
    """This function is much like the two below it, so this docstring and
    the comments can serve for those two as well. The reason for the other two functions
    is that this function pulls a random card from the file and, to prevent
    it from pulling the Correct or Incorrect cards, they have been put into
    a separate file."""

    root = tk.Tk()

    filename = random.choice(note_card_paths())
    note = os.path.splitext(filename)[0]

    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    canvas.create_image(50, 50, anchor="nw", image=photo)

    root.after(10_000, root.destroy)
    root.mainloop()

    return note


def display_correct_card() -> None:
    card = tk.Tk()

    img = Image.open(correct_card_path())

    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(card, width=400, height=400)
    canvas.pack()
    canvas.create_image(50, 50, anchor="nw", image=photo)

    card.after(5000, card.destroy)
    card.mainloop()


def display_incorrect_card() -> None:
    card = tk.Tk()

    img = Image.open(incorrect_card_path())

    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(card, width=400, height=400)
    canvas.pack()
    canvas.create_image(50, 50, anchor="nw", image=photo)

    card.after(5_000, card.destroy)
    card.mainloop()


def main():
    """Function that runs the main loop. This contains the
    audio functions as well. Audio is recorded and then the
    frequency of the audio is used to get the note name. That
    note name is then compared to the note name on the card and,
    if they are the same, the correct card will appear. If not,
    the incorrect card appears. Each of these events takes
    advantage of a delay to allow for time to record and time
    for the user to mentally process and find the note given on
    each card."""

    while True:

        expected_pitch = display_note_flashcard()
        time.sleep(5)

        sound = read_and_write_audio()

        played_pitch = get_pitch(sound)

        if played_pitch == expected_pitch:
            display_correct_card()
        else:
            display_incorrect_card()

        time.sleep(5)


if __name__ == "__main__":
    main()

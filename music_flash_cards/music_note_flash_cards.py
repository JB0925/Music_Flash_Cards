from pyaudio_test import read_and_write_audio, get_pitch
import tkinter as tk
from pil import Image, ImageTk
import random
import os
import time

"""This module creates the flashcards used to run the flashcard
app. It also runs the main loop, which will need to be exited by 
the user when they are ready to stop."""


def display_note_flashcard():
    """This function is much like the two below it, so this docstring and
    the comments can serve for those two as well. The reason for the other two functions
    is that this function pulls a random card from the file and, to prevent
    it from pulling the Correct or Incorrect cards, they have been put into
    a separate file."""

    root = tk.Tk()                  #create the main Tkinter widget
    folder = 'C:/Users/superuser/Music_Flash_Cards/chromatic_note_cards'
    filename = random.choice(os.listdir(folder))
    note = os.path.splitext(filename)[0]                #get the note name from the flash card
    
    img = Image.open(os.path.join(folder, filename))        #open the file with the image
    photo = ImageTk.PhotoImage(img)                         #load the image
    canvas = tk.Canvas(root, width=400, height=400)         #place it on a Tkinter Canvas object
    canvas.pack()
    canvas.create_image(50,50, anchor='nw', image=photo)
    
    root.after(10000, root.destroy)                         #stop the card from running after 10 seconds
    root.mainloop()

    return note


def display_correct_card():
    card = tk.Tk()

    folder = 'C:/Users/superuser/Music_Flash_Cards/correct_and_incorrect_cards'
    correct_card = 'Correct.PNG'
    
    img = Image.open(os.path.join(folder, correct_card))
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(card, width=400, height=400)
    canvas.pack()
    canvas.create_image(50,50, anchor='nw', image=photo)

    card.after(5000, card.destroy)
    card.mainloop()


def display_incorrect_card():
    card = tk.Tk()

    folder = 'C:/Users/superuser/Music_Flash_Cards/correct_and_incorrect_cards'
    incorrect_card = 'Incorrect.PNG'
    
    img = Image.open(os.path.join(folder, incorrect_card))
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(card, width=400, height=400)
    canvas.pack()
    canvas.create_image(50,50, anchor='nw', image=photo)

    card.after(5000, card.destroy)
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

    while True:                             #user will need to stop the program manually
        x = display_note_flashcard()        #show the flashcard
        time.sleep(5)                       #allow for time to process and find the note
        sound = read_and_write_audio()      #record audio
        p = get_pitch(sound)                #get the note name from the recorded sound
    
        if p == x:                          #if the value of the recorded sound is equal
            display_correct_card()          #to the name of the note on the card, display
            time.sleep(5)                   #the "Correct!" card. If not, display the
        else:                               #"Incorrect..." card.
            display_incorrect_card()
            time.sleep(5)


if __name__ == '__main__':
    main()



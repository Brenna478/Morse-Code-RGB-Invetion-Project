# Import necessary elements to use in future area of the code 
from pydub import AudioSegment
from pydub.playback import play
import time
import RPi.GPIO as GPIO

# Load the audio files for short and long beeps
beep = AudioSegment.from_mp3("morseshort.mp3")
beeeep = AudioSegment.from_mp3("morselong.mp3")

# Setup GPIO pins for RGB light
GPIO.setmode(GPIO.BCM) #this is sets up for the ability to determine which pin needs to recieve putputs
GPIO.setwarnings(False)
GPIO.setup(19, GPIO.OUT)  # Blue LED pin, sets up to the LED to be able turn on
GPIO.setup(21, GPIO.OUT)  # Green LED pin, sets up to the LED to be able turn on

# Define the light sequence, organizes the code into one phrase that can be used to run all of the code inside this def
def light_blue():
    GPIO.output(19, GPIO.HIGH)  # Turn on blue light
    time.sleep(0.2)  # Short duration for morse code dot
    GPIO.output(19, GPIO.LOW)  # Turn off blue light

def light_green():
    GPIO.output(21, GPIO.HIGH)  # Turn on green light
    time.sleep(0.6)  # Slightly longer duration for morse code dash
    GPIO.output(21, GPIO.LOW)  # Turn off green light

# Define the morse code, each letter has a specific sequence of dashes and dots which need to be assigned to that letter 
morse_code = {
    "A": '.-',
    "B": '-...',
    "C": '-.-.',
    "D": '-..',
    "E": '.',
    "F": '..-.',
    "G": '--.',
    "H": '....',
    "I": '..',
    "J": '.---',
    "K": '-.-',
    "L": '.-..',
    "M": '--',
    "N": '-.',
    "O": '---',
    "P": '.--.',
    "Q": '--.-',
    "R": '.-.',
    "S": '...',
    "T": '-',
    "U": '..-',
    "V": '...-',
    "W": '.--',
    "X": '-..-',
    "Y": '-.--',
    "Z": '--..',
}

# Define the phrase, this is the phrase that is translated into morse code
phrase = "EPIC"

# Translate the phrase into morse code and play the corresponding sounds
for char in phrase: #char means character, so for each character in the defined phrase it will translate into morse code
    if char.upper() in morse_code:  # If the character(set uppercase) has a assigned morse code do the following: 
        morse = morse_code[char.upper()]
        print(f"Morse code for {char}: {morse}")
        
        for symbol in morse:
            if symbol == ".":
                light_blue()  # Blue for dot
                play(beep)  # Short beep for dot
                time.sleep(0.2)  # Pause between sounds (duration of one dot)
                
            elif symbol == "-":
                light_green()  # Green for dash
                play(beeeep)  # Long beep for dash
                time.sleep(0.6)  # Pause between sounds (duration of one dash)
                
                
        
        time.sleep(0.5)  # Pause between characters

    elif char == " ":  # Pause between words
        print("Space detected, pausing between words.")
        time.sleep(1)  # Pause between words
        

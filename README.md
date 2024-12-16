
### Morse-Code-RGB
Houses all documentation for Morse Code RGB Pi Invention 


## Description: 
Morse code is one of the oldest transmission systems but it is not very accessible to those who listen to the sounds. However, if there is a visual component it not only could be accessible but it could also be a great teaching tool for those who want to learn morse code visually. 

This can be executed via a wired speaker and RGB LED bulb connected to the RaspberryPi. The audio needs to be imported by pydub to be used through the speaker and then executed by pydub.playback. For the lights, it is necessary to import time in order to showcase the length of the sound. The light is connected via male-to-male cables and a voltage resistor and is coded in a specific RBG code for the light to turn that color when enabled. The code has a specific phrase that it translates into Morse code and also visualizes the beeps with the LED. 

## Physical Requirements:
A RaspberryPi (4)
A breadboard with a ribbon cable and T-Cobbler 
5 male to male wires
2 330 Ω (at least) resistor
An RGB LED
A wired speaker
Ability to open the code on the Raspberry pi

## Wiring 
1. Gather 5 male-to-male wires, 2 330 resistors, the RGB LED, and a wired speaker. 
1.5 Make sure the pi is unplugged to start wiring.
2. Take the wires and use the RGB wiring visual aid to choose which colors you want to use for your Morse code identifiers. ![RGB Wiring](https://github.com/user-attachments/assets/5d4a0402-9fd7-41a4-bb7b-1d24700191e8)

3. Use the resistors on the prongs of the colors chosen, one side must not connect to any other prong or wire while the other must be inserted next to the color prong.
4. Use the male-to-male wire to connect the side that is 'NOT' next to a prong and to a numbered pin on the T-cobbler, repeat for the second color.
5. Next take the remaining wires and connect the prong labeled "ground" to the ground (GRD) pin on the T-cobbler.
6. Once finished it should look something similar to this. ![20241213_105649](https://github.com/user-attachments/assets/2a9bec96-de37-4e90-9c5d-5988e89f189f)

## Running the Code
1. To be able to run the code it is necessary to create a virtual environment so that the code does not error. 
2. This series of inputs can be used to create a virtual environment,
[APznzaYV1Eg-qorfcT8esIDBkbimuYF6GxgPMWUgFwReoFxeJizgBc7XIDEMmlzCfpGnNZtfJSjtBzCMFlfiD_Ad5zATgrRr2yWYy65lnQB93ypm2kZnb8wBmplwrLFQFVAU5ooet-CTAp7Sr2vzVfiNTGjzX3qoHSA6vDm6qUbl_-1Ji_AapmAIUtqU7BGcSPB2fco0ZjUqfpmmtDOjri.pdf](https://github.com/user-attachments/files/18156296/APznzaYV1Eg-qorfcT8esIDBkbimuYF6GxgPMWUgFwReoFxeJizgBc7XIDEMmlzCfpGnNZtfJSjtBzCMFlfiD_Ad5zATgrRr2yWYy65lnQB93ypm2kZnb8wBmplwrLFQFVAU5ooet-CTAp7Sr2vzVfiNTGjzX3qoHSA6vDm6qUbl_-1Ji_AapmAIUtqU7BGcSPB2fco0ZjUqfpmmtDOjri.pdf)
3. Next cd (change directory) to the file, in terminal, named Morse code so that all audio files and files can be used in the program. To cd type "cd morse..." and then tab to have the terminal autofill the rest.
4. Now you must import and download the files necessary, in this case pydub and time and RPi.GPIO.
5. Now you should be ready to run the program within the terminal, to run it type "python3 morse_rgb.py" and it should run the audio through the speaker and the light should work.


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
5. Next take the remaining wires and connect the prong labeled "ground" to the ground (GRD) pin on the T-cobbler 
6. Once finished it should look something similar to this![20241213_105649](https://github.com/user-attachments/assets/2a9bec96-de37-4e90-9c5d-5988e89f189f)



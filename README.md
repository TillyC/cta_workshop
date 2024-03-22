# cta_workshop

## Mending Musically 

How to make electronic sensors from scratch using textiles. The goal is for everyone to leave the workshop with a functioning touch sensor that makes a sound.

## Tools
### Textiles
 - Conductive yarn
 - A needle
 - Scrap Fabric
### Electronics
 - Raspberry Pi
 - 2 x crocodile clips
 - 2 x wires
 - breadboard

## Resources
How to videos:
This tutorial is what I used to understand how to play sounds on the raspberry pi ...

https://projects.raspberrypi.org/en/projects/gpio-music-box/4

This was the inspiration for how to make the sensor ...

https://etextile-summercamp.org/swatch-exchange/darned-and-mended/

projects as inspiration:
- https://www.kthartic.com/index.php/wearables/urban-armor-10/)https://www.kthartic.com/index.php/wearables/urban-armor-10/
- https://www.kobakant.at/DIY/?p=3175
- https://www.dezeen.com/2014/06/20/yen-chen-chang-knitted-sensors-rca-show-2014/

## Step by Step
### Intro
I want this workshop to be an introduction to electronic textiles so that you can understand the way it could be applied to a creative brief. I also hope you have fun. 

### Making the Sensor
- Select your square of scrap fabric.
- Thread your needle with conudctive yarn.
- Make a securing stitch, this will act as your positive power connection.
https://www.youtube.com/watch?v=f58woIqfz3o
- Loosely stitch a condensed patch of threads, this will be your pressure activation point.
- Make a second securing stitch, this will act as your negative power connection.
- Set aside until it's time to test - ideally at this point you would use a multimeter to test the resistance but we don't currently have access to one.

### Make the circuit 
Before we plug the Pi in we are going to set up the circuit. This is a simple set up. 
- Connect a different colour crocodile clip to each end of the sensor (these will be yout power and ground connections).
- Attach a correspondng wire to the other end of the crocodile clips.
- One of those wires will connect to your power/data and the other to ground.
- Turn on the Pi.
  
![image](https://github.com/TillyC/cta_workshop/assets/52659157/8d35d90b-6cf4-41fa-91bb-ffa83101230f)
![image](https://github.com/TillyC/cta_workshop/assets/52659157/4b47f7d3-ec3f-407e-98ef-1a3bb63f7d33)

## Set up the Pi (SSH)
To get audio to play from the raspberry pi, we need to make sure to select the correct output. The Pi defaults to the headphone jack but since we have USB speakers we need to go into the settings to change that. 
- plug in a speaker to the usb port (we don't have 18 speakers so you will need to share).
- Open your terminal.
- SSH into your raspberry Pi.
```
  ssh {name}@{IP}
```
- In the terminal type sudo raspi-config.
```
sudo raspi-config
```
- This will open a settings window, press enter to select the first option labelled system options.
![image](https://github.com/TillyC/cta_workshop/assets/52659157/b796fe37-78dd-4405-8398-768901448535)
- Then use the down arrow and press enter to select audio.
![image](https://github.com/TillyC/cta_workshop/assets/52659157/50455d29-c615-4bfe-adb6-b35e70e2c689)
- Use the down arrow and press enter to choose the USB device from the audio options.
- Right arrow and enter to select ok.
- Left arrow and enter to select finish to return to your terminal window.

Lets get everyone into the correct folder.
- Clone this repo onto your Pi.
```
  git clone {URL}
```
- CD into this workshop folder
```
cd cta_workshop
```
### Edit and run the code
- You will need to update the file path and name of the sound file in sensor_code.py.
```
nano sensor_code.py
```
- When the change has been made you need to save the changes and return to the terminal. Ctrl X / Y / enter .
- Run the code
```
python sensor_code.py
```
- You should now be able to hear a sound play from your speaker when you apply pressure to the sensor.

### Customise 
Play around with the code and circuit to see how you can develop this. What happens if you add an LED to the circuit? What if you want the sound to only play once or if you want to add more sensors?

## Set up the Pi (VNC)
To get audio to play from the raspberry pi, we need to make sure to select the correct output. The Pi defaults to the headphone jack but since we have USB speakers we need to go into the settings to change that. 
- plug in a speaker to the usb port (we don't have 18 speakers so you will need to share).
- Open your terminal.
- In the terminal type sudo raspi-config.
```
sudo raspi-config
```
- This will open a settings window, press enter to select the first option labelled system options.
![image](https://github.com/TillyC/cta_workshop/assets/52659157/b796fe37-78dd-4405-8398-768901448535)
- Then use the down arrow and press enter to select audio.
![image](https://github.com/TillyC/cta_workshop/assets/52659157/50455d29-c615-4bfe-adb6-b35e70e2c689)
- Use the down arrow and press enter to choose the USB device from the audio options.
- Right arrow and enter to select ok.
- Left arrow and enter to select finish to return to your terminal window.

Lets get set up a folder. 
- Make a new folder for this workshop in your home directory. This can be done via the terminal or in your file explorer.
```
  cd home
  mkdir cta_workshop
```
- CD into this workshop folder.
```
cd cta_workshop
```
- Download a .wav sound into that folder, I just did it directly on the Pi via the internet explorer.
  
### Write and run the code
- Make a new text file called sensor_code.py.
```
touch sensor_code.py 
```
- Write out the code from the corresponding file in this repo. The code is available to copy and paste under sensor_code.py . I have left comments that explain each part.
- Edit the file path and name of the .wav file as needed. 
- Run the code.
```
python sensor_code.py
```
- You should now be able to hear a sound play from your speaker when you apply pressure to the sensor. 

### Customise 
Play around with the code and circuit to see how you can develop this. What happens if you add an LED to the circuit? What if you want the sound to only play once or if you want to add more sensors?

# Imports go at the top

from microbit import *
import radio

radio.on()
radio.config(group=1)  # Set the radio group

while True:
    radio.send("ping")  # Send a ping message
    
    # Beating heart animation
    display.show(Image.HEART_SMALL)
    sleep(300)  # Small heart visible
    display.show(Image.HEART)
    sleep(300)  # Large heart visible

    sleep(1000)  # Wait 1 second before sending again

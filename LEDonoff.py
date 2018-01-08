import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program

IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setup(40,IO.OUT)             # initialize digital pin40 as an output.
IO.output(40,1)
print ("LED ON \n")               # turn the LED on (making the voltage level HIGH)
time.sleep(5)                         # sleep for a second
IO.cleanup()
print ("LED OFF \n")            # turn the LED off (making all the output pins LOW)
time.sleep(5)                        #sleep for a second    


#!/usr/bin/env python
import RPi.GPIO as GPIO


#Warings and Mode

GPIO.setwarnings(False) #Turn off warnings
GPIO.setmode(GPIO.BOARD) #Board Mode vs GPIO.BCM

#Setups
GPIO.setup(37, GPIO.OUT) #Example 1 Output
GPIO.setup(40, GPIO.IN) #Example 2 Input


#Starts
GPIO.output(37, GPIO.LOW) #Example 1, Setting this Pin to LOW for start
GPIO.output(40, GPIO.HIGH)


#Functions
def end():
    GPIO.cleanup()   #Example Function, also needed at the end as clean up



#Strings

food = 1 #Example

#Code Start

print("Hello World") #Example 1
print(food) #Example 2


#End
end() #GPIO Cleanup

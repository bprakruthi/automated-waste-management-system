import RPi.GPIO as GPIO
import time


# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
LED_ON = 15
 
# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
 
def main():
    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
    LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
 
  # Main program block
 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
  # Initialise display
    lcd_init()
    
  # Toggle backlight on-off-on
    lcd_backlight(True)
    time.sleep(0.2)
    lcd_backlight(False)
    time.sleep(0.5)
    lcd_backlight(True)
    time.sleep(0.5)
    
   
    while True:
 
    # Send some centred test
        #lcd_string("raspberry pi",LCD_LINE_1,2)
        #lcd_string("raspberry pi",LCD_LINE_2,2)
        #lcd_string("raspberry pi",LCD_LINE_3,2)
        #lcd_string("raspberry pi",LCD_LINE_4,2)
        lcd_string("Project PRANJALA-2018",2)
        lcd_byte(LCD_LINE_1,LCD_CMD)
        time.sleep(3)
        lcd_byte(LCD_LINE_2,LCD_CMD)
        #lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd_string("bin status : active",2)
        time.sleep(3)
        
        lcd_byte(LCD_LINE_3,LCD_CMD)
        lcd_string("bin location : r.v.road",2)
        time.sleep(3)
        
        lcd_byte(LCD_LINE_4,LCD_CMD)
        lcd_string("bin load : 3.14kg",2)
        time.sleep(3)
         
        
 
    time.sleep(3) # 3 second delay
 
    
def lcd_init():
     
    GPIO.setwarnings(False)
  
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7
    GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable
 
  # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
    GPIO.setmode(GPIO.BCM)
    GPIO.output(LCD_RS, mode)
    
    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
    LCD_LINE_4 = 0xD4# RS
 
  # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
    lcd_toggle_enable()
 
  # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
    lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)
 
def lcd_string(message,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified
   
    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
    LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
 
    GPIO.setmode(GPIO.BCM)
    if style==1:
        message = message.ljust(LCD_WIDTH," ")
    elif style==2:
        message = message.center(LCD_WIDTH," ")
    elif style==3:
        message = message.rjust(LCD_WIDTH," ")
 
    #lcd_byte(line, LCD_CMD)
        lcd_byte(LCD_LINE_1,LCD_CMD)
        #lcd_string("PROJECT PRANJALA-2018",2)
        #time.sleep(3)
        lcd_byte(LCD_LINE_2,LCD_CMD)
        #lcd_string("bin status : active",2)
        #time.sleep(3)
        lcd_byte(LCD_LINE_3,LCD_CMD)
        lcd_byte(LCD_LINE_4,LCD_CMD)
        
        
 
 
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_backlight(flag):
  # Toggle backlight on-off-on
    GPIO.output(LED_ON, flag)
 
if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!",2)
        GPIO.cleanup()

import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import os

class display(object):
    """ hueBerry Display API v0.1 """
    # My first class ever! yay!
    # This is a bundle of shit, but it's my bundle of shit
    # Will work to integrate this into hueberry.py soon
    # For now, this is just a proof of concept
    
    def __init__(self,console=0,mirror = 0):
        self.console = console
        self.mirror = mirror
        if (self.console == 0 or self.mirror == 1):
            self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)
            self.disp.begin()
            self.width = self.disp.width
            self.height = self.disp.height
            self.image = Image.new('1', (self.width, self.height))
            self.font = ImageFont.load_default()
            self.draw = ImageDraw.Draw(self.image)
        else:
            #console specific initiation goes here
            #Adafruit OLED library standard width for string calculation
            self.width = 128
        self.time_format = True
        
    def display_time(self):
        # Collect current time and date
        if(self.time_format):
            current_time = time.strftime("%-I:%M")
        else:
            current_time = time.strftime("%-H:%M")
        current_date = time.strftime("%m / %d / %Y")
        #Get 24 hour time variable
        H = int(time.strftime("%H"))
        if (self.console == 1 or self.mirror == 1):
            os.system('clear')
            print("Currently on Time screen")
            print("------------------------")
            print("")
            print("        "+str(current_time))
            print("")
            print("------------------------\n\n")
            if (self.mirror == 0):
                return
        # Set font type and size
        if H >= 21 or H < 6:
            font = ImageFont.truetype('BMW_outline.otf', 40)
            #print("outline")
        else:
            font = ImageFont.truetype('BMW_naa.ttf', 45)
            #font = ImageFont.truetype('BMW_outline.otf', 40)
            #print("regular")
        #print H
        #time.sleep(100)
        # Position time
        x_pos = (self.width/2)-(self.string_width(font,current_time)/2)
        y_pos = 2 + (self.disp.height-4-8)/2 - (35/2)
        # Clear image buffer by drawing a black filled box
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        # Draw time
        self.draw.text((x_pos, y_pos), current_time, font=font, fill=255)
        # Set font type and size
        font = ImageFont.truetype('BMW_naa.ttf', 13)
        #font = ImageFont.load_default()
        # Position date
        x_pos = (self.width/2)-(self.string_width(font,current_date)/2)
        y_pos = self.disp.height-10
        # Draw date during daytime hours
        if H < 21 and H > 6:
            self.draw.text((x_pos, y_pos), current_date, font=font, fill=255)
        # Draw the image buffer
        self.disp.image(self.image)
        self.disp.display()

    def display_2lines(self,line1,line2,size):
        if(self.time_format):
            current_time = time.strftime("%-I:%M")
        else:
            current_time = time.strftime("%-H:%M")
        current_date = time.strftime("%m / %d / %Y")
        if (self.console == 0 or self.mirror == 1):
            font = ImageFont.truetype('BMW_naa.ttf', 11)
            #font = ImageFont.load_default()
            #draw a clock
            # Position time
            x_pos = (self.width/2)-(self.string_width(font,current_time)/2)
            y_pos = 0
            # Clear image buffer by drawing a black filled box
            self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
            # Draw time
            self.draw.text((x_pos, y_pos), current_time, font=font, fill=255)
            #draw a menu line
            timeheight = 10
            self.draw.line((0, timeheight, self.width, timeheight), fill=255)
            # Set font type and size
            font = ImageFont.truetype('BMW_naa.ttf', size)
            x_pos = (self.width/2)-(self.string_width(font,line1)/2)
            y_pos = 8 + (self.disp.height-4-8)/2 - (35/2)
            self.draw.text((x_pos, y_pos), line1, font=font, fill=255)
            x_pos = (self.width/2)-(self.string_width(font,line2)/2)
            y_pos = self.disp.height-26
            self.draw.text((x_pos, y_pos), line2, font=font, fill=255)
            self.disp.image(self.image)
            self.disp.display()
        elif (self.console == 1 or self.mirror == 1):
            os.system('clear')
            print("----------------------------")
            print("Currently Displaying 2 lines")
            print(current_time)
            print("----------------------------")
            print(line1)
            print(line2)
            print("----------------------------")
            return
            
    def display_3lines(self,line1,line2,line3,size,offset):
        if(self.time_format):
            current_time = time.strftime("%-I:%M")
        else:
            current_time = time.strftime("%-H:%M")
        current_date = time.strftime("%m / %d / %Y")
        if (self.console == 0 or self.mirror == 1):
            # Clear image buffer by drawing a black filled box
            self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
            font = ImageFont.truetype('BMW_naa.ttf', 11)
            #font = ImageFont.load_default()
            #draw a clock
            # Position time
            x_pos = (self.width/2)-(self.string_width(font,current_time)/2)
            y_pos = 0
            # Draw time
            self.draw.text((x_pos, y_pos), current_time, font=font, fill=255)
            #draw a menu line
            timeheight = 10
            self.draw.line((0, timeheight, self.width, timeheight), fill=255)
            # Set font type and size
            font = ImageFont.truetype('BMW_naa.ttf', size)
            x_pos = (self.width/2)-(self.string_width(font,line1)/2)
            y_pos = 8 + (self.disp.height-4-8)/2 - (35/2)
            self.draw.text((x_pos, y_pos), line1, font=font, fill=255)
            x_pos = (self.width/2)-(self.string_width(font,line2)/2)
            y_pos += offset
            self.draw.text((x_pos, y_pos), line2, font=font, fill=255)
            x_pos = (self.width/2)-(self.string_width(font,line3)/2)
            y_pos += offset
            self.draw.text((x_pos, y_pos), line3, font=font, fill=255)
            self.disp.image(self.image)
            self.disp.display()
        elif (self.console == 1 or self.mirror == 1):
            os.system('clear')
            print("----------------------------")
            print("Currently Displaying 3 lines")
            print(current_time)
            print("----------------------------")
            print(line1)
            print(line2)
            print(line3)
            print("----------------------------")
            return

    def display_custom(self,text):
        if (self.console == 0 or self.mirror == 1):
            # Clear image buffer by drawing a black filled box
            self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
            # Set font type and size
            #font = ImageFont.truetype('FreeMono.ttf', 8)
            font = ImageFont.load_default()
            # Position SSID
            x_pos = (self.width/2) - (self.string_width(font,text)/2)
            y_pos = (self.height/2) - (8/2)
            # Draw SSID
            self.draw.text((x_pos, y_pos), text, font=font, fill=255)
            # Draw the image buffer
            self.disp.image(self.image)
            self.disp.display()
        elif (self.console == 1 or self.mirror == 1):
            os.system('clear')
            print("----------------------------")
            print("custom text")
            print(text)
            print("----------------------------")
            return

    def string_width(self,fontType,string):
        string_width = 0
        for i, c in enumerate(string):
            char_width, char_height = self.draw.textsize(c, font=fontType)
            string_width += char_width
        return string_width
        
    def IntelliDraw(self,drawer,text,font,containerWidth):
        # Modified and stolen from https://mail.python.org/pipermail/image-sig/2004-December/003064.html
        # I'm not using it yet but this is some good inspiration
        words = text.split()  
        lines = [] # prepare a return argument
        lines.append(words) 
        finished = False
        line = 0
        while not finished:
            thistext = lines[line]
            newline = []
            innerFinished = False
            while not innerFinished:
                #print 'thistext: '+str(thistext)
                if drawer.textsize(' '.join(thistext),font)[0] > containerWidth:
                    # this is the heart of the algorithm: we pop words off the current
                    # sentence until the width is ok, then in the next outer loop
                    # we move on to the next sentence. 
                    newline.insert(0,thistext.pop(-1))
                else:
                    innerFinished = True
            if len(newline) > 0:
                lines.append(newline)
                line = line + 1
            else:
                finished = True
        tmp = []        
        for i in lines:
            tmp.append( ' '.join(i) )
        lines = tmp
        (width,height) = drawer.textsize(lines[0],font)            
        total_height = len(lines)*(height+1)
        return (lines,width,height,total_height)

    def InteliDraw_Test(self):
        global pos
        pos = 0
        text = 'One very extremely long string that cannot possibly fit \
        into a small number of pixels of horizontal width, and the idea \
        is to break this text up into multiple lines that can be placed like \
        a paragraph into our image'
        #draw = ImageDraw.Draw(OurImagePreviouslyDefined)
        #font = fontpath = ImageFont.truetype('/usr/local/share/fonts/ttf/times.ttf',26)
        #pixelWidth = 500 # pixels
        lines,tmp,h,total_h = IntelliDraw(self.draw,text,self.font,self.width)
        j = 0
        #for i in lines:
        #    draw.text( (0,0+j*h), i , font=font, fill=255)
        #    j = j + 1
        #self.disp.image(self.image)
        #self.disp.display()
        #time.sleep(5)
        #draw.rectangle((0,0,width,height), outline=0, fill=0)
        while(not GPIO.input(21)):  
            time.sleep(0.01)
        time.sleep(0.5)
        while GPIO.input(21):
            self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
            offset = ((h/2)*-1)*pos
            j = 0 
            for i in lines:
                #Line Centering code
                x_pos = (self.width/2) - (self.string_width(self.font,i)/2)
                self.draw.text( (x_pos,offset+(j*h)), i , font=self.font, fill=255)
                j = j + 1
            self.disp.image(self.image)
            self.disp.display()
            time.sleep(0.01)
        time.sleep(1)

import curses
class control(object):
    def __init__(self):
        # get the curses screen window
        self.screen = curses.initscr()
        # turn off input echoing
        curses.noecho()
        # respond to keys immediately (don't wait for enter)
        curses.cbreak()
        # map arrow keys to special values
        self.screen.keypad(True)
    def get_key(self):
        char = self.screen.getch()
        if char == ord('q'):
            #break
            return "q"
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            #screen.addstr(0, 0, 'right')
            return "right"
        elif char == curses.KEY_LEFT:
            #screen.addstr(0, 0, 'left ')  
            return "left"
        elif char == curses.KEY_UP:
            #screen.addstr(0, 0, 'up   ') 
            return "up"
        elif char == curses.KEY_DOWN:
            #screen.addstr(0, 0, 'down ')
            return "down"

        
if __name__ == "__main__":
    import time
    import hueberry_api
    test = hueberry_api.display()
    test.display_time()
    time.sleep(1)
    test.display_custom("holy shit")
    time.sleep(1)
    test.display_2lines("omg","it's working",17)
    time.sleep(1)
    test.display_3lines("for real","it's working","praise cheese",13,15)
    
    
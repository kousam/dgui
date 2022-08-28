
import random

class DColor():

    def randomPastel():
        MAX_VALUE = 220
        MIN_VALUE = 100
           
        rgb = [0,0,0]
        
        options = [0,1,2]
        
        main = options.pop(random.randint(0,2))
        varied = options.pop(random.randint(0,1))
        skip = options.pop()
        
        rgb[main] = MAX_VALUE
        rgb[varied] = random.randint(MIN_VALUE, MAX_VALUE)
        rgb[skip] = MIN_VALUE
        
        return (rgb[0], rgb[1], rgb[2])
    
    def toHex(rgb):
        r, g, b = rgb
        return '#{}{}{}'.format(str(hex(r)).lstrip('0x'),str(hex(g)).lstrip('0x'),str(hex(b)).lstrip('0x'))
    
        
    def randomPastelHex():
        return DColor.toHex(DColor.randomPastel())
    
    
    def colorsForButton(color):
        r,g,b = color
        
        offset = 35
        
        hover = (r + offset, g + offset, b + offset)
        pressed = (r - offset, g - offset, b - offset)
        
        return [color, hover, pressed]


    


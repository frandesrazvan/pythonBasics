from PIL import Image

'''
mac = Image.open('example.jpg')

# mac.show() 
# print(mac.size) # (1993, 1257) width, hight
# print(mac.filename) # example.jpg
# print(mac.format_description) # JPEG (ISO 10918)

# CROPPING IMAGES
print(mac.size) # (1993, 1257)

halfway = 1993 / 2
x = halfway - 200
y = 800
w = halfway + 200
h = 1257
mac.crop((x, y, w, h)).show()
computer = mac.crop((x, y, w, h))
mac.paste(im = computer, box = (0,0)) # copy to top-left corner | permanently affectiv the variable(spamming paste)
mac.show()
mac.resize((3000, 500)).show()
mac.rotate(90).show()

pencils = Image.open('pencils.jpg')
print(pencils.size) # (1950, 1300)

x = 0
y = 0
w = 1950 / 3
h = 1300 / 10

pencils.crop((x, y, w, h)).show()

x = 0
y = 1100
w = 1950 / 3
h = 1300

pencils.crop((x, y, w, h)).show()
'''

# Color Transparency
# RGBA - Red, Green, Blue, Alpha

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

blue.putalpha(128) # can't show :(
red.putalpha(128)

blue.paste(im = red, box = (0, 0), mask = red)
blue.show()
# blue.save('vanta-black.png')
# vanta_black = Image.open('vanta-black.png')
# vanta_black.show()
# Two images: word_matrix.png / mask.png
# The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it
# Your task is to use the mask.png image to reveal the hidden message inside wthe word_matrix.png

from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print(matrix.size) # (1015, 559)
print(mask.size) # (505, 251)

big_mask = mask.resize((1015, 559))
big_mask.putalpha(50)

matrix.paste(im=big_mask, box = (0, 0), mask=big_mask)
matrix.show()

# Answer is: GREAT WORK WITH IMAGES YOU ARE THE BEST
from PIL import Image
import os
img = Image.open(os.path.join(os.getcwd(), "assets/boards/board1.png"))
img.resize((640, 480), Image.ANTIALIAS).save("board1.png")

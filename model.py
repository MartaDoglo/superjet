import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw
import os


def changed_pic(filename):
    while True:
        file = 'uploads/' + filename
        if os.path.isfile(file):
            source_img = Image.open(file)
            figure, ax = plt.subplots()

            rect = patches.Rectangle((5, 5), 100, 100, linewidth=1, edgecolor='r', facecolor='none')
            ax.imshow(source_img)
            ax.add_patch(rect)
            plt.savefig('pictures/' + filename)
            break

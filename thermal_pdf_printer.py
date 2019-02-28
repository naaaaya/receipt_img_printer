#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
print('drag the file you wanna print here.')
image_path = input().strip()
format = image_path.split('.')[-1]
if format == 'pdf':
    images = convert_from_path(image_path)
    img = images[0].convert("RGBA")
elif [format == 'jpeg'] or [format == 'jpg'] or [format == 'png']:
    img = PIL.Image.open(image_path).convert("RGBA")
img.load()
background = PIL.Image.new("RGB", img.size, (255, 255, 255))
background.paste(img, mask=img.split()[3])
background.save("out.jpg","JPEG",quality=95)
currentWidth = background.width
currentHeight = background.height
ratio = currentHeight/currentWidth
width=384
height = int(width*ratio)
img = background.resize((width,height))
img.save('receipt_resized.jpg')


from escpos.printer import Usb

p = Usb(0x0416, 0x5011, out_ep=3)
p.image('receipt_resized.jpg')
p.text('\n\n\n\n\n\n')

#!/usr/bin/env python

#
# This python helper script does blend 2 images together and produces
# a by KSplashX usuable PNG animation file.
#
# Use:
# blend.py img1.png img2.png output.png
#

from __future__ import division
import sys, os, getopt, Image, ImageFile, ImageEnhance


def fadeon(srcfile1,destfile):
  srcimg1 = Image.open(srcfile1)

  (width1,height1) = srcimg1.size

  destimg = Image.new( "RGBA", (width1*10,height1*3))
  filt = 0
  img = srcimg1
  for row in range(1,4):
    for col in range(1,11):
      x = width1 * col - width1
      y = height1 * row - height1
      img2 = (ImageEnhance.Brightness(img)).enhance(filt)
      destimg.paste(img2,(x,y))
      filt = filt + (1/30)
  destimg.save(destfile)

def pasteanother(srcfile,destfile):
  srcimg = Image.open(srcfile)
  (width1,height1) = srcimg.size
  destimg = Image.open(destfile)
  for row in range(1,4):
    for col in range(1,11):
      x = width1 * col - width1
      y = height1 * row - height1
      destimg.paste(srcimg,(x,y),srcimg)
  destimg.save(destfile)  

def merge(srcfile, destfile, newfile):
  srcimg = Image.open(srcfile)
  (width1,height1) = srcimg.size
  destimg = Image.open(destfile)
  newimg = Image.new( "RGBA", (width1,height1))
  newimg.paste(srcimg,(0,0),srcimg)
  newimg.paste(destimg,(0,0),destimg)
  newimg.save(newfile)


if __name__ == "__main__":
  #if len(sys.argv) != 3: 
  #  print 'Usage: %s' % (sys.argv[0])
  #  sys.exit(1) 
  for i in range(1,6):
    currentimg = "{0}.png".format(i)
    newimg = "Anim{0}.png".format(i)
    fadeon(currentimg,newimg)
    if i >= 2:
      prevmerge= "{0}-combine.png".format(i-1)
      mergeimg = "{0}-combine.png".format(i)
      merge(prevmerge,currentimg,mergeimg)
      pasteanother(prevmerge,newimg)
    print "{0}.png".format(i)
   
    

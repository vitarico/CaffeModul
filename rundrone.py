#!/usr/bin/env python

# Copyright (c) 2011 Bastian Venthur
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Demo app for the AR.Drone.
This simple application allows to control the drone and see the drone's video
stream.
"""

import ps_drone
import cv2
import example as validation
import time


def main():
   drone = ps_drone.Drone()
   drone.reset()


   while (True):
       cap = drone.VideoImage

       cv2.imshow('Live Drone Cam', cap)
           
       number=validation.classify("test/snapshot_iter_21120.caffemodel", "test/deploy.prototxt", cap, 
        "test/mean.binaryproto", "test/labels.txt")
        
       print number 
            
       time.sleep(0.5)           

       if cv2.waitKey(1) & 0xFF == ord('q'):
           exit()     
            
if __name__ == '__main__':
    
   main()
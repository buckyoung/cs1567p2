#!/usr/bin/env python
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import *
from cs1567p2.msg import *

#TAPE   = [240, 243, 244]
RED    = [148, 126, 229] # Not bad
#GREEN  = [212, 241, 219] # Bad -- walls and oranges and whites
BLUE   = [224, 174, 139] # Not bad -- lost on k2 sometimes
ORANGE = [156, 201, 243] 
#BROWN  = [142, 179, 211] # Not terrible -- steals some red
#BLACK  = [112, 99, 97]
#YELLOW = [165, 251, 253] # Not bad -- NEON ORANGE POST IT!, also yellow and some orange
#WHITE  = [255, 255, 255] #Really good, except computer tops
color_mask_list = [BLUE, RED, ORANGE, GREEN]
threshold = 33
locpub = None
kinect1pub = None
kinect2pub = None
kinect3pub = None
top_mask = Image()
mid_mask = Image()

def _1_image_callback(message):
    global color_mask_list
    global top_mask
    global threshold
    global kinect1pub
    #make a new image if you want to view your mask
    top_mask = Image()
    top_mask.height = message.height
    top_mask.width = message.width
    top_mask.encoding = message.encoding
    top_mask.is_bigendian = message.is_bigendian
    top_mask.step = message.step
    if message.encoding == "bgr8": #this is image_color encoding
        byte_array = list(message.data) #convert unit8[] from string to chars
        mask_array = list(message.data)
        print('Kinect 1 (top) Starting...')
        #save only colors
        for index in xrange(message.height*message.width): #iterate through
            for k in xrange(len(color_mask_list)): 
                #iterate through color list, if the bytes match, save the color
                #in the mask
                if abs(color_mask_list[k][0] - ord(byte_array[3*index+0])) < threshold\
                        and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                        and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                    #The color was found in the byte index 
                    mask_array[3*index+0] = chr(color_mask_list[k][0])
                    mask_array[3*index+1] = chr(color_mask_list[k][1])
                    mask_array[3*index+2] = chr(color_mask_list[k][2])
                elif (k==0):
                    #only set to black on first run thru
                    mask_array[3*index+0] = chr(207) #
                    mask_array[3*index+1] = chr(207) #
                    mask_array[3*index+2] = chr(207) #
    top_mask.data = "".join(mask_array) #make char[] back into uint8[] string
    kinect1pub.publish(top_mask) #publish the mask for viewing
    print "\a" #DEBUG (sound the alarm)
    print "Top, Pic 1 Published!"
        
def _2_image_callback(message):
    global color_mask_list
    global mid_mask
    global threshold
    global kinect2pub
    mid_mask = Image()
    mid_mask.height = message.height
    mid_mask.width = message.width
    mid_mask.encoding = message.encoding
    mid_mask.is_bigendian = message.is_bigendian
    mid_mask.step = message.step

    if message.encoding == "bgr8":
        byte_array = list(message.data)
        mask_array = list(message.data)
        print('Kinect 2 (bottom) Starting...')
        for index in xrange(message.height*message.width):
            if (index < 10): #DEBUG PRINT FIRST 10 PIXELS! #DEBUG DEBUG DEBUG
                print('Index, B G R:')
                print(index)
                print(ord(byte_array[3*index+0]))
                print(ord(byte_array[3*index+1]))
                print(ord(byte_array[3*index+2])) 
            # END DEBUG
            for k in xrange(len(color_mask_list)):
                if abs(color_mask_list[k][0] - ord(byte_array[3*index+0])) < threshold\
                        and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                        and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                    mask_array[3*index+0] = chr(color_mask_list[k][0])
                    mask_array[3*index+1] = chr(color_mask_list[k][1])
                    mask_array[3*index+2] = chr(color_mask_list[k][2])
                elif (k==0):
                    #only set to black on first run
                    mask_array[3*index+0] = chr(207) #
                    mask_array[3*index+1] = chr(207) #
                    mask_array[3*index+2] = chr(207) #
    mid_mask.data = "".join(mask_array)
    kinect2pub.publish(mid_mask)
    print "\a" #DEBUG (sound the alarm)
    print "Bottom, Pic 2 Published!"

def _3_image_callback(message):
    global color_mask_list
    global mid_mask
    global threshold
    global kinect3pub
    mid_mask = Image()
    mid_mask.height = message.height
    mid_mask.width = message.width
    mid_mask.encoding = message.encoding
    mid_mask.is_bigendian = message.is_bigendian
    mid_mask.step = message.step

    if message.encoding == "bgr8":
        byte_array = list(message.data)
        mask_array = list(message.data)
        print('Kinect 3 (middle) Starting...')
        for index in xrange(message.height*message.width):
            for k in xrange(len(color_mask_list)):
                if abs(color_mask_list[k][0] - ord(byte_array[3*index+0])) < threshold\
                        and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                        and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                    mask_array[3*index+0] = chr(color_mask_list[k][0])
                    mask_array[3*index+1] = chr(color_mask_list[k][1])
                    mask_array[3*index+2] = chr(color_mask_list[k][2])
                elif (k==0):
                    #only set to black on first run
                    mask_array[3*index+0] = chr(207) #
                    mask_array[3*index+1] = chr(207) #
                    mask_array[3*index+2] = chr(207) #
    mid_mask.data = "".join(mask_array)
    kinect3pub.publish(mid_mask)
    print "\a" #DEBUG (sound the alarm)
    print "Middle, Pic 3 Published!"

def _1_cloud_callback(message):
    try:
        #make a generator, skipping points that have no depth, on points in 
        # list of uvs (index into image [col,row]) or if empty list, get all pt
        data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[]) 
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:
            iteration1 = next(data_out)
            i=i+1
    except StopIteration: 
        print "(Cloud 1top)"

def _2_cloud_callback(message):
    try:
        data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[])
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:
            iteration1 = next(data_out)
            i=i+1
    except StopIteration: 
        print "(Cloud 2bottom)"

def _3_cloud_callback(message):
    try:
        data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[])
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:
            iteration1 = next(data_out)
            i=i+1
    except StopIteration: 
        print "(Cloud 2bottom)"

def initialize():
    global kinect1pub
    global kinect2pub
    global kinect3pub
    global locpub
    rospy.init_node("localizeTOM") #DEBUG? wtf node problems
    locpub = rospy.Publisher("/tomservo/location",LocationList) #publish your locations
    kinect1pub = rospy.Publisher("/tomservo/mask1",Image) #test your mask
    kinect2pub = rospy.Publisher("/tomservo/mask2",Image) #woah!
    kinect3pub = rospy.Publisher("/tomservo/mask3",Image) #woah!
    rospy.Subscriber("/kinect1/rgb/image_color", Image, _1_image_callback)
    #rospy.Subscriber("/kinect1/depth_registered/points", PointCloud2, _1_cloud_callback)
    rospy.Subscriber("/kinect2/rgb/image_color", Image, _2_image_callback)
    #rospy.Subscriber("/kinect2/depth_registered/points", PointCloud2, _2_cloud_callback)
    rospy.Subscriber("/kinect3/rgb/image_color", Image, _3_image_callback)
    #rospy.Subscriber("/kinect3/depth_registered/points", PointCloud2, _3_cloud_callback)
    rospy.spin()

if __name__ == "__main__":
    initialize()


#!/usr/bin/env python
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import *
from cs1567p2.msg import *

color_mask_list = [[110,0,0], [102,102,150], [204, 255, 153], [128,128,250]]
threshold = 125
locpub = None
kinect3pub = None
kinect2pub = None
top_mask = Image()
mid_mask = Image()

def top_image_callback(message):
    global color_mask_list
    global top_mask
    global threshold
    global kinect3pub
    #make a new image if you want to view your mask
    top_mask = Image()
    top_mask.height = message.height
    top_mask.width = message.width
    top_mask.encoding = message.encoding
    top_mask.is_bigendian = message.is_bigendian
    top_mask.step = message.step
    if message.encoding == "bgr8": #this is image_color encoding
        byte_array = list(message.data) #convert unit8[] from string to chars
        print("Message Height:")
        print(message.height)
        print("Message Width:")
        print(message.width)
        for index in xrange(message.height*message.width): #iterate through
#
            for k in xrange(len(color_mask_list)): 
                #iterate through color list, if the bytes match, save the color
                #in the mask
                if abs(color_mask_list[k][0] - ord(byte_array[3*index])) < threshold\
                        and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                        and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                    #DEBUG
                    print("Found a good color, Here it is naturally:")
                    print(ord(byte_array[3*index+0]))
                    print(ord(byte_array[3*index+1]))
                    print(ord(byte_array[3*index+2]))
                    #ENDDEBUG
                    byte_array[3*index+0] = chr(color_mask_list[k][0])
                    byte_array[3*index+1] = chr(color_mask_list[k][1])
                    byte_array[3*index+2] = chr(color_mask_list[k][2])
                    #DEBUG
                    print("...and here it is the color mask list value:")
                    print(ord(byte_array[3*index+0]))
                    print(ord(byte_array[3*index+1]))
                    print(ord(byte_array[3*index+2]))
                    #ENDDEBUG
                else:
                    byte_array[3*index+0] = chr(255) #
                    byte_array[3*index+1] = chr(255) #
                    byte_array[3*index+2] = chr(255) #
    top_mask.data = "".join(byte_array) #make char[] back into uint8[] string
    kinect3pub.publish(top_mask) #publish the mask for viewing
    print "Top, Pic 3 Published!"
        
def mid_image_callback(message):
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
        #print(byte_array)
        for index in xrange(message.height*message.width):
            for k in xrange(len(color_mask_list)):
                if abs(color_mask_list[k][0] - ord(byte_array[3*index])) < threshold\
                        and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                        and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                    #DEBUG
                    print("Found a good color, Here it is naturally:")
                    print(ord(byte_array[3*index+0]))
                    print(ord(byte_array[3*index+1]))
                    print(ord(byte_array[3*index+2]))
                    #ENDDEBUG
                    byte_array[3*index+0] = chr(color_mask_list[k][0])
                    byte_array[3*index+1] = chr(color_mask_list[k][1])
                    byte_array[3*index+2] = chr(color_mask_list[k][2])
                    #DEBUG
                    print("...and here it is the color mask list value:")
                    print(ord(byte_array[3*index+0]))
                    print(ord(byte_array[3*index+1]))
                    print(ord(byte_array[3*index+2]))
                    #ENDDEBUG
                else:
                    byte_array[3*index+0] = chr(255) #
                    byte_array[3*index+1] = chr(255) #
                    byte_array[3*index+2] = chr(255) #
    mid_mask.data = "".join(byte_array)
    kinect2pub.publish(mid_mask)
    print "Bottom, Pic 2 Published!"


def top_cloud_callback(message):
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
        print "(Cloud 3top)"

def mid_cloud_callback(message):
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
    global kinect3pub
    global kinect2pub
    global locpub
    rospy.init_node("localize")
    locpub = rospy.Publisher("/tomservo/location",LocationList) #publish your locations
    kinect3pub = rospy.Publisher("/tomservo/mask3",Image) #test your mask
    kinect2pub = rospy.Publisher("/tomservo/mask2",Image) #woah!
    rospy.Subscriber("/kinect3/rgb/image_color", Image, top_image_callback)
    rospy.Subscriber("/kinect3/depth_registered/points", PointCloud2, top_cloud_callback)
    rospy.Subscriber("/kinect2/rgb/image_color", Image, mid_image_callback)
    rospy.Subscriber("/kinect2/depth_registered/points", PointCloud2, mid_cloud_callback)
    rospy.spin()

if __name__ == "__main__":
    initialize()


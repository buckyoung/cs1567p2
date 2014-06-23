#!/usr/bin/env python
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import *
from cs1567p2.msg import *
from collections import deque

#TAPE   = [240, 243, 244]
#RED    = [148, 126, 229] # Not bad
#GREEN  = [212, 241, 219] # Bad -- walls and oranges and whites
#BLUE   = [224, 174, 139] # Not bad -- lost on k2 sometimes
#ORANGE = [156, 201, 243] 
#BROWN  = [142, 179, 211] # Not terrible -- steals some red
BLACK  = [0,0,0]
#YELLOW = [165, 251, 253] # Not bad -- NEON ORANGE POST IT!, also yellow and some orange
#WHITE  = [255, 255, 255] #Really good, except computer tops
#Green and Orange dont play nice
#Red and Brown dont play nice
RED  = [89,85,225]
#LIZDKRED  = [56,56,166] #*having problems
#LIZGREEN  = [145,195,97] #*having problems ?? IS THIS ORANGE?
LTPURP = [210,160,198]
#LIZDKPURP = [122,83,105] #terrible - catches a lot of carpet
BLUE   = [227,186,88] #note: also picks up TARGBLUE
#TARGETS:
#TARGGREEN  = [95,135,102]
#TARGYELLOW = [120, 243, 250]
#TARGORANGE = [99,161,235]
#TARGBLUE = [222,201,79]
DRKPURP = [173,108,137]
#TARGBROWN = [104,145,198]
#TARGTAN   = [155,214,243]
color_mask_list = [BLUE, RED, DRKPURP, LTPURP]
threshold = 35
locpub = None
kinect1pub = None
kinect2pub = None
kinect3pub = None
_1_mask = Image()
_2_mask = Image()
_3_mask = Image()

class Point:
    row = -1
    col = -1
    def __init__(self, otherpoint=None):
        if(otherpoint != None):
            self.row = otherpoint.row
            self.col = otherpoint.col
class ColorPoint:
    row = -1
    col = -1
    color = [-1, -1, -1]
    def __init__(self, otherpoint=None):
        if(otherpoint != None):
            self.row = otherpoint.row
            self.col = otherpoint.col
            self.color = otherpoint.color
class Blob:    
    start = Point()
    color = [-1, -1, -1]
    min_row = -1
    max_row = -1
    min_col = -1
    max_col = -1
    num_px = 0
    center = Point()
    mask = Image()
    def __init__(self, start_cp, mask):
        self.start.row  = start_cp.row
        self.start.col  = start_cp.col
        self.color      = start_cp.color
        self.min_row    = start_cp.row
        self.max_row    = start_cp.row
        self.min_col    = start_cp.col
        self.max_col    = start_cp.col
        self.num_px     = 0
        self.center.row = start_cp.row
        self.center.col = start_cp.col
        self.mask       = mask

def print_color(message):
    global kinect3pub
    global top_mask
    top_mask = Image()
    top_mask.height = message.height
    top_mask.width = message.width
    top_mask.encoding = message.encoding
    top_mask.is_bigendian = message.is_bigendian
    top_mask.step = message.step
    b = 0
    g = 0
    r = 0
    sum = 0
    size = 10 # size by size square
    if message.encoding == "bgr8":
        byte_array = list(message.data)
        for row in range(size):
            for index in range(message.width*row, message.width*row+size):
                sum = sum+1
                b = b + ord(byte_array[3*index+0])
                g = g + ord(byte_array[3*index+1])
                r = r + ord(byte_array[3*index+2])
                byte_array[3*index+0] = chr(255)
                byte_array[3*index+1] = chr(50)
                byte_array[3*index+2] = chr(100)
    print("Color B G R:")
    print(b/sum)
    print(g/sum)
    print(r/sum)
    top_mask.data = "".join(byte_array)
    kinect3pub.publish(top_mask)

def _1_image_callback(message):
    global color_mask_list
    global _1_mask
    global threshold
    global kinect1pub
    #make a new image if you want to view your mask
    _1_mask = Image()
    _1_mask.height = message.height
    _1_mask.width = message.width
    _1_mask.encoding = message.encoding
    _1_mask.is_bigendian = message.is_bigendian
    _1_mask.step = message.step
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
    _1_mask.data = "".join(mask_array) #make char[] back into uint8[] string
    kinect1pub.publish(_1_mask) #publish the mask for viewing
    print "Top, Pic 1 Published!"
        
def _2_image_callback(message):
    global color_mask_list
    global _2_mask
    global threshold
    global kinect2pub
    _2_mask = Image()
    _2_mask.height = message.height
    _2_mask.width = message.width
    _2_mask.encoding = message.encoding
    _2_mask.is_bigendian = message.is_bigendian
    _2_mask.step = message.step
    if message.encoding == "bgr8":
        byte_array = list(message.data)
        mask_array = list(message.data)
        print('Kinect 2 (bottom) Starting...')
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
    _2_mask.data = "".join(mask_array)
    kinect2pub.publish(_2_mask)
    print "Bottom, Pic 2 Published!"
    localize(_2_mask)

def _3_image_callback(message):
    global color_mask_list
    global _3_mask
    global threshold
    global kinect3pub
    _3_mask = Image()
    _3_mask.height = message.height
    _3_mask.width = message.width
    _3_mask.encoding = message.encoding
    _3_mask.is_bigendian = message.is_bigendian
    _3_mask.step = message.step

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
    _3_mask.data = "".join(mask_array)
    kinect3pub.publish(_3_mask)
    print "Middle, Pic 3 Published!"
    localize(_3_mask)

def localize(mask):
    color_point = ColorPoint()
    #robot_colors = [DRKPURP]
    # iterate thru mask to find a certain color (Each robot will have its own color)
    #for color in robot_colors:
    color_point = find_color(mask, BLUE)
    blob = Blob(color_point, mask)
    print("starting fill blob")
    blob = fill_blob(blob, blob.start)
    print("finished fill blob, debug pub")
    global kinect2pub
    kinect2pub.publish(blob.mask)
    if blob.num_px > 100:
        #found our robot!
        color_point = ColorPoint()
    # fill color to make blob
    # is blob big enough to be a square?
    # yes, search around blob for the orientation color (same for each robot)
    # is orientation blob big enough to be square?
    # yes, we have a robot and an orientation
def find_color(mask, color):
    row = -1
    col = -1
    for index in xrange(mask.width*mask.height):
        if (mask.data[3*index+0] == chr(color[0])\
                and mask.data[3*index+1] == chr(color[1])\
                and mask.data[3*index+2] == chr(color[2])):
            # if the data pixel matches the color
            row = int(index/mask.width)
            col = index % mask.width
            break
    result = ColorPoint()
    result.row = row
    result.col = col
    result.color = color
    return result
    
#accept a blob and a start point
#Breadth first fill it
#return a blob
def fill_blob(blob, start_point):
    q = deque()
    q.append(start_point) #start_node is a ColorPoint
    mask_array = list(blob.mask.data)
    while(q): #while the q has items
        # Pop an item
        current_point = q.popleft()
        # If it has been visited, skip this iteration
        if(ord(mask_array[3*(current_point.row*blob.mask.width+current_point.col)+0]) == chr(0)\
                and ord(mask_array[3*(current_point.row*blob.mask.width+current_point.col)+1]) == chr(0)\
                and ord(mask_array[3*(current_point.row*blob.mask.width+current_point.col)+2]) == chr(0)):
            continue
        # Otherwise, turn the current point black
        mask_array[3*(current_point.row*blob.mask.width+current_point.col)+0] = chr(0)
        mask_array[3*(current_point.row*blob.mask.width+current_point.col)+1] = chr(0)
        mask_array[3*(current_point.row*blob.mask.width+current_point.col)+2] = chr(0)
        # Prepare neighbors
        u = Point(current_point)
        d = Point(current_point)
        l = Point(current_point)
        r = Point(current_point)
        u.row = u.row - 1
        d.row = d.row + 1
        r.col = r.col + 1
        l.col = l.col - 1
        ur     = Point(u)
        ur.col = ur.col + 1
        ul     = Point(u)
        ul.col = ul.col - 1
        dr     = Point(d)
        dr.col = dr.col + 1
        dl     = Point(d)
        dl.col = dl.col - 1
        # Enque neighbors if not out of bounds
        if u.row >= 0:
            q.append(u)
        if ur.row >= 0 and ur.col < blob.mask.width:
            q.append(ur)
        if r.col < blob.mask.width:
            q.append(r)
        if dr.row < blob.mask.height and dr.col < blob.mask.width:
            q.append(dr)
        if d.row < blob.mask.height:
            q.append(d)
        if dl.row < blob.mask.height and dl.col >= 0:
            q.append(dl)
        if l.col >= 0:
            q.append(l)
        if ul.row >= 0 and ul.col >= 0:
            q.append(ul)
    #save the new mask
    blob.mask.data = "".join(mask_array)
    return blob

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
#    rospy.Subscriber("/kinect1/rgb/image_color", Image, _1_image_callback)
    #rospy.Subscriber("/kinect1/depth_registered/points", PointCloud2, _1_cloud_callback)
    rospy.Subscriber("/kinect2/rgb/image_color", Image, _2_image_callback)
    #rospy.Subscriber("/kinect2/depth_registered/points", PointCloud2, _2_cloud_callback)
#    rospy.Subscriber("/kinect3/rgb/image_color", Image, _3_image_callback)
    #rospy.Subscriber("/kinect3/depth_registered/points", PointCloud2, _3_cloud_callback)
#    rospy.Subscriber("/kinect3/rgb/image_color", Image, print_color)
    rospy.spin()

if __name__ == "__main__":
    initialize()


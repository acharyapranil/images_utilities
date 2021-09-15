

# --------------> Program Introduction <------------------ #
# We extract the objects in a Image where objects are labelled and the label is in the xml file:
# Motivation: Let's say we want to train a classifer 


# Requirements
#     .xml file should have at least following information
#         <object>
#             <bndbox> 
#                 <xmin>
#                 <ymin>
#                 <xmax> 
#                 <ymax>
#            </object>

# !!!!!!!!!!!! KEY WE EXTRACT WHATEVER IS STORED INSIDE bndbox !!!!!!!!!!!! #

import glob
import os
from xml.etree import ElementTree

import cv2



#!!!!!!!!!!!!! -----> START INPUT FROM THE USER <------- !!!!!!!!!!!!!! #

# ------> START: Read a file and extract all bounding box stored inside the file bndbox   <------------- #
xml_filename = "test_img.xml"
img_filename = "test_img.jpg"
# ------> END: Read a file and extract all bounding box stored inside the file bndbox   <------------- #

#!!!!!!!!!!!!! -----> END INPUT FROM THE USER <------- !!!!!!!!!!!!!! #

dom = ElementTree.parse(xml_filename) #Read entire file
all_bounding_boxes = dom.findall("object") #From the file extract everything inside <object>
# Once we have extracted <object> we will extract bndbox which has xmin ymin xmax ymax

xmin = 0
ymin = 0
xmax = 0
ymax = 0

img = cv2.cvtColor(cv2.imread(img_filename), cv2.COLOR_BGR2RGB)

for c in all_bounding_boxes:
    
    content_inside_bndbox = c.find("bndbox")
    xmin = int( content_inside_bndbox.find("xmin").text )
    xmax = int( content_inside_bndbox.find("xmax").text )
    ymin = int( content_inside_bndbox.find("ymin").text )
    ymax = int( content_inside_bndbox.find("ymax").text )

    cv2.imshow("figure1", cv2.cvtColor(img[ ymin:ymax, xmin:xmax, : ], cv2.COLOR_RGB2BGR) )
    cv2.waitKey(2000)
    

 
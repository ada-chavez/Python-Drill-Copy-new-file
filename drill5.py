## Version: Python 2.7
##
## Date: 03/28/17
##
## Author: Ada Chavez http://adachavez.com
##
## Purpose: (Drill given by The Tech Academy) A program to determine txt files that have been modified/created in the
## last 24 hours and to then copy those files to another folder.

import shutil
import os
import time
from datetime import datetime,timedelta

def compareTimes(folderA, folderB):
    # calculates the current time
    currentTime = datetime.now()
    # calculates the time 24 hours ago
    time24HrsAgo = currentTime - timedelta(hours=24)

    
    for fileList in os.listdir(folderA):
        # files path and the modified datetime will be shown
        files = os.path.realpath(os.path.join(folderA,fileList))
        
        if files.endswith('.txt'):
            # shows modified time for each file
            folderAModifiedTime = datetime.fromtimestamp(os.path.getmtime(files))
            # compares the modified time for each file to the time 24 hours ago
            if folderAModifiedTime > time24HrsAgo:
                
                print files, "copied file to: ", folderB
                # copies files to folder B
                shutil.copy(files,folderB)
            else:
                print files, "was not copied"
    
    
folderA = 'C:/Users/techacademy/Desktop/A'
folderB = 'C:/Users/techacademy/Desktop/B'

compareTimes(folderA,folderB)


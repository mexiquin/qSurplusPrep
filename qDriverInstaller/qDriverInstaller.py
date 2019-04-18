
'''
Developed by: Quinton Jasper
Version: 1.0

This program is designed to more easily access
driver install resources and automate the process
of pc preparation for NAU Property Surplus

Steps of Execution:

1. Install network drivers from SDITool database (stored as dependency on usb drive)

2. Contact NAU servers that contain driver files (IP: 192.168.0.1 I believe)

3. Install Dell Command Update for any BIOS updates (do research into DCU API)

4. Download updated Media Creation Tool from microsoft website. Places file on to desktop for easy access

'''

import os
import sys
import glob
import requests

# constant for finding the scripts dir with all dependencies
# as well as constant for the desktop directory of any given machine
scriptsDir =  os.path.join(os.getcwd(), 'Scripts')
desktopDir = os.path.join(os.environ["HOMEPATH"], "Desktop")

# Main access point of the program. Runs all functions in order they need to be ran
def main():
    # Testing out functions
    usrIn = input("Put url in here for testing:\n")
    downloadToDir(usrIn, desktopDir)
        

# Searches direcory for file that contains given keywords
def findExecutable(keyword):
	for name in glob.glob('Scripts/%s.exe' % keyword):
		return name

# Install Dell Command update for later manual use
def installDell():
	pass

# Install network drivers from SDI Tool.
def installNetwork():
	pass

# Download a file from a given URL to the specified directory (Works!)
def downloadToDir(url, outDir):
        fileName = fileNameFromURL(url)
        directory = '%s/%s' % (outDir, fileName)
        requestor = requests.get(url, allow_redirects = True)

        file = open(directory, "wb")
        file.write(requestor.content)

# Finds the name of the file based on the url name (Works!)
def fileNameFromURL(url):
	if url.find('/'):
		return url.rsplit('/', 1)[1]

if __name__ == "__main__":
	main()

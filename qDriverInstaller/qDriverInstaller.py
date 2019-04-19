
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
import subprocess
import pyfiglet
import cowsay

# constant for finding the scripts dir with all dependencies
# as well as constant for the desktop directory of any given machine
scriptsDir =  os.path.join(os.getcwd(), 'Scripts')
desktopDir = os.path.join(os.environ["HOMEPATH"], "Desktop")

# Make sure to update this URL every time that windows 10 releases a major update
mediaCreationToolURL = "https://software-download.microsoft.com/download/pr/MediaCreationTool1809.exe"

# Main access point of the program. Runs all functions in order they need to be ran
def main():
    # Simple main functionality to test if the build with pyInstaller will work

    # Welcome interface
    #printInterface()
    printCowsay("Quinton's Driver Installer: Version 2.0")

    # take input for what install is wanted
    installChoice = input("(1) Install Network\n(2) Install Dell Command Update\n(ENTER) Both\n")

    if "1" in installChoice:
        installNetwork()
    elif "2" in installChoice:
        installDell()
    else:
        installNetwork()
        installDell()

    # Download Media Creation Tool to Desktop\
    downloadToDir(mediaCreationToolURL, desktopDir)
        

# Searches direcory for file that contains given keywords
def findExecutable(keyword):
	for name in glob.glob('Scripts/%s.exe' % keyword):
		return name

# Install Dell Command update for later manual use (Works!)
def installDell():
	subprocess.run([findExecutable("DCU"), "/s"])

# Install network drivers from SDI Tool. (Works!)
def installNetwork():
	subprocess.run([findExecutable("SDI_x64"), "-autoinstall", "-autoclose", "-showconsole", "-nogui"])

# Download a file from a given URL to the specified directory (Works!)
def downloadToDir(url, outDir):
        fileName = fileNameFromURL(url)
        directory = '%s/%s' % (outDir, fileName)
        requestor = requests.get(url, allow_redirects = True)

        file = open(directory, "wb")
        file.write(requestor.content)

# Installs the drivers utilizing ITS's driver library
def installNAUDrivers():
    pass

def printInterface():
    welcomeBanner = pyfiglet.figlet_format("Quinton's\nDriver\nInstaller")
    print(welcomeBanner)

def printCowsay(input):
    cowsay.cow(input)

# Finds the name of the file based on the url name (Works!)
def fileNameFromURL(url):
	if url.find('/'):
		return url.rsplit('/', 1)[1]

if __name__ == "__main__":
	main()

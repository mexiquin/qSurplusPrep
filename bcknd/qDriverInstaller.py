"""
@author Quinton Jasper
Version: 2.0

This program is designed to more easily access
driver install resources and automate the process
of pc preparation for NAU Property Surplus

Steps of Execution:

1. Install network drivers from SDITool database (stored as dependency on usb drive)

2. Contact NAU servers that contain driver files (IP: 192.168.0.1 I believe)

3. Install Dell Command Update for any BIOS updates (do research into DCU API)

4. Download updated Media Creation Tool from microsoft website. Places file on to desktop for easy access

"""

import cowsay
import glob
import os
import requests
import subprocess
import time

from . import timeSet

# constant for finding the scripts dir with all dependencies
# as well as constant for the desktop directory of any given machine
scriptsDir = os.path.join(os.getcwd(), 'Scripts')
desktopDir = os.path.join(os.environ["USERPROFILE"], "Desktop")

'''
This is a modified url that microsoft uses to redirect to the actual download of MediaCreationToolXXXX.exe
Hopefully, this url will not need to be changed, though we will keep our eye on it
for each major release of the windows 10 operating system
'''
mediaCreationToolURL = "https://go.microsoft.com/fwlink/?LinkId=691209"


# Main access point of the program. Runs all functions in order they need to be ran (Only if ran in CLI)
def main():
    # Simple main functionality to test if the build with pyInstaller will work

    # Welcome interface
    # printInterface()
    printCowsay("Quinton's Driver Installer: Version 2.0")
    create_scripts()

    # take input for what install is wanted
    print("####### OPTIONS #######\n")
    install_choice = input(
        "(ENTER) Install Everything (Recommended)\n(1) Install Network\n(2) Install Dell Command Update\n(3) Install "
        "ITS Drivers\n(4) Download Media Creation Tool\n(5) Update system time\n")

    if "1" in install_choice:
        install_network()
    elif "2" in install_choice:
        install_dell()
    elif "3" in install_choice:
        installNAUDrivers()
    elif "4" in install_choice:
        download_to_dir(mediaCreationToolURL, desktopDir)
    elif "5" in install_choice:
        # Fix system clock time so that the rest of the program will run smoothly
        timeSet.updateTime()

    elif install_choice == "":
        install_network()
        timeSet.updateTime()
        install_dell()
        installNAUDrivers()
        download_to_dir(mediaCreationToolURL, desktopDir)
    else:
        input("Error: Invalid input value\n\nPress ENTER to try again...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


# Searches directory for file that contains given keywords
def find_exec(keyword):
    for name in glob.glob('%s*.exe' % keyword):
        return name


# Install Dell Command update for later manual use (Works!)
def install_dell():
    print("Installing Dell Command Update...\n")
    subprocess.run([find_exec("DCU"), "/s"])
    print("Dell Command Update has been installed!")


# Install network drivers from SDI Tool. (Works!)
def install_network():
    subprocess.run([find_exec("SDI_x64"), "-autoinstall",
                    "-showconsole", "-nogui", "-autoclose"])


# Download a file from a given URL to the specified directory (Works!)
def download_to_dir(url, outDir):
    requestor = requests.get(url, allow_redirects=True)
    fileName = fileNameFromURL(requestor.url)
    directory = f'{outDir}/{fileName}'

    # Exception handling for the HTTPS request
    try:
        requestor.raise_for_status()
    except Exception as urlOof:
        print(f"Error in accessing URL: {urlOof}")
        input("Press ENTER to continue...")

    print(f"Downloading {fileName}")

    # Some exception handling for file writing stuff
    try:
        file = open(directory, "wb")
        file.write(requestor.content)
        file.close()
    except IOError as e:
        print(f"Error writing file {e}")
        time.sleep(7)

    else:
        print(f"Download of {fileName} Complete")


# Installs the drivers utilizing ITS's driver library
def installNAUDrivers():
    subprocess.run("NAUDriver.bat")


# Default methond of displaying the Quinton Driver Installer Text
def printCowsay(input):
    cowsay.cow(input)


# Potential for implementing an instruction manual for any curious technicians
def printInstructions():
    pass


# Finds the name of the file based on the url name (Works!)
def fileNameFromURL(url):
    if url.find('/'):
        return url.rsplit('/', 1)[1]

# Method for creating and eventually populating a scripts folder in case none exists


def create_scripts():
    try:
        os.chdir(scriptsDir)
    except OSError as oopsDirectory:
        print("You're missing your scripts folder!\nAutogenerating folder for you...")
        os.mkdir(scriptsDir)


# if scripts directory is empty, this method will be called. Will populate scripts folder with necessary files.
'''
Files that we need:
- SDITool - With network drivers only
- Dell Command Update
- NAU Driver library .bat
'''

TODO
def populate_scripts():
    # Get dcu from url and push to file
    download_to_dir('https://downloads.dell.com/FOLDER05055451M/1/Dell-Command-Update_DDVDP_WIN_2.4.0_A00.EXE',
                    os.path.join(scriptsDir, 'DCU.exe'))
    #


if __name__ == "__main__":
    main()

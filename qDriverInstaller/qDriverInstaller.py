
'''
Developed by: Quinton Jasper
Version: 2.0

This program is designed to more easily access
driver install resources and automate the process
of pc preparation for NAU Property Surplus

Steps of Execution:

1. Install network drivers from SDITool database (stored as dependency on usb drive)

2. Contact NAU servers that contain driver files (IP: 192.168.0.1 I believe)

3. Install Dell Command Update for any BIOS updates (do research into DCU API)

4. Download updated Media Creation Tool from microsoft website. Places file on to desktop for easy access

'''

import os, sys, glob, requests, subprocess, pyfiglet, cowsay, time
import timeSet

# constant for finding the scripts dir with all dependencies
# as well as constant for the desktop directory of any given machine
scriptsDir =  os.path.join(os.getcwd(), 'Scripts')
desktopDir = os.path.join(os.environ["USERPROFILE"], "Desktop")

'''
This is a modified url that microsoft uses to redirect to the actual download of MediaCreationToolXXXX.exe
Hopefully, this url will not need to be changed, though we will keep our eye on it
for each major release of the windows 10 operating system
'''
mediaCreationToolURL = "https://go.microsoft.com/fwlink/?LinkId=691209"

# Main access point of the program. Runs all functions in order they need to be ran
def main():
    # Simple main functionality to test if the build with pyInstaller will work

    # Welcome interface
    #printInterface()
    printCowsay("Quinton's Driver Installer: Version 2.0")
    os.chdir(scriptsDir)

    # take input for what install is wanted
    print("####### OPTIONS #######\n")
    installChoice = input("(ENTER) Install Everything (Reccomended)\n(1) Install Network\n(2) Install Dell Command Update\n(3) Install ITS Drivers\n(4) Download Media Creation Tool\n(5) Update system time\n")

    if "1" in installChoice:
        installNetwork()
    elif "2" in installChoice:
        installDell()
    elif "3" in installChoice:
        installNAUDrivers()
    elif "4" in installChoice:
        downloadToDir(mediaCreationToolURL, desktopDir)
    elif "5" in installChoice:
		# Fix system clock time so that the rest of the program will run smoothly
        timeSet.updateTime()

    elif installChoice == "":
        installNetwork()
        timeSet.updateTime()
        installDell()
        installNAUDrivers()
        downloadToDir(mediaCreationToolURL, desktopDir)
    else:
        input("Error: Invalid input value\n\nPress ENTER to try again...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

        

# Searches direcory for file that contains given keywords
def findExecutable(keyword):
    for name in glob.glob('%s*.exe' % keyword):
        return name

# Install Dell Command update for later manual use (Works!)
def installDell():
	subprocess.run([findExecutable("DCU"), "/s"])

# Install network drivers from SDI Tool. (Works!)
def installNetwork():
	subprocess.run([findExecutable("SDI_x64"), "-autoinstall", "-autoclose", "-showconsole", "-nogui"])

# Download a file from a given URL to the specified directory (Works!)
def downloadToDir(url, outDir):
    requestor = requests.get(url, allow_redirects = True)
    fileName = fileNameFromURL(requestor.url)
    directory = '%s/%s' % (outDir, fileName)

    # Exception handling for the HTTPS request
    try:
        requestor.raise_for_status()
    except Exception as urlOof:
        print("Error in acessing URL: %s", urlOof)
        input("Press ENTER to try again...")
        main()

    print("Downloading %s" % fileName)

    # Some exception handling for file writing stuff
    try:
        file = open(directory, "wb")
        file.write(requestor.content)
        file.close()
    except IOError as e:
        print("Error writing file %s" % e)
        time.sleep(7)

    else:
        print("Download of %s Complete" % fileName)

# Installs the drivers utilizing ITS's driver library
def installNAUDrivers():
    subprocess.run("NAUDriver.bat")

# As of right now, this is unused. Is another option for printing
# the welcome text
def printInterface():
    welcomeBanner = pyfiglet.figlet_format("Quinton's\nDriver\nInstaller")
    print(welcomeBanner)

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

if __name__ == "__main__":
	main()

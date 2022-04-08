# Quinton's Driver Installer

### Note:
The main branch is treated much like an unstable testing branch
I recommend you download and use the build from the Stable branch. There,
I will publish the version of the program that is prepared for use
on the Surplus floor

This is a rewrite of the original NAU Surplus driver installer I wrote written in Go. This edition is written in python
and introduces additional functionality that would have been a pain to write in Go.

# New Features

## New Interface Screen
To be totally honest, nothing much has really changed here, other than the inclusion of a few more install options, as well as
a cute cow displaying the name of the application. The goal is to eventually implement an easy to use GUI interface over the course of the application's development.

## Downloads MediaCreationTool directly from Microsoft's Website
Initially, the media creation tool executable was included on the installation usb and had to manually by copied and pasted
onto the target computer for the Windows 10 update step. Now, the script will download a copy directly from the microsoft website
and save it to the target computer's Desktop folder

## Auto-Corrects system clock 
This version of the installer will automatically update the system clock. This
is always helpful when accessing the internet. If you don't know what I mean,
most of this program will not work, since it is necessary to access the internet
to install drivers. And, with the incorrect time, you can not access the internet.

## *NEW* GUI Implementation
We now have an easy to use GUI that will save your fingers and sanity from writing the commands
into the command line. It will be constantly updated and maintained to make sure that nothing breaks
and that the interface is as easy to understand as possible for our technicians.

## How To Make The .exe
In case you need to "recompile" this code, you're going to need to convert these .py files into a single .exe file.
To do this, make sure you have a copy of Python 3.7 (the version this code was tested on)
installed on the computer and make sure _pyinstaller_ is installed using the
python tool __pip__. 

If you're not sure it is installed, go to a cmd window and type:
```bash
pip install pyinstaller
```

Here, you will need to navigate into the folder containing the .py files (within
the cmd window). Make yourself familiar with the __cd__ command in the console. For example:
```bash
cd Downloads/qSurplusPrep
```

Once you're in the folder containing all of the .py files, run the command in your
console:
```bash
pyinstaller --uac-admin --onefile userInterface.py
```

__NOTE__: there is a known issue with this process and the _uac-admin_ command.
if any errors spring up from this, refer to this stackoverflow page: [PyInstaller UAC Issue](https://stackoverflow.com/questions/43068920/pyinstaller-uac-not-working-in-onefile-mode)

After this command is run, however, it should spit out a .exe file inside of a folder named __dist__

__NOTE__: You're done creating the .exe However, when you put it on a USB, make sure that it is accompanied by
the _Scripts_ folder, containing all of the install tools. The folder hierarchy should look like this:

* userInterface.exe
* Scripts
    * SDI.exe
    * DCU.exe
    * etc.
    
Where userInterface.exe is the compiled python program to double-click.

I will try to include a copy of the latest working _Scripts_ file so  that you don't have to search around the internet for
the correct dependencies. (Inside __Latest_Working_Scripts__ folder)

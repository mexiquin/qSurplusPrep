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

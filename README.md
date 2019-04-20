# qSurplusPrep

This is a rewrite of the original NAU Surplus driver installer I wrote written in Go. This edition is written in python
and introduces additional functionality that would have been a pain to write in Go.

# New Features

## New Interface Screen
To be totally honest, nothing much has really changed here, other than the inclusion of a few more install options, as well as
a cute cow displaying the name of the application. The goal is to eventually implement an easy to use GUI interface over the course of the application's development.

## Downloads MediaCreationTool directly from microsoft's Website
Initially, the media creation tool executable was included on the installation usb and had to manually by copied and pasted
onto the target computer for the Windows 10 update step. Now, the script will download a copy directly from the microsoft website
and save it to the target computer's Desktop folder

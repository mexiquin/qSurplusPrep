"""
This file is designed to add a Graphical User Interface
to the driver install program. (All in the name of simplicity)

@author Quinton Jasper
"""

import PySimpleGUI as SG

import qDriverInstaller

# Layout of the initial window

layout = [
    [SG.Text("Surplus Driver Installer", justification='center', font=("Helvetica", 18))],
    [SG.Text("What would you like to do?")],
    [SG.Drop(values=("Install All", "Network", "Dell Command Update", "ITS Drivers", "Media Creation Tool", "Time Set"))],
    [SG.Submit(tooltip="Submit to execute the action(s)"), SG.Quit()]
]

window = SG.Window("Quinton's Driver Installer", default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read()

    if event is None or event == 'Quit':
        break

    value = values[0]

    qDriverInstaller.create_scripts()

    if "Network" in value:
        qDriverInstaller.install_network()
    elif "Dell" in value:
        qDriverInstaller.install_dell()
    elif "ITS" in value:
        qDriverInstaller.installNAUDrivers()
    elif "Creation Tool" in value:
        qDriverInstaller.download_to_dir(qDriverInstaller.mediaCreationToolURL, qDriverInstaller.desktopDir)
    elif "Time Set" in value:
        qDriverInstaller.timeSet.updateTime()
    elif "All" in value:
        qDriverInstaller.install_network()
        qDriverInstaller.timeSet.updateTime()
        qDriverInstaller.install_dell()
        qDriverInstaller.installNAUDrivers()
        qDriverInstaller.download_to_dir(qDriverInstaller.mediaCreationToolURL, qDriverInstaller.desktopDir)
        print("\nAll operations have been completed!\n")

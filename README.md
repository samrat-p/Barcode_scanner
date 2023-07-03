# Barcode Scanner System using Python 
<p>A barcode scanner system is an essential tool for capturing and processing barcode data efficiently. By utilizing Python, you can develop a barcode scanner system that timestamps data each time a barcode is scanned. I made this project basically for an small office system. Corporate life sucks !!!</p>

## lets go thorough how the system is works
<p>Everytime a barcode is scanned a python libary will decode the data and process the data, after processing the data,a function will get the barcode data and timestamps. This can be achieved using a Pandas Dataframe or You can use other kinds of Dataframe.After successfully a barcode scan a sound will prompt to know the user that the barcode has been scanned sucessfully.
Everytime scanning a barcode each data with their required field of information will be stored in a excel sheet (.xlsx Format file), this allows for easy data retrival and analysis.
for Preventing Spams (like scanning a same barcode multiple time in a short time period), after scanning a barcode users have to wait another 3 seconds to scan another barcode.</p>

## what could i have done better?
<p> I wanted shift this system into an audrino board and add a GUI.So users can interact with the system.</p>

## What u need to run this code -- ??
<p>You need a create a python virtual enviroment (why virtual enviroment? well every package you install inside the enviroment, the packages does not mess with your c drive or wherever you install your python) and <b>Needs to have this packages below <b>

- contourpy==1.1.0
- cycler==0.11.0
- et-xmlfile==1.1.0   
- fonttools==4.40.0
- kiwisolver==1.4.4
- matplotlib==3.7.1
- numpy==1.25.0
- opencv-python==4.7.0.72
- openpyxl==3.1.2
- packaging==23.1
- pandas==2.0.3
- Pillow==9.5.0
- pygame==2.5.0
- pyparsing==3.1.0
- python-dateutil==2.8.2
- pytz==2023.3
- pyzbar==0.1.9
- six==1.16.0
- tzdata==2023.3





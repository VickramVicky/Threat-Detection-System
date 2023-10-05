# Threat-Detection-System
# Objective
This work is an attempt to design and develop a system which can detect the handguns in no time with less computational resources.

# Project Requirements
Python
Pip
PipEnv-To create Virtual Envs

# Log:
--Create Vitrual Envvironment in Dev/Clinetside using PipEnv using pythonversion 3.8(pip install VirtualEnv pipenv)
--install Dependencies
	--numpy,pyqt5.opencvheadless,requests,opencv in the virtual Env
	--D:\Python Projects\Gun Recogonition\Dev\Client_side>pipenv install requests numpy pyqt5 opencv-python-headless
	--The installed Dependencies can be seen through the pip file in the folder client side
--install QT designer to create a GUI application for the client side 
--intall pyQT Package
--install pip install opencv-python

# Methodology

Our Proposed System is about the Threat detection in our area which is achieved using the following Functions
• Functionality to capture the Video from the CCTV and covert those to the images
• With the images has the Input we have the Functionality that capture the threat either Handgun.
• Functionality that will alert the near by Officers

# Dataset

Currently we have trained the Dataset with the 1106 records where we have using this to deduct the threat that we are facing in the surrounding. These datasets will have the ability to deduct the Handgun as of now. Will be later trained for the other weapons also. However, this dataset contains a small number of records which could affect the efficiency of the model but on later stages we will train for more data.

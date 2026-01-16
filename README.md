# bachtis_group_scripts
A collection of some Python scripts I created for working within the CMS group under Dr. Michalis Bachtis at UCLA.

# kraken_plots.py
This script was for parsing through a text file for an extended monitoring test of the Kraken PCB. The text file contained readouts of various parameters for certain components within the board at different timeslices. The script reads through the file, separates and reoraganizes the data into multiple time-series arrays for each parameter for each component, and plots the data according to the desired parameters.

# clock_miner.py
This script was for automating a task during testing of the Octopus PCBs. During testing, clock frequencies created from the 32 crystal oscillators as well as the 10 programmable clock synthesizer outputs were measured. These frequencies were to be entered into a database in Google Sheets. For automation, a spreadsheet was generated of the measured clock frequencies. The script reads through the spreadsheet, updating the labels of the measured values from the program to match the labels within the database. It then establishes a connection with and gives the program authorization to write to Google Sheets. The script then writes the values to the database within Google Sheets in the proper location.

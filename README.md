# MadHacks-Spring-2023

24 Hour Hackathon at UW - Madison

Worked on solo project, Following TDS's Sponsor challenge to work with networking, something I have never touched before. 

Created a flask web app to run on a localhost, utilizes a python script that works with nmap to scan network ports to check for various conditions.

This is also done with a vulnerability scan based off of the nmap NSE scrip vulscan(https://github.com/scipag/vulscan)

Information is then saved as xml and then turned into an HTML document for the user to read on the website. In addition, the website will display a map of the IP addresses found.
(Further implementation wanted if time, like adding vulnerability color etc)

## TO RUN THE PROGRAM

If there is not a config.py file, please create one:

if you would like to use the free key just have one line in the file
```api_key = "free"```
if you plan to purchase a key, please replace free with your key

Please install dependencies: ```pip install -r "requirements.txt"```

After all the dependencies have installed you can run the program with: ```python3 main.py``` in console

Navigate to localhost:5500 or http://127.0.0.1:5500, etc(available addresses will display in the command line

Enter your target IP/address in the scan target field and wait for the script to fully execute, and then feel free to open the report or zoom in on the map  :)




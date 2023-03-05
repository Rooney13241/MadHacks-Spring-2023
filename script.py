import subprocess
import datetime
from bs4 import BeautifulSoup
import os

CURRENT_FILENAME = ""


def scan(target):
    nmap_command = ["nmap", "-oX", "output.xml", "-sV", "-T4", "--script", "vulners", target]

    result = subprocess.run(nmap_command)

    if result.returncode == 0:
        print("Nmap command executed succesfully.")
    else:
        print(f"An error occurred while running the Nmap command. Return code: {result.returncode}")
        exit()
    directory = './htmlfiles/'
    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{directory}{date_time}.html'
    global CURRENT_FILENAME
    CURRENT_FILENAME = filename
    xml_to_html = ["xsltproc", "output.xml", "-o", filename]

    step2 = subprocess.run(xml_to_html)

    if result.returncode == 0:
        print("xsltproc command executed succesfully.")
    else:
        print(f"An error occurred while running the xsltproc command. Return code: {result.returncode}")
        exit()


def locationid():

    addr_list = set()

    with open('output.xml', 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, 'xml')
    b_address = bs_data.find_all('address')
    for val in b_address:
        addr_list.add(val.get('addr'))

    return addr_list

if __name__ == '__main__':
    locationid()

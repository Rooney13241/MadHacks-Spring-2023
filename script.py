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
    addr_list = []
    if not os.path.isfile('output.xml'):
        return addr_list

    with open('output.xml', 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, 'xml')
    b_address = bs_data.find_all('address')
    for val in b_address:
        addr_list.append(val.get('addr'))
    addr_list = set(addr_list)
    return addr_list


def vulnercount():
    with open('output.xml', 'r') as f:
        xml = f.read()

    soup = BeautifulSoup(xml, 'xml')

    cvss_scores = {}
    host_tag = soup.find_all('host')
    for host in host_tag:
        addr = host.find('address')['addr']
        cvss_list = []
        for elem in host.find_all('elem', {'key': 'cvss'}):
            cvss_list.append(float(elem.text))

        cvss_scores[addr] = cvss_list
    return cvss_scores
if __name__ == '__main__':
    d = vulnercount()
    x = locationid()
    for y in x:
        if len(d[y]) == 0:
            d[y] = [0]
    print(d)
    # scan('scanme.nmap.org')
    # locationid()

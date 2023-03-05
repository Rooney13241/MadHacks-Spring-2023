import subprocess

target = input("What is the target")

nmap_command = ["nmap", "-oX", "output.xml", "-sV", "--script", "vulners", target]

result = subprocess.run(nmap_command)

if result.returncode == 0:
	print("Nmap command executed succesfully.")
else:
	print(f"An error occurred while running the Nmap command. Return code: {result.returncode}")
	exit()


xml_to_html = ["xsltproc", "output.xml", "-o", "analysis.html"]

step2 = subprocess.run(xml_to_html)

if result.returncode == 0:
        print("xsltproc command executed succesfully.")
else:
        print(f"An error occurred while running the xsltproc command. Return code: {result.returncode}")
        exit()


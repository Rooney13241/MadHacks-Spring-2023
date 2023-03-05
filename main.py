from flask import Flask, render_template, url_for, send_file, request
import os
import script
from ip2geotools.databases.noncommercial import DbIpCity
import config

app = Flask(__name__)
html_dir = './htmlfiles/'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user input from the request
        user_input = request.form['user_input']
        # Run the user input on the command line
        script.scan(user_input)

    addr_list = script.locationid()
    coordinates = {}
    vuln = script.vulnercount()
    for ip_address in addr_list:
        response = DbIpCity.get(ip_address, api_key=config.api_key)
        latitude = response.latitude
        longitude = response.longitude
        # if (latitude,longitude) not in count:
        #     count[(latitude,longitude)] = 0
        # count[(latitude,longitude)] += 1
        # if not coordinates:
        #     coordinates[ip_address] = (latitude, longitude, vuln[ip_address])
        # elif latitude == coordinates.get(ip_address)[0] and longitude == coordinates.get(ip_address)[1] and len(vuln[ip_address]) > 0:
        #     print(vuln[ip_address])
        if len(vuln[ip_address]) == 0:
            vuln[ip_address] = [0]
        if not coordinates:
            coordinates[ip_address] = (latitude, longitude, vuln[ip_address])
        else:
            for key, value in dict(coordinates).items():
                if latitude == value[0] and longitude == value[1] and len(vuln[ip_address]) > 1:
                    del coordinates[key]
                    coordinates[ip_address] = (latitude, longitude, vuln[ip_address])
                elif latitude == value[0] and longitude == value[1] and len(vuln[ip_address]) == 0 and len(value[2]) == 0:
                    del coordinates[key]
                    coordinates[ip_address] = (latitude, longitude, vuln[ip_address])
                else:
                    coordinates[ip_address] = (latitude, longitude, vuln[ip_address])

        # coordinates[ip_address] = (latitude, longitude)
    print(coordinates)
    html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
    html_files.sort(reverse=True)
    # Save the output to a file
    # Return the output file to the user
    return render_template('index.html', html_files=html_files, coordinates=coordinates)


@app.route('/view/<filename>')
def view(filename):
    filepath = os.path.join(html_dir, filename)
    return send_file(filepath)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500)

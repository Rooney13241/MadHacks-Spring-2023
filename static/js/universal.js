var map = L.map('map').fitWorld();

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function addMarkers(coordinates){
    for (var ip in coordinates) {
        var color = 'violet'; //default color
        if (coordinates[ip][2][0] == 0.0){
              color = 'green';
        }
        else if (coordinates[ip][2][0] < 4.0) {
              color = 'gold';
        }
        else if (coordinates[ip][2][0] < 8.0){
              color = 'red';
        }
        else if (coordinates[ip][2][0] >= 8.0){
              color = 'black';
        }
        console.log(color);

        var length = ((coordinates[ip][2].length == 1) ? 0 : coordinates[ip][2].length);
        L.marker(coordinates[ip], {icon: L.icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-'+color+'.png',
    iconSize: [25, 41], iconAnchor: [12, 41]
    })})
    .addTo(map)
    .bindPopup(ip + 'highest risk score: ' + coordinates[ip][2][0] +', Number of vulnerabilities: ' +
    length);
//' (' + coordinates[ip][2] + ' occurrences)'
    }
}

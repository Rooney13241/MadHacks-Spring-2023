var map = L.map('map').fitWorld();

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var counter = 0;

function addMarkers(coordinates){
    for (var ip in coordinates) {
        var color = 'green'; // alternate marker color
        L.marker(coordinates[ip], {icon: L.icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-'+color+'.png',
    iconSize: [25, 41], iconAnchor: [12, 41]
    })})
    .addTo(map)
    .bindPopup(ip);
    counter++;
//' (' + coordinates[ip][2] + ' occurrences)'
    }
}

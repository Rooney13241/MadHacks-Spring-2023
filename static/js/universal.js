var map = L.map('map').fitWorld();

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function addMarkers(coordinates){
    for (var ip in coordinates) {
        console.log(coordinates[ip])
        var color;
        if (coordinates[ip][2] < 50) {
            color = 'red';
        } else if (coordinates[ip][2] < 100) {
            color = 'orange';
        } else {
            color = 'green';
        }
        L.marker(coordinates[ip], {icon: L.icon({
        iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-'+color+'.png',
        iconSize: [25, 41], iconAnchor: [12, 41]
        })}).addTo(map).bindPopup(ip);
    }
}

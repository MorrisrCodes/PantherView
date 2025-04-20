document.addEventListener("DOMContentLoaded", function () {
    // Example button functionality
    document.getElementById("changeViewBtn").addEventListener("click", function () {
        alert("Changing map view!");
        // Add logic to modify map properties here
    });

    document.getElementById("zoomInBtn").addEventListener("click", function () {
        map.zoomIn(); // Assuming 'map' is globally accessible
    });

    document.getElementById("zoomOutBtn").addEventListener("click", function () {
        map.zoomOut(); 
    });

    document.getElementById("resetViewBtn").addEventListener("click", function () {
        map.flyTo({ center: [-74.0066, 40.7135], zoom: 15.5, pitch: 45, bearing: -17.6 });
    });
});

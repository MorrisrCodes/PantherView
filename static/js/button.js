// document.addEventListener("DOMContentLoaded", function () {
//     // Example button functionality
//     document.getElementById("changeViewBtn").addEventListener("click", function () {
//         alert("Changing map view!");
//         // Add logic to modify map properties here
//     });

//     document.getElementById("zoomInBtn").addEventListener("click", function () {
//         map.zoomIn(); // Assuming 'map' is globally accessible
//     });

//     document.getElementById("zoomOutBtn").addEventListener("click", function () {
//         map.zoomOut(); 
//     });

//     document.getElementById("resetViewBtn").addEventListener("click", function () {
//         map.flyTo({ center: [-74.0066, 40.7135], zoom: 15.5, pitch: 45, bearing: -17.6 });
//     });
// });

function handleIssueSelection(locationName, issueType) {
    console.log("Issue button clicked:", locationName, issueType);
    alert(`Issue reported for ${locationName}: ${issueType}`);
    reportToServer(locationName, issueType);
}

function handleEventSelection(locationName, eventType) {
    console.log("Event button clicked:", locationName, eventType);
    alert(`Event reported for ${locationName}: ${eventType}`);
    reportToServer(locationName, eventType);
}

function reportToServer(location, type) {
    fetch("/report", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            location: location,
            type: type
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Report saved:", data);
    })
    .catch(error => {
        console.error("Error reporting:", error);
    });
}

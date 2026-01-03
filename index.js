const WebSocket = require('ws');

// --- SECURITY BEST PRACTICE ---
// In Node.js, you should load this from a secret environment variable:
// const API_KEY = process.env.AISSTREAM_API_KEY;
const API_KEY = "864002057a10f30379dae6cab23925bbe0eff74e";

// 1. Connect to the WSS endpoint
const socket = new WebSocket("wss://stream.aisstream.io/v0/stream");

// 2. Event handler: Runs when the connection is open
socket.onopen = function () {
    console.log("WebSocket connection established. Sending subscription message...");

    // Define the subscription message with your API key
    let subscriptionMessage = {
        "APIKey": API_KEY,
        "BoundingBoxes": [[[-90, -180], [90, 180]]],
        "FilterMessageTypes": ["PositionReport"]
    };

    // Send the JSON message as a string
    socket.send(JSON.stringify(subscriptionMessage));
};

// 3. Event handler: Runs every time a new message is received
socket.onmessage = function (event) {
    let aisMessage = JSON.parse(event.data);

    // Process the data stream
    if (aisMessage["MessageType"] === "PositionReport") {
        let positionReport = aisMessage["Message"]["PositionReport"];
        let timestamp = new Date().toISOString();
        console.log(`[${timestamp}] ShipId: ${positionReport["UserID"]} Lat: ${positionReport['Latitude']} Lon: ${positionReport['Longitude']}`);
    }
};

// Event handler: Runs if there is an error
socket.onerror = function (error) {
    console.error("WebSocket Error:", error);
};

// Event handler: Runs when the connection closes
socket.onclose = function () {
    console.log("WebSocket connection closed.");
};
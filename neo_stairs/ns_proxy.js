#!/usr/bin/node
const http  = require('http');
const Blynk = require("blynk-library");

var stairsServer = new Blynk.Blynk('6d8a00fee2ac4da59e7c87721609286b');
var rgb          = new stairsServer.VirtualPin(1);

// Maps "a" to a number between 0-255 from 0-1023
function map(x) {
    var y = (x-0)/(1023-0) * (255-0) + 0;
    return (y);
}

rgb.on('write', (params) => {
    var red   = Math.round(map(params[0]));
    var green = Math.round(map(params[1]));
    var blue  = Math.round(map(params[2]));

    http.get(`http://localhost:8000/set_color?red=${red};green=${green};blue=${blue}`, (res) => {
        if (res.statusCode !== 200) {
            console.log(`GET Error [${res.statusCode}]`);
            res.resume();
            return;
        }

        res.on('end', () => {
            console.log("Successfully set the color");
        }).on('error', (err) => {
            console.log(`Error: ${e.message}`);
        });
    });
})


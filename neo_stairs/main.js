#!/usr/bin/node
const Blynk = require("blynk-library");
const spawn = require("child_process").spawn;

var stairsServer = new Blynk.Blynk('6d8a00fee2ac4da59e7c87721609286b');
var button = new stairsServer.VirtualPin(0);

button.on('write', function(params) {
    list = spawn("sudo", ["./main.py", "random"]);

    list.stdout.on("data", (data) => {
        console.log(`${data}`);
    });

    list.stderr.on("data", (data) => {
        console.log(`${data}`);
    })

    list.on("error", (err) => {
        console.log(`${err}`);
    })
});

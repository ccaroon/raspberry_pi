#!/usr/bin/node
const Blynk = require("blynk-library");
const spawn = require("child_process").spawn;

var stairsServer = new Blynk.Blynk('6d8a00fee2ac4da59e7c87721609286b');
var button       = new stairsServer.VirtualPin(0);
var rgb          = new stairsServer.VirtualPin(1);

const COMMAND = './neo_stairs.py';

// Maps "a" to a number between 0-255 from 0-1023
function map(x) {
    var y = (x-0)/(1023-0) * (255-0) + 0;
    return (y);
}

rgb.on('write', (params) => {
    var red   = Math.round(map(params[0]));
    var green = Math.round(map(params[1]));
    var blue  = Math.round(map(params[2]));
    // console.log(`Red: [${params[0]}][${red}]`);
    // console.log(`Green: [${params[1]}][${green}]`);
    // console.log(`Blue: [${params[2]}][${blue}]`);

    var cmd = spawn("sudo", [`${COMMAND}`, "rgb", `--red=${red}`, `--green=${green}`, `--blue=${blue}`]);

    cmd.stderr.on("data", (data) => {
        console.log(`${data}`);
    });

    cmd.on("error", (err) => {
        console.log(`${err}`);
    });
})


button.on('write', function(params) {
    var cmd = spawn("sudo", [`${COMMAND}`, "random"]);

    cmd.on("error", (err) => {
        console.log(`${err}`);
    });
});

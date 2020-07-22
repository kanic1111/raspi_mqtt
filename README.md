# raspi_mqtt
var mqtt = require('mqtt')
const readline = require('readline');
var client  = mqtt.connect('mqtt://192.168.43.34:1883')
const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
client.on('connect', function () {
        input.question('`which Relay you wants open (1~8) ', (answer) => {
        client.publish('arduino',  answer)
        client.end()
        input.close();
        })
})



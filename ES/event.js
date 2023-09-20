
const events = require('events')


const person = new events.EventEmitter()


person.on("hello", ()=>{
    console.log("Emitts hello");
});

person.emit("hello");


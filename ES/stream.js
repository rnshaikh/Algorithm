/*
Streams are objects that let you read data from a source or write data to a destination in continuous fashion. 
There are four types of streams

Readable − Stream which is used for read operation.
Writable − Stream which is used for write operation.
Duplex − Stream which can be used for both read and write operation.
Transform − A type of duplex stream where the output is computed based on input.
Each type of Stream is an EventEmitter instance and throws several events at different instance of times.

Example:

data − This event is fired when there is data is available to read.
end − This event is fired when there is no more data to read.
error − This event is fired when there is any error receiving or writing data.
finish − This event is fired when all the data has been flushed to underlying system.



*/

const fs = require('fs');
const { nextTick } = require('process');

let readStream = fs.createReadStream("./file.js");
readStream.setEncoding('utf-8');
let content = "";
readStream.on('data', (data)=>{
    content += data;
});
readStream.on('end', ()=>{

    console.log("data finised", content);

});
readStream.on('error', (err)=>{
    console.log("Error", err.stack)
});


let text = "//This is Text to read and write...............\n";

let writeStream = fs.createWriteStream("./test.js");
readStream.pipe(writeStream);

writeStream.write(text, 'utf-8');

writeStream.on('end', ()=>{

    console.log("Write Ended....")
})

writeStream.on('error', (err)=>{
    console.log("Error write", err.stack);
})



/// stream

const stream = require('stream');
let readable = new stream.Readable({read() {}});
let writable = new stream.Writable();

writable._write = (chunck, encoding, next)=>{
    console.log("chunk", chunck.toString());
    next();
}

readable.pipe(writable);

readable.push("Hi,,,,,,,,");
readable.push("What are you doing.");

//for read from stream
readable.on('readable', () => {
    console.log(readable.read().toString());
});



/// transform

const { Transform } = require('stream');

const transformStream = new Transform();

transformStream._transform = (chunk, encoding, next) => {
    transformStream.push(chunk.toString().toUpperCase());
    next();
  };
process.stdin.pipe(transformStream).pipe(process.stdout);



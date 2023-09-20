const fs = require('fs');


let readStream = fs.createReadStream('./oops.js');
readStream.setEncoding('utf-8');

let result = "";

readStream.on('data', (chunk)=>{
    result += chunk;
});

readStream.on('end', ()=>{
    console.log("End complete data", result);

})


console.log("Dataa", result)
let writeStream = fs.createWriteStream('./test_write.js');

writeStream.on('end', ()=>{
    console.log("write completed.");
})

readStream.pipe(writeStream)
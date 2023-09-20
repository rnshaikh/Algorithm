// function calculateCount(){

//     return new Promise((resolve, reject)=>{

//         let counter = 0;
//         for (let i = 0; i < 20_000_000_000; i++) {
//             counter++;
//         }
//         resolve(counter);

//     })


// }

const express = require("express");
const { Worker } = require("worker_threads");



let workersCreate = () =>{

    return new Promise((resolve, reject)=>{

        const worker = new Worker('./multiple-thread.js');

        worker.on('message', (data)=>{
            resolve(data);
        })

        worker.on('error', (msg)=>{
            reject(msg);
        })


    });


}

const app = express();
const port = process.env.PORT || 3000;

app.get("/non-blocking/", (req, res) => {
  res.status(200).send("This page is non-blocking");
});

app.get("/blocking", async(req, res) => {
    
    let result = await workersCreate()
    res.status(200).send(`result is ${result}`);
    // let promises = []
    // for(let i=0 ; i<1;i++){
    //     promises.push(workersCreate())
    // }
    // console.log("Promises", promises)
    // let result = await Promise.all(promises)
    // console.log("Result", result);
    // let counter = result[0] + result[1] + result[2] + result[3]
    // res.status(200).send(`result is ${result[0]}`)

    
    
    // single thread
    //let worker = new Worker('./worker-threads.js')
    // worker.on('message', (counter)=>{
    //     res.status(200).send(`result is : ${counter}`)
    // })

    // worker.on('error', (msg)=>{
    //     res.status(400).send(`error ${msg}`)
    // })

    
    
    //let counter = await calculateCount()
    //res.status(200).send(`result is ${counter}`);
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
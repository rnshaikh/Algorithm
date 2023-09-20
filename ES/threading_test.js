const express = require('express');
const {Worker} = require('worker_threads');

const app = express()
const THREAD_LIMIT = 20

const create_worker = () =>{
    return new Promise((resolve, reject)=>{
        try{
            let worker = new Worker('./worker_thread_test.js', {"workerData":{"thread": THREAD_LIMIT}});
            worker.on("message", (counter)=>{
                resolve(counter)
            });
        }
        catch(err){
            reject(err.errors)
        }
    })

}

app.get('/non-blocking', (req, res)=>{

    res.status(200).send({"msg": "nonblocking"});
})

app.get('/blocking', (req, res)=>{
    // let counter = 0
    // for(let i=0; i<=20_000_000_000;i++){
    //     counter += i
    // }
    // const worker = new Worker('./worker_thread_test.js');
    // worker.on('message', (counter)=>{
    //     res.status(200).send({"msg":`blocking, ${counter}`});
    // })
    
    let workers = [];
    let counter = 0
    for(let i=0; i<THREAD_LIMIT; i++){
        workers.push(create_worker())
    }
    console.log("WER", workers)
    Promise.all(workers).then(ans=>{
        for(let i of ans){
            counter = counter+i;
        }
        res.status(200).send({"msg":`blocking : ${counter}`})
    });
})

app.listen(3000)

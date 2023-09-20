

Nodejs:

    1) what is node js
    2) what is event-loop
    setTick vs setImmidiate()
    3) what is nodejs data type
    4) node js built in module
    5) node file io
    6) node streams
    7) node.js web module jwt
    8) callback and its limitation 
    9) promises and async and await
    10) oops and polymorphism
    11) multithrading



1) what is nodejs
    node js open source cross platform runtime environment built on chorms v8 engine. it provide single threaded,
    event-driven, non-blocking i/o for building highly scalable server side applications.

    feautre:
        Asynchronous and Event driven – All APIs of Node.js are asynchronous. This feature means that if a 
            Node receives a request for some Input/Output operation, it will execute that operation in the 
            background and continue with the processing of other requests. Thus it will not wait for the response 
            from the previous requests.

        Fast in Code execution – Node.js uses the V8 JavaScript Runtime engine, the one which is used by Google Chrome. Node has a wrapper over the JavaScript engine which makes the runtime engine much faster and hence processing of requests within Node.js also become faster.

        Single Threaded but Highly Scalable – Node.js uses a single thread model for event looping. The response from 
        these events may or may not reach the server immediately. However, this does not block other operations. 
        Thus making Node.js highly scalable. Traditional servers create limited threads to handle requests
        while Node.js creates a single thread that provides service to much larger numbers of such requests.

        Node.js library uses JavaScript – This is another important aspect of Node.js from the developer's point of view. 
        The majority of developers are already well-versed in JavaScript. Hence, development in Node.js becomes easier 
        for a developer who knows JavaScript.

        There is an Active and vibrant community for the Node.js framework – The active community always keeps the 
        framework updated with the latest trends in the web development.

        No Buffering – Node.js applications never buffer any data. They simply output the data in chunks.

2) node js event loop:
        it infinite loop which makes asynchronous processing possible in nodejs.
        this infinite loop wait for task, if there is task in call stack it exceutes then sleep until it receive more task
        this infinite loop execute task from event queue only when there is not task in call stack.
        event loop allow us to use callback and promises.

        phases of event loop:
            Timers: Callbacks scheduled by setTimeout() or setInterval() are executed in this phase.
            Pending Callbacks: I/O callbacks deferred to the next loop iteration are executed here.
            Idle, Prepare: Used internally only.
            Poll: Retrieves new I/O events.
            Check: It invokes setIntermediate() callbacks.
            Close Callbacks: It handles some close callbacks. Eg: socket.on(‘close’, …)


        when programe start all synchronous function call push into call stack and they get executed as their 
        or when it encounter asynchornous function like setTimeout or setInterval or promises it called corresponding
        node js api which offload processing to libuv thread after processing is done its call back function store in 
        micro queue or macro queue 
        micro queue store promises and macro queue event queue store setinterval and setTimeout and they call back function
        push into callstack for processing they get executed.

        Only after tasks in microTasks are completed/ excahusted, 
        event loop will next pick up one task from macroTasks. And this repeats.


        Use setImmediate if you want to queue the function behind whatever I/O event callbacks that are already in the event queue. Use process.nextTick to effectively queue the function at the head of the event queue so that it executes immediately after the current function completes.

        nextTick get executed at start of next iteration and setImmdiate is get executed at check phase of next iteration of event loop


        https://www.freecodecamp.org/news/nodejs-eventloop-tutorial/
        https://medium.com/dkatalis/eventloop-in-nodejs-macrotasks-and-microtasks-164417e619b9


3) Event driven programming
        In an event-driven application, there is generally a main loop that listens for events, and 
        then triggers a callback function when one of those events is detected.

        Although events look quite similar to callbacks, the difference lies in the fact that callback functions are 
        called when an asynchronous function returns its result, whereas event handling works on the observer pattern. 
        The functions that listen to events act as Observers. Whenever an event gets fired, its listener function starts 
        executing.

REST
Representational state transfer is a software architectural style that describes a uniform interface between physically separate components, often across the Internet in a Client-Server architecture.
https://www.redhat.com/en/topics/api/what-is-a-rest-api


4) Node js Data Type:
    it has 7 primitive data type:
    1) null
    2) undefined
    3) String
    4) Number
    5) BigInt
    6) Boolean
    7) Symbol

    it has 3 complex data type:
    1) Object
    2) Array - also object type
    3) Function- also object type
    4) Buffer -Buffer is mainly used to store binary data, while reading from a file or receiving packets over the network.

5) built in module or core module.
    1) os	Provides information about the operation system    
    2) path	To handle file paths
    3) querystring	To handle URL query strings
    4) stream	To handle streaming data
    5) util	 To access utility functions
    6) http	 To make Node.js act as an HTTP server
    7) https	To make Node.js act as an HTTPS server.
    8) events To handle events
    9) fs  To handle the file system


5) callback and its limitation

    function loadScript(src, callback) {
        let script = document.createElement('script');
        script.src = src;

        script.onload = () => callback(null, script);
        script.onerror = () => callback(new Error(`Script load error for ${src}`));

        document.head.append(script);
    }

    loadScript('/my/script.js', function(error, script) {
        if (error) {
            // handle error
        } else {
            // script loaded successfully
        }
    });

    when some asynchronous process is executing we pass second argument as callback function function which get executed 
    after processing is done 
    such kind of programmin called callback style programming.

    that’s called a “callback-based” style of asynchronous programming. A function that does something asynchronously should provide a callback argument where we put the function to run after it’s complete.

    
    But for multiple asynchronous actions that follow one after another As calls become more nested, the code becomes deeper and increasingly more difficult to manage which is call callback hell.


6) Promises :

    promises is syntactical sugar for callback functions. as name suggest it promise to executed asynchronous code and 
    gives back data or result in case of success or failure.

    promises has 3 state:
        pending, fulfilled, rejected

    
    let promise = new Promise((resolve, reject)=>{

            resolve("hello world") 

    })

    then : it is run when give promise is successfully executed return data
    promise.then((data)=>{
        console.log(data)
    }, (err)=>{
        console.log(err)
    })

    catch : catch is run when promise get reject, then we can use null in then err parameter.
    promise.catch((err)=>{
        console.log(err)
    })

    finally : get executed alwayse. it does not have any knowlegde of promise states. used for cleanup

    
    
    promise chaining:
    if we want execute asynchronous function one after other. then we can use promise chaining in promise chain. then is create and resolve promise and result is return to next then if it creats error then result is passed to next catch.

    fetch('/article/promise-chaining/user.json')
    // Load it as json
    .then(response => response.json())
    // Make a request to GitHub
    .then(user => fetch(`https://api.github.com/users/${user.name}`))
    // Load the response as json
    .then(response => response.json())
    // Show the avatar image (githubUser.avatar_url) for 3 seconds (maybe animate it)
    .then(githubUser => {
        let img = document.createElement('img');
        img.src = githubUser.avatar_url;
        img.className = "promise-avatar-example";
        document.body.append(img);

        setTimeout(() => img.remove(), 3000); // (*)
    });

    Promise API:
        1) Promise.all : takes an iterable (usually, an array of promises) and returns a new promise.
        The new promise resolves when all listed promises are resolved, and the array of their results becomes its result.
        Promise.all([
            new Promise(resolve => setTimeout(() => resolve(1), 3000)), // 1
            new Promise(resolve => setTimeout(() => resolve(2), 2000)), // 2
            new Promise(resolve => setTimeout(() => resolve(3), 1000))  // 3
            ]).then(alert) [1,2,3]

        2) Promise.allSettled just waits for all promises to settle, regardless of the result. The resulting array has:
            {status:"fulfilled", value:result} for successful responses,
            {status:"rejected", reason:error} for errors.
        
        3) Promise.race : Similar to Promise.all, but waits only for the first settled promise and gets its result (or error).

        4) Promise.any : Similar to Promise.race, but waits only for the first fulfilled promise and gets its result.
                        If all of the given promises are rejected, then the returned promise is rejected with AggregateError – a special error object that stores all promise errors in its errors property.

    Promisification:
        “Promisification” is a long word for a simple transformation. It’s the conversion of a function that accepts a callback into a function that returns a promise.
        it is done by utils.promisify() function

    Async/Await:
        it is syntactical sugar for promise.

        async function hello(){

            return
        }

        async function alwayse return promise.

        await: called async function with await it waits until promise is fullfilled.
        in async await error is catch using try and catch block

        hellow.then(data).catch(err) also in terms of promise.


let obj = {"name": "rizwan", "age":{"min": 10, "max":20}}
//let clone = JSON.parse(JSON.stringify(obj))
//let clone  = Object.assign({}, obj)
//let clone = Object.defineProperties({}, Object.getOwnPropertyDescriptors(obj))
//let clone = {...obj}
clone.age.min = 20

console.log(clone)
console.log(obj)
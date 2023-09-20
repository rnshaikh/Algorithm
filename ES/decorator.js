function dec(func){
    
    function wrapper(){
        console.log("befor function")
        func()
        console.log("after function")
    }
    
    return wrapper
}

function hello(){
    console.log("Hello")
}


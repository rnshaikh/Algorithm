
const readLine = require('readline');
const { Heap } =  require('heap-js');


let question = async(query) =>{
    return new Promise((resolve, reject)=>{
        try{
            input.question(query, resolve)
        }
        catch(err){
            reject(err);
        }
    });
}

let input = readLine.createInterface({
    input : process.stdin,
    output: process.stdout
});




class ParkingLot{

    constructor(capacity){

        this.map = {}
        this.min_heap = {}
        this.capacity = capacity
    }






}














async function main(){
    outer:while(true){
        let manager = null;
        let resp = await question(`Enter A Choice 1.Enter File Path 2.Exit`);
        resp = parseInt(resp);
        let file_name = null;
        switch(resp){
    
            case 1: file_name = await question("Enter file path:");
                    manager = new FileManager(file_name)
                    content = await manager.readSync();
                    break;

            case 2: case 2: console.log("Bye.")
                    break;

            default: console.log("invalid choice");
                    break outer;
        }
    }
    process.exit()
}
main()

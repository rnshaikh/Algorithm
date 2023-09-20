const fs = require('fs');
const readLine = require('readline');

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

let readFileAsync = function name(path) {

    return new Promise((resolve, reject)=>{

        fs.readFile(path, 'utf-8', (err, data)=>{
            if(err){
                reject(err)

            }
            else{
                resolve(data)
            }
        })

    });
}

let writeFileAsync = function name(dest, content) {

    return new Promise((resolve, reject)=>{

        fs.writeFile(dest, content, (err, data)=>{

            if(err){
                reject(err)
            }
            else{
                resolve(data)
            }

        })

    })

    
}

class FileManager{

    constructor(path){
        this.filePath = path
    }
    readSync(){

        let content = fs.readFileSync(this.filePath, 'utf-8');
        console.log("Content of given file:", content);
    }

    readAsync = async()=>{
        debugger;
        console.log("In async read function");
        let content = await readFileAsync(this.filePath, 'utf-8');
        console.log("Content of given file:", content);
    }

    writeSync(dest){
        debugger;
        let content = fs.readFileSync(this.filePath, 'utf-8')
        content = fs.writeFileSync(dest, content, 'utf-8');
        console.log("Content write file", content)

    }

    writeAsync = async(dest)=>{

        let content = fs.readFileSync(this.filePath, 'utf-8');
        let resp = await writeFileAsync(dest, content)
        console.log("Content write async file", content)

    }



}

let input = readLine.createInterface({
    input : process.stdin,
    output: process.stdout
});

async function main(){
    outer:while(true){
        let manager = null;
        let resp = await question(`Enter A Choice 1.ReadFileSync 2.ReadFileAsync 3.writeFileSync 4.writeFileAsync 5.Exit`);
        resp = parseInt(resp);
        let file_name = null;
        let dest = null;
        switch(resp){
    
            case 1: file_name = await question("Enter file path:");
                    manager = new FileManager(file_name)
                    manager.readSync();
                    break;
            case 2: file_name = await question("Enter file path:");
                    manager = new FileManager(file_name)
                    await manager.readAsync();
                    break;
            
            case 3: file_name = await question("Enter source path:");
                    dest = await question("Enter destination path:");
                    manager = new FileManager(file_name)
                    manager.writeSync(dest);
                    break;

            case 4: file_name = await question("Enter source path:");
                    dest = await question("Enter destination path:");
                    manager = new FileManager(file_name)
                    await manager.writeAsync(dest);
                    break;

            default: console.log("invalid choice");
                    break outer;
        }
    }
    process.exit()
}
main()

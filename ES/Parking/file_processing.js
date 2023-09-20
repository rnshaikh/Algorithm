const fs = require('fs');


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

    readAsync = async()=>{
        debugger;
        console.log("In async read function");
        let content = await readFileAsync(this.filePath, 'utf-8');
        console.log("Content of given file:", content);
    }
    
    writeAsync = async(dest)=>{

        let content = fs.readFileSync(this.filePath, 'utf-8');
        let resp = await writeFileAsync(dest, content)
        console.log("Content write async file", content)

    }
}

export default FileManager;
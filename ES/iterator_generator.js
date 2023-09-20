let obj = {
    initial:0,
    final : 10,
    [Symbol.iterator](){
        return {
            val: this.initial,
            final : this.final,
            next(){
                if (this.val > this.final){
                    return {
                        done:true
                    }
                    
                }
                else{

                    return {
                        done:false,
                        value: this.val++
                    }

                }
            }
        }
    }
}

function iter(n){
    return {
        val:0,
        final:n,
        next(){
            if(this.val>this.final){
                return {done:true}
            }
            else{
                return {value:this.val++, done:false}
            }
        }
    }
    
}

console.log(...obj)
let it = iter(10)
console.log(it.next())


function* gen(n){
    
    for(let i=0; i<=n ; i++){
        yield i
    }
}
let obj = gen(10)
let f = [...obj]
console.log(f)

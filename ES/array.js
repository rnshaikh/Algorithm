
// Array.

let arr = [1,2,3,4,5,6,7];
arr.slice(0,1); // from 0 to no of element return copy exclude end index
console.log("Arr slice 0 to no of element", arr.slice(0,1));

arr.slice(-3, -1); // can take negative element  
console.log("Arr slice -2  to no of element", arr.slice(-3, -1))


// splice

arr.splice(0, 2)  // delete element from start to no of element
console.log("arr splice 0 to 1 element remove", arr)

arr.splice(-2, 2) // delete element from -2 to 2 no of element
console.log("arr splice -2 to 2 element remove", arr)

arr.splice(0, 2, 10,20,30)  // delete element from start to no of element and add elements in their place.


arr.push(11,22) // arr push element at last 
console.log("arr push ele's at last", arr)

arr.pop()
console.log("arr pop ele at last", arr) // arr pop

arr.unshift(44,55) // insert new item at start
console.log("arr insert unshift ele's at first", arr)
arr.shift() // remove first item from list
console.log("arr remove shift ele at first", arr)



// objects
let varKey = "age";

let obj ={"string":1, 
          [Symbol("name")]:2,
          varKey:20}

console.log(obj)

for (let[key, val] of Object.entries(obj)){
    console.log(typeof(key))
    console.log(key, val)
}



let arr = new Array(1,2,3, 4, 5, 6,7,8,9)
arr = arr.slice(0, 9)
arr.splice(0, 1, 10)
arr.push(11)
arr.pop()
arr.unshift(11)
arr.shift()

arr.forEach((ele)=>{
    console.log("ele", ele)
})

let newA = arr.map((item, index, arr)=>{
    
    return item
})
console.log("newA", newA)

let fil = arr.filter((ele)=> ele%2 == 0)
console.log("fil", fil)

console.log("aaa", arr.indexOf(11))
console.log("aa", arr.includes(4))

let sum_a = arr.reduce((result, item)=> result+item, 0)
console.log("sum", sum_a, arr)






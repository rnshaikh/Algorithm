

class Walker {

    constructor(){

    }

    walk = () =>{
        console.log(`${this.name} can walk`)
    }
    
}

class Runner {

    constructor(){

    }

    run = () =>{
        console.log(`${this.name} can walk`)
    }

}

class Swimmer {

    constructor(){

    }

    swim = () =>{
        console.log(`${this.name} can swim`)
    }

}

let personMixin = {
    
    walk(){
        console.log(`${this.name} can walk`)
    },
    run(){
        console.log(`${this.name} can walk`)
    }
}

class Animal{

    constructor(leg){
        this.leg = leg
    }

    run = () =>{
        print("Run...")
    }

    walk = () =>{
        print("Walk....")
    }

}


class Person extends Swimmer{

    _protected = 10
    #private = 4

    constructor(name, leg){
        super()
        this.name = name
        this.leg = leg
    }

    get protected(){
        return this._protected
    }
    set protected(value){
        this._protected = value
    }

    #setprivate(value){
        this.#private = value
    }

    set private(value){
        this.#setprivate(value)
    }

    get private(){
        return this.#private
    }



    legNo = () =>{
        console.log("Man leg", this.leg)
    }
}

Object.assign(Person.prototype, personMixin);


class Whale extends Swimmer{

    constructor(name, leg){
        super()
        this.name = name
        this.leg = leg
    }

    legNo = () =>{
        console.log("Whale leg", this.leg)
    }
    
}


let whale = new Whale("Doo", 0)
let person = new Person("pero", 2)

whale.legNo()
whale.swim()

person.legNo()
person.walk()
person.run()
person.swim()
console.log("Proetected", person._protected)
console.log("private", person.private, person.private=100)







// static data memeber and memeber function.
// class Parent{

//     static len = 10

//     constructor(){
//         this.counter = 0
//     }

//     increaseCounter(){

//         if(this.counter > 10){
//             throw Error("Len is Exceeded.")
//         }
//         this.counter += 1
//         console.log("Current Counter", this.counter)

//     }

//     static initializeCounter () {
//         Parent.len = 10
//         this.counter = 0
//         console.log("initialize Counter", this.counter)
//     }

// }

// class Child extends Parent{

//     constructor(){
//         super();
//         super.increaseCounter()
//     }

// }


// let obj = new Child()

// for(let i =0 ; i< 9; i++){
//     obj.increaseCounter()
// }

// Parent.initializeCounter()

// for(let i =0 ; i< 15; i++){
//     obj.increaseCounter()
// }



// class Article {
//     constructor(title, date) {
//       this.title = title;
//       this.date = date;
//     }
  
//     static compare(articleA, articleB) {
//       return articleA.date - articleB.date;
//     }
//   }
  
//   // usage
//   let articles = [
//     new Article("HTML", new Date(2019, 1, 1)),
//     new Article("CSS", new Date(2019, 0, 1)),
//     new Article("JavaScript", new Date(2019, 11, 1))
//   ];
  
//   articles.sort(Article.compare);
  
//   alert( articles[0].title ); // CS


// class Article {
//     static publisher = "Ilya Kantor";
//   }
  
//   alert( Article.publisher ); // Ilya Kantor


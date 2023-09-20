class Mammel{
    constructor(){
        this.leg = 0
        this.hands = 0
    }
    walk(){
        
    }
    
    run(){
         
    }
}

class Person extends Mammel{
    _name = "";
    #age = 10;
    static valid = false;

    constructor(leg, hands, name){
        super()
        this._name = name
        this.leg = leg
        this.hands = hands
    }
    walk(){
        console.log("Can Walk with:", this.leg)
    }
    run(){
        console.log("Can run with", this.leg, this.hands)
    }
    set age(val){
        this.#age = val; 
    }
    get age(){
        return this.#age
    }
    static isValid(person){
        console.log("Usss", this.leg)
        if(person.age > 18){
            this.valid = true;
        }
        console.log("Is valid", this.valid)
    }
    
}

let person = new Person(2,2, "ABC")
console.log("person leg", person.leg)
console.log("person hands", person.hands)
console.log("person: name", person._name)
console.log("person: age", person.age)
person.age = 19
console.log("person: age", person.age)
person.walk()
person.run()

Person.isValid(person)

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getDetails() {
        return this.name + ' ' + this.age;
    }
}

const p = new Person('sanket', 25);
console.log(p.getDetails());
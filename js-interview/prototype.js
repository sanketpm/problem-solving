function Person(name, age) {
    this.name = 'sanket';
    this.age = 25
}

Person.prototype.details = function() {
    return  this.name + ' ' + this.age;
};

const p = new Person('Sanket', 25);
console.log((p.details)())
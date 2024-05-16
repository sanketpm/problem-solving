// fn as a assigned value
const x = () => 'hello';
console.log(x());

// fn an argument
function greet(arg) {
    console.log(x());
}
greet(x);

// fn as return value
function foo() {
    return () => 'hello';
}

var name = foo();
console.log(name(), 'sanket');
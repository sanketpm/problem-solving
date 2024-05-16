function greet() {
    const name = 'sanket';

    return function() {
        return 'hello ' + name;
    }
}

const fn = greet();
console.log(fn());

/*
The returned `inner-function` has access to the enclosing(outer) function's variables, even though the inner function is
being used outside
*/
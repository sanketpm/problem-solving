const p1 = { name: 'sanket', age: 25 }
const p2 = { name: 'sanket', age: 25 }

function print(g1, g2) {
    console.log(g1 + ' ' + g2 + ' ' + this.name + ' ')
}

const f1 = print.bind(p1)
const f2 = print.bind(p2)

f1('hello', 'hi')
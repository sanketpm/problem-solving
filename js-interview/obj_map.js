/*
const obj = {
    'str': 'check',
    $: 'check'
    1: 'check',
    [1,2]: 'check',
    {name: 'name'}: 'check',
    () => {}: 'check'
};

console.log(obj);
*/

const map = new Map();

map.set('str', 'check');
map.set(Symbol('$'), 'check');
map.set(() => {}, 'check');
map.set(123, 'check');
map.set(['arr'], 'check');
map.set({name: 'sanket'}, 'check');

console.log(map);
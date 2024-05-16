'''
An ouotward apperance that is used to conceal the less pleasant or credible reality

In simple words: It's just an encapsulation
-> It comes down to interfaces

Abstract Lower Level details that we dont want to worry about
It's more like a good programming technique rather then call it a pattern
eg:
Http Clients
```
fetch('http://example.com/file.json')
    .then( (response) => response.json() )
    .then( (data) => console.log(data) )
```
'''


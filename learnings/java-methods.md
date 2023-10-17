## Map
**- Map.putIfAbsent(key, value)**

Before:
```
if( !map.containsKey(key) ) {
    map.put(key, value);
}
```
Now:
```
map.putIfAbsent(key, value);
```


**- Map.setOrDefault(key, value)**
Before:
```
 Map<Integer, String> map = new HashMap<>();

if( map.containsKey(1) ) {
    return map.get(1);
} else {
    map.put(1, 'sanket');
    return map.get(1);
}

OUTPUT:
'sanket'
```

AFTER:
```
Map<Integer, String> map = new HashMap<>();
map.put(1, "supreet");

System.out.println(map.getOrDefault(1, "sanket"));

OUTPUT:
supreet

==========================================================

Map<Integer, String> map = new HashMap<>();

System.out.println(map.getOrDefault(1, "sanket"));

OUTPUT:
sanket

```


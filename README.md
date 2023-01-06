# SSON

Super Simple Object Notation.

## Notation

This is the notation for one SSON file:

MyObjects.SSON

```
obj_name{
  asset1:value
  asset2:value
  asset3:value
}
another_obj{
  sub_obj{
  sub_asset1:value
  }
  asset:sub_obj.sub_asset1
}
```

This is what it would look like in JSON:

MyObject.JSON

```js
{
  asset1: value
  asset2: value
  asset3: value
}
```
```js
{
  sub_obj
  {
  sub_asset1: value
  }
}

```
# python cheetsheet


## list


<br>
<br>

## dict

- 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워짐

- 키로 접근하여 값 변경할 수 있음

<br>

### 선언 

선언시 빈 중괄호 `{}` 혹은 `dict()` 함수 사용

```python
>>> e = {}
>>> type(e)
<class 'dict'>
>>> f = dict()
>>> type(f)
<class 'dict'>
```

<br>

### 수정

키로 접근하여 값을 할당
```python
>>> d = {'abc' : 1, 'def' : 2}
>>> d['abc'] = 5
>>> d
{'abc': 5, 'def': 2}
```

<br>

### for 문과의 활용
- `key`

for 문을 통해 dict를 순회하면, key 값이 할당됨(단, 순서 개념이 없어 __임의의 순서__로 할당!)

```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
```

- `value`

`values()` 를 사용하면 value 값으로 for 문을 순회 가능

```python
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30    
```


- `key & value`

`items()` 를 사용하면 key, value 값으로 for 문을 순회 가능

```python
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30
```

<br>

### 특정 key가 존재하는가?

`in` 사용

```python
>>> 'alice' in a
True
>>> 'teacher' in a
False
>>> 'teacher' not in a
True
```

<br>

<br>
<br>
<br>
<br>


```python
```


<br>
<br>
<br>
<br>

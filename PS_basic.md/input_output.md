# PS 기초 학습 (Python) : 입출력

<br/>

## 출력

<br/>

### 문장 출력

- python3에서 문장을 출력 시, 큰 따옴표나 작은 따옴표 아무거나 사용해도 된다.

```python
print("Hello World")
```

<br/>

### 문자열레 특수 문자를 포함시켜 출력하기

- 특수 문자 앞에 <code>\\</code>를 붙여주면 이를 기호가 아닌 문자로 인식한다.  
  (자주 사용하는 방법이므로 기억하자)

```python
print("Let\'s do it")
```

<br/>

- <code>"</code>,<code>'</code>를 포함시킬 때, <code>"""</code> 또는 <code>'''</code>로 전체 문장을 감싸는 방법도 있다.

```python
print('''Let's do it''')
```

▼ 출력 결과

```
Let's do it
```

<br/>

### 2줄 출력 (print 함수 한 번만 사용)

- <code>\n</code>문자를 이용한다. (new line을 의미하는 특수 문자)

```python
print("Hello World\nNice to meet you")
```

▼ 출력 결과

```
Hello World
Nice to meet you
```

<br/>

- <code>"""</code> 또는 <code>'''</code>을 사용해도 된다.

```python
print("""Hello World
Nice to meet you""")
```

▼ 출력 결과

```
Hello World
Nice to meet you
```

<br/>

### 공백을 사이에 두고 출력

- print 함수에 2개의 값을 <code>,</code>를 사이에 두고 넣어준다.

```python
print(1, 2)
```

▼ 출력 결과

```
1 2
```

<br/>

- 구분자를 <code>sep</code>를 이용하여 직접 설정할 수 있다.

```python
print(1, 2, sep=" ")
print(1, 2, sep=",")
print(1, 2, sep="/")
```

▼ 출력 결과

```
1 2
1,2
1/2
```

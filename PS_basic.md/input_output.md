# PS 기초 학습 (Python) : 입출력

## 기본 출력

<br/>

### 문장 출력

- python3에서 문장을 출력 시, 큰 따옴표나 작은 따옴표 아무거나 사용해도 된다.

```python
print("Hello World")
```

<br/>

### 문자열에 특수 문자를 포함시켜 출력

- 특수 문자 앞에 <code>\\</code>를 붙여주면, 이를 기호가 아닌 문자로 인식한다.

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

### 두 값을 공백을 두고 출력

- print 함수에 2개의 값을 <code>,</code>를 사이에 두고 넣어준다.

```python
print(1, 2)
```

▼ 출력 결과

```
1 2
```

<br/>

- <code>,</code> 사용 시 구분자로 쓸 값을 <strong>sep</strong>를 이용하여 직접 설정할 수 있다.

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

<br/>

- print 함수는 end라는 값에 <code>\n</code> 문자가 기본적으로 들어가 있기 때문에, 다음 줄로 알아서 넘어간다.

* 이 end값을 공백 <code>' '</code>으로 바꾸면 print 함수 2개로 공백을 두고 출력할 수 있다.

```python
print(1, end=" ")
print(2)
```

▼ 출력 결과

```
1 2
```

<br/>

## 변수와 자료형

<br/>

### 변수를 이용한 출력

- 변수를 선언하고 정수값을 넣은 후 출력할 수 있다.

* 2개 이상의 변수를 한 줄에 동시에 선언할 수 있다.

* 변수끼리 사칙연산이 가능하다. (정수형, 실수형끼리만)

```python
a = 1
b, c = 2, 3
d = b + c
print("a =", a)
print("d =", d)
```

▼ 출력 결과

```
a = 1
d = 5
```

<br/>

- 변수의 이름은 다르게 정할 수 있고, 문자열이나 실수도 담을 수 있다.

```python
dummy = "toy"
temp = 3.141592653
```

<br/>

- print() 함수에 type()을 사용하면 해당 변수의 자료형을 확인할 수 있다.

```python
dummy = "toy"
temp = 3.141592653
print(type(dummy))  # <class 'str'>
print(type(temp))  # <class 'float'>
```

<br/>

### 코딩 컨벤션

- 일반적으로 변수나 함수명은 소문자로 쓰는 것이 원칙이며, 띄어쓰기가 필요할 경우 언더바 (Underscore)를 사용한다.

- 이와 같은 일종의 코드 작성 규약을 <strong>"코딩 컨벤션 (Coding Convention)"</strong>이라 한다.

* 코딩 컨벤션은 협업을 위한 일종의 약속으로, 각 언어나 회사에 따라 정의해 놓은 코딩 컨벤션은 다양하다.

<br/>

## 출력 형식

<br/>

### 1. 변수 포멧 (%d, %s, ...)과 % 이용

<br/>

### 2. format 함수 이용

<br/>

### 3. f 문자영 포멧 이용

<br/>
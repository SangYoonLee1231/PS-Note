## <a href="https://programmers.co.kr/learn/courses/30/lessons/12951">JadenCase 문자열 만들기</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-14

<br/>

```js
function solution(s) {
  const arrayS = s.split(" ");

  for (let i = 0; i < arrayS.length; i++) {
    arrayS[i] = arrayS[i].split("");

    for (let j = 0; j < arrayS[i].length; j++) {
      if (arrayS[i][j].match(new RegExp(/^[0-9]/))) {
        continue;
      }
      if (j === 0) {
        arrayS[i][j] = arrayS[i][j].toUpperCase();
      } else {
        arrayS[i][j] = arrayS[i][j].toLowerCase();
      }
    }

    arrayS[i] = arrayS[i].join("");
  }

  return arrayS.join(" ");
}
```

<br/>

#### 풀이 로직

- 문자열을 공백에 따라 나눠 배열로 변환한 후, 각 배열의 요소를 순회하여 첫 문자는 대문자로, 나머지 문자는 소문자로 바꿔준다.

- 배열 요소 탐색 시, 해당 문자가 숫자인지 우선적으로 확인하고, 이 경우는 문자 바꾸기 작업을 생략한다.

<br/>

#### 느낀점

- 처음에 배열 메소드를 사용하여 풀었으나, 코드가 너무 복잡해졌고 고치기에도 까다로워져 결국 다 지우고 반복문만으로 다시 풀었다.

- 숫자 처리를 같이 해줘야 하는 것이 까다로웠다. 덕분에 이를 우선적으로 처리하는 것이 좋겠다는 걸 생각해낼 수 있었다.

- 생각보다 푸는데 오래 걸린 문제였다. 문제 조건 하나를 놓친 것도 있었고 배열 메소드를 이중으로 사용하다 보니 코드를 치면서 많이 헷갈리기도 했다.

- 또한 한 번도 써보지 않았던 정규 표현식과 <code>match()</code> 메소드를 처음으로 써봤다. 좋은 경험이었다.

## <a href="https://programmers.co.kr/learn/courses/30/lessons/68645">삼각 달팽이</a>

### 풀이 1 (Python)

- 풀이한 날짜 : 2023-01-05

<br/>

```js
function solution(n) {
  let grid = new Array(n).fill(0);
  let answer = [];

  for (let i = 0; i < n; i++) {
    grid[i] = new Array(i + 1).fill(0);
  }

  grid = fill_grid(grid, n);

  for (let i in grid) {
    for (let j in grid[i]) {
      answer.push(grid[i][j]);
    }
  }

  return answer;
}

function fill_grid(grid, n) {
  let [x, y] = [0, 0];
  let [dx, dy] = [
    [1, 0, -1],
    [0, 1, -1],
  ];
  let total_num = (n * (n + 1)) / 2;
  let direction = 0;

  for (let i = 1; i <= total_num; i++) {
    grid[x][y] = i;

    let [nx, ny] = [x + dx[direction], y + dy[direction]];
    if (!in_range(nx, ny, n) || grid[nx][ny] !== 0) {
      direction = (direction + 1) % 3;
      [x, y] = [x + dx[direction], y + dy[direction]];
    } else {
      [x, y] = [nx, ny];
    }
  }

  return grid;
}

function in_range(x, y, n) {
  return x < n && y <= x ? true : false;
}
```

<br/>

#### 풀이 방법

- 2차원 격자에 dx, dy 테크닉을 이용하여 숫자를 순서대로 채워넣는 방식으로 문제를 해결하였다.

<br/>

#### 느낀점

- 시간 제한을 두고 풀었던 문제로, 해결하는 데 58분 정도 걸렸다.

- JS에서 2차원 배열 초기화 하는 방법, 범위 조건 따지기 등등 시간을 잡아먹었던 부분이 있었다. 아직 문제 풀이 연습이 더 많이 필요한 것 같다.

- 그래도 쉽지 않았던 문제를 시간 내에 풀 수 있어서 뿌듯하다.

<br/><br/>

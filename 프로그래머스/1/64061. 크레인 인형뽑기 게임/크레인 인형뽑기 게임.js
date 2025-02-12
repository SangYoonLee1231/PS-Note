function solution(board, moves) {
    const size = board.length;
    const basket = [];
    
    return moves.reduce((answer, move) => {
        answer += move_to_basket(board, basket, move - 1, size);
        return answer;
    }, 0)
}

function check_if_blow(basket) {
    if (basket.length >= 2 && basket.at(-1) === basket.at(-2)) {
        basket.pop();
        basket.pop();
        return 2;
    }
    return 0;
}

function move_to_basket(board, basket, move, size) {
    for (let i = 0; i < size; i++) {
        if (board[i][move]) {
            basket.push(board[i][move]);
            board[i][move] = 0;
            return check_if_blow(basket);
        }
    }
    return 0;
}



// board[row][col] -> row: 1->size, col: move
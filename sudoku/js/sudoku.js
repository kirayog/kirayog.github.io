const form = document.getElementById("form");
const output = document.getElementById("output");

count = 0;

//submitが押されたときの処理
//inputtypeがtextのフォームを全て取得し、listに格納している
form.onsubmit = function (event) {
    event.preventDefault();
    const numbers = form.number;
    for (let i = 0; i < numbers.length; i++) {
        plain[Math.floor(i / 9)][i % 9] = 0;
        if (numbers[i].value != "") {
            plain[Math.floor(i / 9)][i % 9] = +numbers[i].value;
        }
    }
    //output.innerHTML = plain + "が入力されました。";

    const startTime = performance.now(); //開始時間

    const sudoku = plain;
    const usd = createUsd(sudoku);
    const nextPoint = serchNextPoint(sudoku, usd);
    dfs(0, sudoku, usd, nextPoint);
    console.log(count);

    const endTime = performance.now(); //終了時間
    const time = Math.floor((endTime - startTime) * Math.pow(10, 2)) / Math.pow(10, 2);
    output.innerHTML = "計算時間：" + time + "ミリ秒"; //何ミリ秒かかったかを表示する
};

//マスの状況は9行9列の二重配列で管理する
//未入力のマスは0
const plain = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

//数独のルールに反していないかを調べる関数
//ルール通りならtrue、間違っていればfalseを返す
function ck(cnt, s) {
    const x = Math.floor(cnt / 9); //引数のsを(x,y)座標に変換する
    const y = cnt % 9;
    const duplistX = [false, false, false, false, false, false, false, false, false, false]; //横方向で調べる
    const duplistY = [false, false, false, false, false, false, false, false, false, false]; //縦方向で調べる
    const duplistK = [false, false, false, false, false, false, false, false, false, false]; //3×3のマスで調べる
    for (let i = 0; i < 9; i++) {
        if (s[x][i] != 0 && duplistX[s[x][i]] == true) return false; //横方向で調べる
        else duplistX[s[x][i]] = true;
        if (s[i][y] != 0 && duplistY[s[i][y]] == true) return false; //縦方向で調べる
        else duplistY[s[i][y]] = true;
        if (s[Math.floor(x / 3) * 3 + Math.floor(i / 3)][Math.floor(y / 3) * 3 + i % 3] != 0 &&
            duplistK[s[Math.floor(x / 3) * 3 + Math.floor(i / 3)][Math.floor(y / 3) * 3 + i % 3]] == true) return false; //3×3のマスで調べる
        else duplistK[s[Math.floor(x / 3) * 3 + Math.floor(i / 3)][Math.floor(y / 3) * 3 + i % 3]] = true;
    }
    return true;
}


//入力された数独の答えを探索する関数
//深さ優先探索で行うため、再帰関数を使用する
// function dfs(cnt, s) { //cnt:何マス目まで調べられたか(0~81)、s:数独の盤面の配列を入れる(9×9の二重配列)
//     if (cnt == 81) { //計算結果を出力する関数を呼び出す予定
//         for (let i = 0; i < 9; i++) {
//             console.log(s[i]);
//         }
//         /*let str = "<table border='1'>";//新しく表を作る場合
//         for (let i = 0; i < 9; i++) {
//             str += "<tr>";
//             for (let j = 0; j < 9; j++) {
//                 str += "<td>" + s[i][j] + "</td>";
//             }
//             str += "</tr>";
//         }
//         str += "</table>"
//         output.innerHTML = str;*/
//         let numbers = form.number;//フォームに値を入力する
//         for (let i = 0; i < numbers.length; i++) {
//             numbers[i].value = s[Math.floor(i / 9)][i % 9];
//         }
//         return true;
//     }
//     const x = Math.floor(cnt / 9); //引数のcntを(x,y)座標に変換する
//     const y = cnt % 9;
//     if (s[x][y] != 0) { //元から数字が入っているマスは無条件で次のマスへ進む
//         if (dfs(cnt + 1, s) == true) return true;
//     } else {
//         for (let i = 0; i < 9; i++) { //iを変えながら一つ一つ数字を入れてみる
//             s[x][y] = i + 1;
//             if (ck(cnt, s) == true) { //入れた結果、数独のルールに反していなかったら次のマスへ進む
//                 if (dfs(cnt + 1, s) == true) return true;
//             }
//         }
//         s[x][y] = 0; //試した数字が入ったままなのでリセットする
//     }
//     return false; //どの数字も入らなかった場合は一つ前のマスへ戻る
// }

function createUsd(s) { //dfsで使うusdを作成するための関数
    const usd = new Array(9);
    for (let i = 0; i < 9; i++) { //usdをfalseで初期化(trueで使用済み、falseで未使用)
        usd[i] = new Array(9);
        for (let j = 0; j < 9; j++) {
            usd[i][j] = new Array(9);
            for (let k = 0; k < 9; k++) {
                usd[i][j][k] = false;
            }
        }
    }
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const n = s[i][j];
            if (n != 0) {
                for (let k = 0; k < 9; k++) {
                    usd[i][k][n - 1] = true; //x方向にtrueで埋める
                    usd[k][j][n - 1] = true; //y方向にtrueで埋める
                    usd[Math.floor(i / 3) * 3 + Math.floor(k / 3)][Math.floor(j / 3) * 3 + k % 3][n - 1] = true; //3×3のマスをtrueで埋める
                    usd[i][j][k] = true; //数字が入っているマスには数字が確実に入らないのでtrueで埋める
                }
            }
        }
    }
    return usd;
}

//dfs内で次に探索する箇所、nextPointを探す関数
//入る数字の候補が最も少ないマスを配列で返す
function serchNextPoint(s, usd) {
    let nextPoint = null;
    let minCnt = 10;
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (s[i][j] == 0) {
                let cnt = 0;
                for (let k = 0; k < 9; k++) {
                    if (usd[i][j][k] == false) cnt++;
                }
                if (cnt < minCnt && cnt != 0) {
                    minCnt = cnt;
                    nextPoint = [i, j];
                }
            }
        }
    }
    return nextPoint;
}

//usdを更新する関数
function updateUsd(usd, i, j, n) {
    const newUsd = new Array(9);
    for (let i = 0; i < 9; i++) {
        newUsd[i] = new Array(9);
        for (let j = 0; j < 9; j++) {
            newUsd[i][j] = new Array(9);
            for (let k = 0; k < 9; k++) {
                if (usd[i][j][k] == true) {
                    newUsd[i][j][k] = true;
                } else {
                    newUsd[i][j][k] = false;
                }
            }
        }
    }
    // const newUsd = usd.concat(); //参照渡しになる
    // const newUsd = JSON.parse(JSON.stringify(usd)) //4倍かかる
    for (let k = 0; k < 9; k++) {
        newUsd[i][k][n - 1] = true; //x方向にtrueで埋める
        newUsd[k][j][n - 1] = true; //y方向にtrueで埋める
        newUsd[Math.floor(i / 3) * 3 + Math.floor(k / 3)][Math.floor(j / 3) * 3 + k % 3][n - 1] = true; //3×3のマスをtrueで埋める
        newUsd[i][j][k] = true; //数字が入っているマスには数字が確実に入らないのでtrueで埋める
    }
    return newUsd;
}

function outPut(s) {
    for (let i = 0; i < 9; i++) {
        if (s[i].includes(0) == true) {
            return false;
        }
    }
    for (let i = 0; i < 9; i++) {
        console.log(s[i]);
    }
    /*let str = "<table border='1'>";//新しく表を作る場合
    for (let i = 0; i < 9; i++) {
        str += "<tr>";
        for (let j = 0; j < 9; j++) {
            str += "<td>" + s[i][j] + "</td>";
        }
        str += "</tr>";
    }
    str += "</table>"
    output.innerHTML = str;*/
    let numbers = form.number;//フォームに値を入力する
    for (let i = 0; i < numbers.length; i++) {
        numbers[i].value = s[Math.floor(i / 9)][i % 9];
    }
    return true;
}

function dfs(cnt, s, usd, nextPoint) { //usd:使われた数字を記録する配列(9×9×9の三重配列)
    if (nextPoint == null) { //計算結果を出力する関数を呼び出す予定
        return outPut(s);
    }

    const x = nextPoint[0]; //引数のcntを(x,y)座標に変換する
    const y = nextPoint[1];
    for (let i = 0; i < 9; i++) { //iを変えながら一つ一つ数字を入れてみる
        if (usd[x][y][i] == false) {
            s[x][y] = i + 1;
            const newUsd = updateUsd(usd, x, y, i + 1);
            const nextPoint = serchNextPoint(s, usd);//newUsdじゃないのになんで速い？？？？
            count++;
            if (dfs(cnt + 1, s, newUsd, nextPoint) == true) {
                return true;
            }
        }
    }

    s[x][y] = 0; //試した数字が入ったままなのでリセットする
    return false; //どの数字も入らなかった場合は一つ前のマスへ戻る
}
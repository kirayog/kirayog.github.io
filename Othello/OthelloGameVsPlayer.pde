int tileLength = 40;//タイルの一辺の長さ
int leftGap = 40;//盤面の左の隙間
int upperGap = 40;//盤面の上の隙間

int[][] eightDirectionArray = {{-1,  0},
                               {-1,  1},
                               { 0,  1},
                               { 1,  1},
                               { 1,  0},
                               { 1, -1},
                               { 0, -1},
                               {-1, -1}};//八方向

int[][] tileColorArray = {{0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 1, 2, 0, 0, 0},
                          {0, 0, 0, 2, 1, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0}};//0で緑、1で白、2で黒
                          
int[][] tileScore = {{120, -20, 20,  5,  5, 20, -20, 120}, 
                     {-20, -40, -5, -5, -5, -5, -40, -20}, 
                     { 20,  -5, 15,  3,  3, 15,  -5,  20}, 
                     {  5,  -5,  3,  3,  3,  3,  -5,   5}, 
                     {  5,  -5,  3,  3,  3,  3,  -5,   5}, 
                     { 20,  -5, 15,  3,  3, 15,  -5,  20}, 
                     {-20, -40, -5, -5, -5, -5, -40, -20}, 
                     {120, -20, 20,  5,  5, 20, -20, 120}};
                          
int whiteTileCount;
int blackTileCount;

boolean playerTurn = true;//trueで白のターン、falseで黒のターン
boolean reversedTile = false;//trueで一回以上ひっくり返した、falseで一回もひっくり返してない
                               
ArrayList<Integer> reversibleTilePosX = new ArrayList<Integer>();
ArrayList<Integer> reversibleTilePosY = new ArrayList<Integer>();

ArrayList<Tile> puttableTileArray = new ArrayList<Tile>();

Tile[][] tileArray = new Tile[8][8];
Tile[][] tmpTileArray = new Tile[8][8];//現在のマスの状況を一時的に保存する

Tile bestScoreTile;

void setup(){
  size(600, 400);
  PFont font = createFont("Meiryo", 30);
  textFont(font);
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      tileArray[i][j] = new Tile(leftGap + tileLength * i, 
                                  upperGap + tileLength * j, 
                                  i, 
                                  j);
    }
  }
  fieldUpdate();
  textUpdate();
}

void draw(){
  
}

void mousePressed(){
  if(mouseX > leftGap &&
     mouseX < (leftGap + tileLength * 8) &&
     mouseY > upperGap &&
     mouseY < (upperGap + tileLength * 8)){
       gameDirector(mouseX, mouseY);
  }
}

void gameDirector(int mousePosX, int mousePosY){
  Tile tile = clickedTileCheck(mousePosX, mousePosY);
  if(puttableTileCheck(tile, tileColorArray)){
    putTile(tile);
    playerTurn = !playerTurn;
    background(204);
    fieldUpdate();
    tileCount();
    turnSkipCheck();
    if(playerTurn == false){
      putTile(enemyPutTile());
//      minimax(tileColorArray, 2);
//      putTile(bestScoreTile);
      playerTurn = !playerTurn;
      background(204);
      fieldUpdate();
      tileCount();
      turnSkipCheck();
    }
  }
}  

void fieldUpdate(){
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      fill(0, 180, 0);
      rect(tileArray[i][j].upperLeftPositionX, tileArray[i][j].upperLeftPositionY, 
           tileLength, tileLength);
      if(tileColorArray[i][j] == 1){
        fill(255);
        ellipse(tileArray[i][j].upperLeftPositionX + tileLength/2,
                tileArray[i][j].upperLeftPositionY + tileLength/2,
                tileLength, 
                tileLength);
      }else if(tileColorArray[i][j] == 2){
        fill(0);
        ellipse(tileArray[i][j].upperLeftPositionX + tileLength/2,
                tileArray[i][j].upperLeftPositionY + tileLength/2,
                tileLength, 
                tileLength);
      }
    }
  }
}

Tile clickedTileCheck(int mousePosX, int mousePosY){
  
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(mousePosX >= tileArray[i][j].upperLeftPositionX &&
         mousePosX <= tileArray[i][j].upperLeftPositionX + tileLength &&
         mousePosY >= tileArray[i][j].upperLeftPositionY &&
         mousePosY <= tileArray[i][j].upperLeftPositionY + tileLength){
           return tileArray[i][j];
      }
    }
  }
  return tileArray[0][0];
}

boolean puttableTileCheck(Tile tile, int[][] tileColorArray){
  
  int playerColor;
  int enemyColor;
  int boardColor;
  
  if(playerTurn){
    boardColor = 0;
    playerColor = 1;
    enemyColor = 2;
  }else{
    boardColor = 0;
    playerColor = 2;
    enemyColor = 1;
  }
  
  if(tileColorArray[tile.tileNumberX][tile.tileNumberY] != boardColor){
    return false;
  }
  
  for(int i = 0; i < eightDirectionArray.length; i++){
    if(tile.tileNumberX + eightDirectionArray[i][0] < 0 ||
       tile.tileNumberX + eightDirectionArray[i][0] > 7 ||
       tile.tileNumberY + eightDirectionArray[i][1] < 0 ||
       tile.tileNumberY + eightDirectionArray[i][1] > 7 ){
      continue;
    }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == playerColor ||
             tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == boardColor){
      continue;
    }
    
    int moveCount = 1;
    
    while(true){
      if(tile.tileNumberX + eightDirectionArray[i][0] * moveCount < 0 ||
         tile.tileNumberX + eightDirectionArray[i][0] * moveCount > 7 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount < 0 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount > 7){
        break;
      }
      
      if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                       [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == enemyColor){
        moveCount++;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == boardColor){
        break;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == playerColor){
        reversedTile = true;
        break;
      }
    }
  }
  if(reversedTile){
    reversedTile = false;
    return true;
  }else{
    return false;
  }
}

void putTile(Tile tile){
  if(playerTurn){
    tileColorArray[tile.tileNumberX][tile.tileNumberY] = 1;
  }else{
    tileColorArray[tile.tileNumberX][tile.tileNumberY] = 2;
  }
  
  int playerColor;
  int enemyColor;
  int boardColor;
  
  if(playerTurn){
    boardColor = 0;
    playerColor = 1;
    enemyColor = 2;
  }else{
    boardColor = 0;
    playerColor = 2;
    enemyColor = 1;
  }
  
  for(int i = 0; i < eightDirectionArray.length; i++){
    if(tile.tileNumberX + eightDirectionArray[i][0] < 0 ||
       tile.tileNumberX + eightDirectionArray[i][0] > 7 ||
       tile.tileNumberY + eightDirectionArray[i][1] < 0 ||
       tile.tileNumberY + eightDirectionArray[i][1] > 7 ){
      continue;
    }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == playerColor ||
             tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == boardColor){
      continue;
    }
    
    int moveCount = 1;
    
    while(true){
      if(tile.tileNumberX + eightDirectionArray[i][0] * moveCount < 0 ||
         tile.tileNumberX + eightDirectionArray[i][0] * moveCount > 7 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount < 0 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount > 7){
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }
      
      if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                       [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == enemyColor){
        reversibleTilePosX.add(tile.tileNumberX + eightDirectionArray[i][0] * moveCount);
        reversibleTilePosY.add(tile.tileNumberY + eightDirectionArray[i][1] * moveCount);
        moveCount++;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == boardColor){
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == playerColor){
        for(int j = 0; j < reversibleTilePosX.size(); j++){
          tileColorArray[reversibleTilePosX.get(j)][reversibleTilePosY.get(j)] = playerColor;
        }
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }
    }
  }
}

void tileCount(){
  
  whiteTileCount = 0;
  blackTileCount = 0;
  
  for(int i = 0; i < tileColorArray.length; i++){
    for(int j = 0; j < tileColorArray[0].length; j++){
      if(tileColorArray[i][j] == 1){
        whiteTileCount++;
      }else if(tileColorArray[i][j] == 2){
        blackTileCount++;
      }
    }
  }
}

boolean endCheck(){ //trueで続行、falseで終了
  
  tileCount();
  
  if(whiteTileCount + blackTileCount == 64){
    if(whiteTileCount > blackTileCount){
      text("白の勝ち", 400, 100);
    }else if(whiteTileCount < blackTileCount){
      text("黒の勝ち", 400, 100);
    }else if(whiteTileCount == blackTileCount){
      text("引き分け", 400, 100);
    }
    return false;
  }
  
  if(whiteTileCount == 0){
    text("黒の勝ち", 400, 100);
    return false;
  }else if(blackTileCount == 0){
    text("白の勝ち", 400, 100);
    return false;
  }
  
  return true;
}

void textUpdate(){
  
  tileCount();
  
  fill(0);
  textSize(30);
  if(endCheck() == true){
    if(playerTurn){
      text("白のターン", 400, 100);
    }else{
      text("黒のターン", 400, 100);
    }
  }
  text("白：" + whiteTileCount + "枚\n" +
       "黒：" + blackTileCount + "枚", 400, 200);
}

void turnSkipCheck(){
  if(allPuttableTileCheck() == false){
    playerTurn = !playerTurn;
    textUpdate(); 
    if(allPuttableTileCheck() == false){
      if(whiteTileCount > blackTileCount){
        text("白の勝ち", 400, 100);
      }else if(whiteTileCount < blackTileCount){
        text("黒の勝ち", 400, 100);
      }else if(whiteTileCount == blackTileCount){
        text("引き分け", 400, 100);
      }
      text("白：" + whiteTileCount + "枚\n" +
           "黒：" + blackTileCount + "枚", 400, 200);
    }
  }else{
    textUpdate(); 
  }
}

boolean allPuttableTileCheck(){
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(puttableTileCheck(tileArray[i][j], tileColorArray)){
        return true;
      }
    }
  }
  return false;
}

Tile enemyPutTile(){
  int maxScore = -10000;
  Tile maxScoreTile = tileArray[0][0];
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      tmpTileArray[i][j] = tileArray[i][j];
    }
  }
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(puttableTileCheck(tileArray[i][j], tileColorArray)){
        if(scoreCheck(tileArray[i][j]) > maxScore){
          maxScore = scoreCheck(tileArray[i][j]);
          maxScoreTile = tileArray[i][j];
        }
      }
    }
  }
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      tileArray[i][j] = tmpTileArray[i][j];
    }
  }
  return maxScoreTile;
}

/*
int minimax(int[][] tColorArray, int depth){
  
  int bestScore = 0;
  bestScoreTile = tileArray[0][0];
  
  if(depth == 0){
    return allScoreCheck(tColorArray);
  }
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(puttableTileCheck(tileArray[i][j], tColorArray)){//puttableTileCheckの引数に盤面を追加する
        int minimax = minimax(tColorArray, depth - 1);
        if(depth % 2 == 0 && minimax > bestScore){//深度が偶数でmaxを求める
          bestScore = minimax;
          bestScoreTile = tileArray[i][j];
        }
        if(depth % 2 == 1 && minimax < bestScore){//奇数でminを求める
          bestScore = minimax;
          bestScoreTile = tileArray[i][j];
        }
      }
    }
  }
  return bestScore;
}
*/

int scoreCheck(Tile tile){
  
  int score = 0;
  int playerColor;
  int enemyColor;
  int boardColor;
  
  if(playerTurn){
    boardColor = 0;
    playerColor = 1;
    enemyColor = 2;
  }else{
    boardColor = 0;
    playerColor = 2;
    enemyColor = 1;
  }
  
  for(int i = 0; i < eightDirectionArray.length; i++){
    if(tile.tileNumberX + eightDirectionArray[i][0] < 0 ||
       tile.tileNumberX + eightDirectionArray[i][0] > 7 ||
       tile.tileNumberY + eightDirectionArray[i][1] < 0 ||
       tile.tileNumberY + eightDirectionArray[i][1] > 7 ){
      continue;
    }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == playerColor ||
             tileColorArray[tile.tileNumberX + eightDirectionArray[i][0]]
                           [tile.tileNumberY + eightDirectionArray[i][1]] == boardColor){
      continue;
    }
    
    int moveCount = 1;
    
    while(true){
      if(tile.tileNumberX + eightDirectionArray[i][0] * moveCount < 0 ||
         tile.tileNumberX + eightDirectionArray[i][0] * moveCount > 7 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount < 0 ||
         tile.tileNumberY + eightDirectionArray[i][1] * moveCount > 7){
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }
      
      if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                       [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == enemyColor){
        reversibleTilePosX.add(tile.tileNumberX + eightDirectionArray[i][0] * moveCount);
        reversibleTilePosY.add(tile.tileNumberY + eightDirectionArray[i][1] * moveCount);
        moveCount++;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == boardColor){
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }else if(tileColorArray[tile.tileNumberX + eightDirectionArray[i][0] * moveCount]
                             [tile.tileNumberY + eightDirectionArray[i][1] * moveCount] == playerColor){
        score += tileScore[tile.tileNumberX][tile.tileNumberY];
        for(int j = 0; j < reversibleTilePosX.size(); j++){
          score += tileScore[reversibleTilePosX.get(j)][reversibleTilePosY.get(j)];
        }
        reversibleTilePosX.clear();
        reversibleTilePosY.clear();
        break;
      }
    }
  }
  return score;
}

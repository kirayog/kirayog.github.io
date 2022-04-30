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
                          
int whiteTileCount;
int blackTileCount;

boolean playerTurn = true;//trueで白のターン、falseで黒のターン
boolean reversedTile = false;//trueで一回以上ひっくり返した、falseで一回もひっくり返してない
                               
ArrayList<Integer> reversibleTilePosX = new ArrayList<Integer>();
ArrayList<Integer> reversibleTilePosY = new ArrayList<Integer>();

Tile[][] tileArray = new Tile[8][8];

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
  if(puttableTileCheck(tile)){
    putTile(tile);
    playerTurn = !playerTurn;
    background(204);
    fieldUpdate();
    tileCount();
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

boolean puttableTileCheck(Tile tile){
  
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

boolean allPuttableTileCheck(){
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(puttableTileCheck(tileArray[i][j])){
        return true;
      }
    }
  }
  return false;
}

int maxlevel(int limit){//https://www.webcyou.com/?p=6997

  if(limit == 0){
    return 0;//この手の最終評価値を入れる
  }
  
  int score = -100;
  int score_max = -100;
  
  for(int i = 0; i < tileColorArray.length; i++){
    for(int j = 0; j < tileColorArray[0].length; j++){
      if(puttableTileCheck(tileArray[i][j])){
        score = minlevel(limit - 1);
      }
    }
  }
  return score_max;
}

int minlevel(int limit){
  return 0;
}

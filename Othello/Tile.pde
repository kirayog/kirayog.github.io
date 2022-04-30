class Tile{
  
  int upperLeftPositionX;//タイルの左上のX座標
  int upperLeftPositionY;//タイルの左上のY座標
  int tileNumberX;//0-7
  int tileNumberY;//0-7
  
  Tile(int ulpX, int ulpY, int tnX, int tnY){
    upperLeftPositionX = ulpX;
    upperLeftPositionY = ulpY;
    tileNumberX = tnX;
    tileNumberY = tnY;
  }
}

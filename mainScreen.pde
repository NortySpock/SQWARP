 //Processing.js example sketch
int fontsize = 24;
int mainScreenWidth = 500;
int mainScreenHeight = 500;

void setup() {
  size(mainScreenWidth, mainScreenHeight);
  stroke(0);
  fill(255);
  textFont(createFont("Arial",fontsize));
  noLoop();
}

void draw() {
  background(#000000);
  String textstring = "mainScreen";
  float twidth = textWidth(textstring);
  text(textstring, (width-twidth)/2, height/2);
  fill(128)
  triangle(30,75,59,20,86,75)
}

function Ship {
}
Ship.prototype.heading = 0


function posRatioTriangle(x,y,ratio) {

}

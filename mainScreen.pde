 //Processing.js example sketch
int fontsize = 24;

void setup() {
  size(400, 300);
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
}

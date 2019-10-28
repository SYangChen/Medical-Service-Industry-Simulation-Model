/*
HTML5 Canvas in C++

int main() has the Canvas code in it ⬇⬇⬇

Available Functions:

//Size Canvas
ctx.render(width,height);

//Block texture
ctx.fillStyle(1);

//Rectangle
ctx.fillRect(x,y,width,height);

//Background texture
ctx.background(0);

//Wrap and draw
ctx.draw();

More coming soon!

*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;



class Canvas{
    public:
    int w = 0;
    int h = 0;
    char colors[10] = {char(219),char(176),char(177),char(178)};
    char f = char(178);
    char bg = char(176);
    
    string lines[100][100];
    
    void render(int cw,int ch){
        w = cw;
        h = ch;
    }
    
    void fillStyle(char cf){
        f = colors[cf];
    }
    
    void background(char cf){
        bg = colors[cf];
    }
    
    void fillRect(int x,int y,int width,int height){
        for(int k = y;k < height + y;k++){
            for(int i = x;i < width + x;i++){
                lines[y + k][x + i] = f;
            }
        }
    }
    
    void draw(){
        for(int i = 0;i < h;i++){
            for(int j = 0;j < w;j++){
                if(lines[i][j] != ""){
                    cout << lines[i][j];
                }else{
                    cout << bg;
                }
            }
            cout << endl;
        }
    }
};


int main() {
    /*Declaration of Canvas class*/
    Canvas ctx;
    
    /*Render canvas (width,height)*/
    ctx.render(20,10);
    
    /*JS fillRect(x,y,width,height); object*/
    ctx.fillRect(0,0,5,5);
    
    /*Fill with color 3*/
    ctx.fillStyle(3);
    ctx.fillRect(3,2,5,5);
    
    /*For new background*/
    //ctx.background(0);

    /*Draw and wrap canvas*/
    ctx.draw();

    return 0;
}
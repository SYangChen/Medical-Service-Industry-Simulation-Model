#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <fstream>
#include <cstring>
#include <sstream>
#include <ctime>

using namespace std;

const int DIRECTION = 8;
const int SIZE = 40;
const int x_move[DIRECTION] = {-1, 0, 1, 1, 1, 0, -1, -1};
const int y_move[DIRECTION] = {1, 1, 1, 0, -1, -1, -1, 0};
void showWorld(char world[SIZE+1][SIZE+1]);
void activate(char world[SIZE+1][SIZE+1]);

int main(){
    
    /* init */
	char world[SIZE+1][SIZE+1] = {};
    for(int i=0; i<SIZE; i++){
    	memset(world[i], ' ', SIZE);
	}
	
    int x,y;
    int turn = 0, turn2 = 0;
    int number_Patient;
    int number_Doctor;
    int number_selfhealed;

    srand(time(NULL));
    while (true)
    {
	    int patient_cnt = 0;
	    int doctor_cnt = 0;
	    int heal_cnt = 0;
	    
	    number_Patient = rand() % 10 ; // 21~40
		while(patient_cnt < number_Patient)
	    {
	        x = rand() % SIZE;
	        y = rand() % SIZE;
	        if((world[x][y] == ' ')||(world[x][y] == '+')){
	            world[x][y] = 'X';
	            patient_cnt++;
	        }
	        else continue;
		    //showWorld(world);
		}
        
        if(turn % 3 == 0){
            turn = 0;
            number_Doctor = rand() % 4 + 1; // 5~9
            doctor_cnt = 0;
            while(doctor_cnt < number_Doctor){
                x = rand() % SIZE;
                y = rand() % SIZE;
                world[x][y] = '+';
                doctor_cnt++;
            }
        }
        
        /* ¯f¤H¦ÛÂ¡ */ 
        //if(turn2 % 10 == 0) 
        //{
        	turn2 = 0;
            number_selfhealed = rand() % 5 + 1; // 5~9
            heal_cnt = 0;
            while(heal_cnt < number_selfhealed){
                x = rand() % SIZE;
                y = rand() % SIZE;
                if(world[x][y]=='X'){
                	world[x][y] = ' ';
                	heal_cnt++;
				}
                
            }
		//}
		
        turn++;
        turn2++;
        showWorld(world);
        activate(world);
        usleep(500000); // 1 sec
        //system("CLS"); // for WINDOWS 10
        //system("clear"); // for ubuntu
        //clearScreen();
	}
  
}

void showWorld(char world[SIZE+1][SIZE+1]){

	// print border
	for(int i=0; i<SIZE+1; i++){
		cout << "--";
	}
	cout << endl;

	/* print World */
    for(int i = 1; i < SIZE; i++)
    {
    	cout <<"| ";
        for(int j = 1; j < SIZE; j++)
        {
            cout << world[i][j] << " ";
        }
        cout <<" |"<< endl;
    }

    // print border
    for(int i=0; i<SIZE+1; i++){
		cout << "--";
	}
	cout << endl;
}

void activate(char world[SIZE+1][SIZE+1]){

    for(int i = 1; i < SIZE; i++)
    {
        for(int j = 1; j < SIZE; j++)
        {
            /* count patient */
            int patient_cnt = 0;
            for(int d = 0; d < DIRECTION; d++)
            {
                if( world[i + x_move[d]][j + y_move[d]] == 'X'){
                    patient_cnt++;
                }
            }

            /* patient or people case */
            if(world[i][j] == 'X' || world[i][j] == ' '){
                /* Cluster infection */
                if(patient_cnt >= 5){
                	int infected = rand() % 4;
                    for(int n = 0; n < infected; n++)
                    {
                    	int d = rand() % 7; // give random direction
                        world[i + x_move[d]][j + y_move[d]] = 'X'; // random infection
                    }
                }
            }
            /* Doctor case */
            else{
                /* Healing patient(s) */
                if(patient_cnt < 4){
                    for(int d = 0; d < DIRECTION; d++)
                    {
                        world[i + x_move[d]][j + y_move[d]] = ' '; // become normal people
                    }
                }
                /* Doctor Overworked or retired */
                else{
                    world[i][j] = ' ';
                }
            }
        }
    }
}


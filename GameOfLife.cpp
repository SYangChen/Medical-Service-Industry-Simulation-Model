#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <cstring>
#include <ctime>
#include <algorithm>

using namespace std;

const int DIRECTION = 8;
const int SIZE = 40;
const int x_move[DIRECTION] = {-1, 0, 1, 1, 1, 0, -1, -1};
const int y_move[DIRECTION] = {1, 1, 1, 0, -1, -1, -1, 0};
void showWorld(char world[SIZE+2][SIZE+2]);
void activate(char world[SIZE+2][SIZE+2]);

int main(){
    
    /* init */
	char world[SIZE+2][SIZE+2] = {};
    for(int i=0; i<SIZE+2; i++){
    	memset(world[i], ' ', SIZE+2);
	}
	
    int x,y;
    int turn = 0;
    int number_Patient;
    int number_Doctor;
    int number_selfhealed;

    /* activate the world */
    srand(time(NULL));
    while (true){

	    int patient_cntr = 0;
	    int doctor_cntr = 0;
	    int heal_cntr = 0;
	    
	    number_Patient = rand() % 10; // 0~10
		while(patient_cntr < number_Patient){
	        x = rand() % SIZE + 1;
	        y = rand() % SIZE + 1;
	        if((world[x][y] == ' ') || (world[x][y] == '+')){
	            world[x][y] = 'X';
	            patient_cntr++;
	        }
	        else continue;
		}
        
        if(turn % 3 == 0){
            turn = 0;
            number_Doctor = rand() % 4 + 1; // 1~4
            doctor_cntr = 0;
            while(doctor_cntr < number_Doctor){
                x = rand() % SIZE + 1;
                y = rand() % SIZE + 1;
                world[x][y] = '+';
                doctor_cntr++;
            }
        }
        
        /* Patient Self-healed */ 
        number_selfhealed = rand() % 4 + 1; // 1~4
        while(heal_cntr < number_selfhealed){
            x = rand() % SIZE + 1;
            y = rand() % SIZE + 1;
            if(world[x][y] == 'X'){
                world[x][y] = ' ';
                heal_cntr++;
            }  
        }

        /* Count */
        int normal = 0;  // number of normal
        int doctor = 0;  // number of doctor
        int patient = 0; // number of patient

        for(int i = 1; i < SIZE+2; i++){
	        for(int j = 1; j < SIZE+2; j++){
	        	if(world[i][j] == ' ')
	        		normal++;
	        	else if(world[i][j] == 'X')
	        		patient++;
	        	else if(world[i][j] == '+')
	        		doctor++;
	        }
	    }

        /* Doctor is oversupply */
        if( (patient != 0) && (doctor / patient) > 3 ){
        	number_Doctor = rand() % 3 + 1; // 1~3 retire
        	doctor_cntr = 0;
            while(doctor_cntr < number_Doctor){
                x = rand() % SIZE + 1;
                y = rand() % SIZE + 1;
                if(world[x][y] == '+'){
                	world[x][y] = ' ';
                    doctor_cntr++;
                }
            }
        }

        turn++;
        showWorld(world);
        activate(world);
        usleep(1000000); // 1 sec
	}
    return 0;
}

void showWorld(char world[SIZE+2][SIZE+2]){

	// print border
	for(int i=0; i<SIZE+2; i++){
		cout << "--";
	}
	cout << endl;

	/* print World */
    for(int i = 1; i < SIZE+2; i++){
    	cout <<"| ";
        for(int j = 1; j < SIZE+2; j++){
            cout << world[i][j] <<" ";
        }
        cout <<" |"<< endl;
    }

    // print border
    for(int i=0; i<SIZE+2; i++){
		cout << "--";
	}
	cout << endl;
}

void activate(char world[SIZE+2][SIZE+2]){

    for(int i = 1; i < SIZE+2; i++){
        for(int j = 1; j < SIZE+2; j++){
            /* count patient */
            int patient_cntr = 0;
            for(int d = 0; d < DIRECTION; d++){
                if( world[i + x_move[d]][j + y_move[d]] == 'X'){
                    patient_cntr++;
                }
            }

            /* patient or people case */
            if(world[i][j] == 'X' || world[i][j] == ' '){
                /* Cluster infection */
                if(patient_cntr >= 5){
                	int infected = rand() % 4;
                    for(int n = 0; n < infected; n++){
                    	int d = rand() % 7; // give random direction
                        world[i + x_move[d]][j + y_move[d]] = 'X'; // random infection
                    }
                }
            }
            /* Doctor case */
            else{
                /* Healing patient(s) */
                if(patient_cntr < 4){
                    for(int d = 0; d < DIRECTION; d++){
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
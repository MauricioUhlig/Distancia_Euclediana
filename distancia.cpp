#include <iostream>
#include <stdlib.h>     
#include <time.h> 
#include <math.h>

using namespace std;

int main() {

    int m[10][2];
    int n = 3;
    srand (time(NULL));

    for(int i = 0; i < 10; i++){
        m[i][0]= rand()%100 +1;
        m[i][1]= rand()%100 +1;
    }

    for(int i = 0; i < 10; i++){
        cout << m[i][0] << "\t";
    }
    cout << endl;
    for(int i = 0; i < 10; i++){
        cout << m[i][1] << "\t";
    }
    cout << endl << "ordenado" << endl;




    return 0;
}

float minDist(int *m, n){
    if(n <= 3) return minDistBrute(m);
}

float minDistBrute(int *m){
    float a,b,c;
    float min;

    a = calcDist(m[0][0],m[0][1],m[1][0],m[1][1]);
    b = calcDist(m[0][0],m[0][1],m[2][0],m[2][1]);
    c = calcDist(m[2][0],m[2][1],m[1][0],m[1][1]); 

    min = (a<b) ? a : b;
    min = (min<c) ? min : c;

    return min;
}

float calcDist(int x1, int y1, int x2, int y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}
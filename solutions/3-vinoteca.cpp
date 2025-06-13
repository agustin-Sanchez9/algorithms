#include <iostream>
#include <ctime>
#include <ctsdlib>
using namespace std;

void MuestraMatriz(int matriz[][6]);
bool CumpleTOC(int matriz[][6]);

void CargaBotellas(int matriz[][6]){
	// 0 = vacio, 1 = botella
	for(int i=0; i<6 ; i++){
		for(int j=0; j<6 ; j++){
			matriz[i][j] = 0;
		}
	}
	for(int i=0 ; i<12 ; i++){
		int aux = rand()%36;
		matriz[aux/6][aux%6] = 1;
	}
}

int main(int argc, char *argv[]){
	int matriz[6][6];
	srand(time(NULL));
	do
		CargaBotellas(matriz);
	while(!CumpleTOC(matriz));
	MuestraMatriz(matriz);
	return 0;
}

bool CumpleTOC(int matriz[][6]){
	
}

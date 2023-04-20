#include <stdio.h>
#include<time.h>
#include<stdlib.h>
//A es NFA
// L(A) = {w | w termina con 01}
#define TRUE 1
#define FALSE 0
#define TAM 100000
typedef unsigned char boolean;

//Crea la matriz de procesos
boolean NFA(char *cadena, int size);
//Escribe el historial
void Record(int **procesos,char *cadena,int size);

int main()
{
	int size,i;
	char *cadena;
	
	srand(time(NULL));
	size = rand()%TAM+1;
	cadena = (char*)malloc(sizeof(char)*size);
	for(i=0; i<size ; i++){
		cadena[i]=(rand()%2)+'0';
	}
	if(NFA(cadena, size))
		printf("\nCadena aceptada\n");
	else
		printf("\nCadena rechazada\n");
	
	return 0;
}


boolean NFA(char *cadena, int size)
{
	int cad=0,pro=0,ultimo=1,limiteA=1;
	int q0=0,q1=1,q2=2,qphi=3;
	int **procesos;
	boolean b;
	
	//Crea "semi-matriz"
	procesos = (int **)malloc((size)*sizeof(int*));
	for (cad=0 ; cad<=size ; cad++)
			procesos[cad] = (int *) malloc ((cad+1)*sizeof(int));
		
	for(cad=0;cad<=size;cad++){
		for(pro=0;pro<limiteA;pro++)
				procesos[cad][pro]=9; 
		limiteA++;
	}
	//El automata empieza en el estado q0
	procesos[0][0]=q0;
	limiteA=1;
	for(cad=0 ; cad<size ; cad++) //cad<size y no <= porque se usa cad+1 dentro del for
	{
		for(pro=0 ; pro<limiteA&&procesos[cad][pro]!=9 ; pro++) //No sobrepasa el limite, ni revisa datos que no se usan
		{
			if(cadena[cad]=='0' && procesos[cad][pro]==0)
			{
				procesos[cad+1][pro]=q0;
				procesos[cad+1][ultimo]=q1;
				ultimo++;
			}
			else if(cadena[cad]=='1' &&procesos[cad][pro]==0)
			{
				procesos[cad+1][pro]=q0;
			}			
			else if(cadena[cad]=='1'&&procesos[cad][pro]==1)
			{
				procesos[cad+1][pro]=q2;
			}
			else 
			{
				procesos[cad+1][pro]=qphi;
			}
		}
		limiteA++;
	}
	Record(procesos, cadena,size);
	if(procesos[cad][ultimo-1]==q2)
		b=TRUE;
	else
		b=FALSE;
	return b;
}

void Record(int **procesos,char *cadena,int size)
{
	int pro=0,cad=0,limiteA=1;
	char c;
	FILE *record;
	record =fopen("record.txt","w+");
	fprintf(record, "\t\tP R O C E S O S\n");
	 
	for(cad=0; cad<=size ; cad++)
	{
		//Cadena
		if(cad!=size){
			fputc(cadena[cad], record);
			fputc('	', record);
		}
		else
			fputc('	', record);
		//Estados
		for(pro=0 ; pro<limiteA ; pro++)
		{
			if(procesos[cad][pro]<4)
			{
				if(procesos[cad][pro]==3)
					c='x';
				else
					c=procesos[cad][pro]+'0';
				
				fputc('q', record);
			    fputc(c, record);
				fputc('	', record);
			}		
		}
		limiteA++;
		fputc('\n', record);
	}
	fclose(record);
} 

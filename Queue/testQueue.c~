

#include <stdio.h>
#include <stdlib.h>
#include "queue.h"


void PrintQueue(QueueRecord* Q) {

int i = Q->Front;
printf("\n");
if (IsEmpty(Q))
printf("Empty Queue...\n");
else while(1){
	printf(" %d ",Q->Array[i].prob);
	if(i == Q->Rear)
		break;
	i=Succ(i,Q);
	}
printf("\n");  
}


main() {

  int e = 0;
  QueueRecord *Q;
  QueueRecord sa;
  Q = &sa;
  DTNMsg m;
  int i;

  MakeEmpty(Q);
  printf("Enqueue 20 elements...\n");
  for (i=0; i<20; i++) {
   m.prob = rand()%100;
   Enqueue(m, Q);
 }

PrintQueue(Q);

 
printf("\n Dequeing.......\n");
for (i=0; i<7; i++)
printf(" %d ",(FrontAndDequeue(Q)).prob);

printf("\n Enqueing.......\n");
for (i=0; i<5; i++) {
m.prob = rand()%100;
printf(" %d ",m.prob);
Enqueue(m, Q);
}


PrintQueue(Q); 
SortQueue(Q);
for (i=0; i<5; i++)
printf(" %d ",(FrontAndDequeue(Q)).prob);

PrintQueue(Q);
printf("\n\n");


}

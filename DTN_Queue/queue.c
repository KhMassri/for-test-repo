
/**

Written by: Khalil Massri
DTN Implementation
*/


#include"queue.h"



int IsEmpty(QueueRecord* Q) {
  return Q->Size == 0;
}

int IsFull(QueueRecord* Q) {
  return Q->Size == CAPACITY;
}

void MakeEmpty(QueueRecord* Q) {

  Q->Size = 0;
  Q->Front = 1;
  Q->Rear = 0;

}

int Succ(int Value, QueueRecord* Q) {
  if (++Value == CAPACITY) {
    Value = 0;
  }
  return Value;
}

void Enqueue(DTNMsg X, QueueRecord* Q) {

  if (IsFull(Q)) {
    return;
  } else {
    Q->Size++;
    Q->Rear = Succ(Q->Rear, Q);
    Q->Array[Q->Rear] = X;
  }

}


DTNMsg* Front(QueueRecord* Q) {

      return &(Q->Array[Q->Front]);
}

void Dequeue(QueueRecord* Q) {

  if (IsEmpty(Q)) {
    return;
  } else {
    Q->Size--;
    Q->Front = Succ(Q->Front, Q);
  }

}

DTNMsg FrontAndDequeue(QueueRecord* Q) {

  DTNMsg temp = {0,0,0};

  if (IsEmpty(Q))
    return temp;

  else {
    Q->Size--;
    temp = Q->Array[Q->Front];
    Q->Front = Succ(Q->Front, Q);
  }
  return temp;

}

void SortQueue(QueueRecord* Q){
if(IsEmpty(Q))
return;
DTNMsg temp;
int i,j;

for(i=Q->Front;i!=Q->Rear;i=Succ(i,Q))
for(j=Succ(i,Q); j!=Succ(Q->Rear,Q) ;j=Succ(j,Q))
{
if((Q->Array[j]).prob < (Q->Array[i]).prob)
{temp = Q->Array[i];
Q->Array[i]=Q->Array[j];
Q->Array[j]=temp;
}	
			
}

}



int Contains(QueueRecord* Q, int Id){
	if(IsEmpty(Q))
		return 0;
	int i = Q->Front;
	do{
		if((Q->Array[i]).seq == Id)
			return 1;
		if(i == Q->Rear)
			break;
		i=Succ(i,Q);
	}while(i!=Q->Front);

	return 0;
}









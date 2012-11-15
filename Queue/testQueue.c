

#include <stdio.h>
#include <stdlib.h>

#define MinQueueSize (5)

#define Error(Str)        FatalError(Str)
#define FatalError(Str)   fprintf(stderr, "%s\n", Str), exit(1)
#define CAPACITY 20

typedef struct
{
	int proto;
	int time;
	int seq;
	
}  DTNMsg;



typedef struct {
  int Front;
  int Rear;
  int Size;
  DTNMsg Array[CAPACITY];
} QueueRecord;

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



static int Succ(int Value, QueueRecord* Q) {
  if (++Value == CAPACITY) {
    Value = 0;
  }
  return Value;
}

void Enqueue(DTNMsg X, QueueRecord* Q) {

  if (IsFull(Q)) {
    Error("Enqueue Error: The queue is full.");
  } else {
    Q->Size++;
    Q->Rear = Succ(Q->Rear, Q);
    Q->Array[Q->Rear] = X;
  }

}

DTNMsg Front(QueueRecord* Q) {
DTNMsg X = {0,0,0};
  if (!IsEmpty(Q)) {
    return Q->Array[Q->Front];
  }
  Error("Front Error: The queue is empty.");

  /* Return value to avoid warnings from the compiler */
  return X;

}

void Dequeue(QueueRecord* Q) {

  if (IsEmpty(Q)) {
    Error("Dequeue Error: The queue is empty.");
  } else {
    Q->Size--;
    Q->Front = Succ(Q->Front, Q);
  }

}

DTNMsg FrontAndDequeue(QueueRecord* Q) {

  DTNMsg X = {0,0,0};

  if (IsEmpty(Q)) {
    Error("FrontAndDequeue Error: The queue is empty.");
  } else {
    Q->Size--;
    X = Q->Array[Q->Front];
    Q->Front = Succ(Q->Front, Q);
  }
  return X;

}


main() {

  
  QueueRecord *Q;
  QueueRecord sa;
  Q = &sa;
  DTNMsg m;
  int i;

  MakeEmpty(Q);
  printf("Enqueue 10 elements...\n");
  for (i=0; i<10; i++) {
   m.proto = i;
   Enqueue(m, Q);
 }


printf("Print all 10 elements...\n");
 while (!IsEmpty(Q)) {
   printf("%d ", (Front(Q)).proto);
   Dequeue(Q);
 }
printf("\n\n");

printf("Enqueue 10 more elements...\n");
for (i=10; i<20; i++) {
m.proto = i;
Enqueue(m, Q);
}

  printf("Print the new queue...\n");
  while (!IsEmpty(Q)) {
    printf("%d ", (Front(Q)).proto);
    Dequeue(Q);
  }
  printf("\n\n");

 

}

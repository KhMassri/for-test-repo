# +---------------------------------------------+
# | FILE   : Makefile                           |
# | AUTHOR : Jeffrey Hunter                     |
# | WEB    : http://www.iDevelopment.info       |
# | DATE   : 27-AUG-2002                        |
# | NOTE   : Makefile for Queue data structure. |
# +---------------------------------------------+
CC=gcc

testQueue: testQueue.o queue.o
	$(CC) testQueue.o queue.o -o $@

clean:
	rm -f a.out core *.o testQueue


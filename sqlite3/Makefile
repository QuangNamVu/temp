CC=g++
CFLAGS=-I.
SQL=-l sqlite3
DEPS=header.h
OBJ=main.o  convert.o login.o select.o teacher.o student.o admin.o update.o

%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(SQL)
all: main
	./main

.PHONY: clean
clean:
	@rm -f $(PROGRAMS) *.o core

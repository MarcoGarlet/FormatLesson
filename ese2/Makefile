CC = gcc
CFLAGS = -z execstack -no-pie -fstack-protector -no-pie -m32 -mpreferred-stack-boundary=2 
TARGET = ese
all: $(TARGET)
$(TARGET): $(TARGET).c
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c
clean:
	$(RM) $(TARGET)

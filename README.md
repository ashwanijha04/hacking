Hacking
====

This repository contains some resources for beginners to learn hacking. I was always curious about Hacking but never got these tutorials readily available and explained nicely. I haven't built any of these resources myself but I have collected the relevant materials to use. I am just happy to give this back to the community. Trust me, it feels like a super-power when you get this skill. A shiny upgrade to your Iron Man suit. Go break!

## Execution Command
Modern compilers are patched for buffer overflow vulnerabilities and we need to turn the protection off to practise this exploit.

   > gcc -fno-stack-protector -D_FORTIFY_SOURCE=0 -g -o <executable_name> <file_name>.c
#### Example:
   > gcc -fno-stack-protector -D_FORTIFY_SOURCE=0 -g -o auth_overflow auth_overflow.c
   > ./auth_overflow
#### Debugging:
   > gdb -q auth_overflow [ Start Debugging ]
   
   > break *main [Put a breakpoint at the start of main]
   
   > set disassembly-flavor intel [Set the disassembly flavor to intel type - Do it, it helps.]
   
   > disass main [Disassemble main - This seems fun. Shows the assembler code ]
   
   > list [ Lists the program literally ]
   
   > info registers [ Returns the information about the registers ]
   
   > x/24wx $rsp [ ]
   
   > x/2i $rip [ Returns the next two instructions of the instruction pointer ]


## Directories:
#### booksrc:
    Contains the examples from the Book: Hacking - The art of Exploitation.
    
#### Challenges:
    These are the challenges from protstar. They contain source code which can be exploited.
    https://exploit.education/protostar/stack-zero/
    



## Related Links
* get the live linux disc: [downlooad here](https://www.dropbox.com/s/eho0p2q8oaz53h1/hacking-live-1.0.iso?dl=0)
* http://www.amazon.com/Hacking-The-Art-Exploitation-Edition/dp/1593271441 - buy your own copy of the book

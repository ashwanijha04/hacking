Don't be a script kiddie.
====

This repository contains some resources for beginners to learn hacking. I was always curious about Hacking but never got these tutorials readily available and explained nicely. I haven't built any of these resources myself but I have collected the relevant materials to use. I am just happy to give this back to the community. Trust me, it feels like a super-power when you get this skill. A shiny upgrade to your Iron Man suit. Go break!


## Download the book: Hacking - The Art of exploitation [here](https://github.com/ashwanijha04/hacking/blob/master/Hacking-%20The%20Art%20of%20Exploitation%20(2nd%20ed.%202008)%20-%20Erickson.pdf)

Press the download button if it doesn't open.


## Where should I practice if I own shitty computers or office computer or "I don't wanna break my PC's memory" or anyhing else ?

Well, the cloud.
Recommended: AWS
OS: Ubuntu LTS Server 18.04 x/86 will do fine.

Go launch an Ubuntu Instance on AWS. SSH into the instance and start hacking.
Just clone this repository in your cloud machine and get started.


   #### How to launch a virtual machine on AWS?
   > https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/

   #### How to launch a virtual machine on AWS?

   > https://aws.amazon.com/free/

   #### Getting started with Amazon EC2 instances:
   > https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-get-started-overview


## Execution Command

Modern compilers are patched for buffer overflow vulnerabilities and we need to turn the protection off to practise this exploit.

   > gcc -fno-stack-protector -D_FORTIFY_SOURCE=0 -g -o <executable_name> <file_name>.c
#### Example:
   > gcc -fno-stack-protector -D_FORTIFY_SOURCE=0 -g -o auth_overflow auth_overflow.c
   > ./auth_overflow
#### Debugging:

   [ Start Debugging ]
   > gdb -q auth_overflow
   
   [Put a breakpoint at the start of main]
   > break *main
   
   [Set the disassembly flavor to intel type - Do it, it helps.]
   > set disassembly-flavor intel
   
   [Disassemble main - This seems fun. Shows the assembler code ]
   > disass main 
   
   [ Lists the program literally ] 
   > list
   
   > define hook-stop
   
   [ Returns the information about the registers ]
   > info registers
   
   > x/24wx $rsp [ ]
   
   > x/wx $rbp - <hex> [A local variable mostly]
   
   [ Returns the next two instructions of the instruction pointer ]
   > x/2i $rip 
   
   end

## Directories:

#### booksrc:
    Contains the examples from the Book: Hacking - The art of Exploitation.
    
#### Challenges:
    These are the challenges from protstar. They contain source code which can be exploited.
    https://exploit.education/protostar/stack-zero/
    



     Overview

This is a simple game of tic-tac-toe developed in Python. It allows two players to play with one another on different command lines through networking.
The host starts the game by first running host.py, waiting for the client to connect by then running client.py. Once their connected, the game itself starts.

The host starts as "X" and goes first, and the client is "O." The players choose the square they would like to use with coordinates; both "A1" and "1A" would be accepted, for example.
The game proceeds, with the players taking turns, until one wins or the game is a draw. The host, then the client, is asked whether they'd like a rematch. If both agree, the game starts anew.

 
I programmed this primarily to learn the basics of networking and how to send and receive data between two users. I also wanted to continue polishing my skills in the Python language.



Network Communication :

I used a host/client network architecture for this project using TCP (Transmission Control Protocol), and I used port 12783. 
The messages were sent back and forth between the host and the client thanks to the pickle module, which converts any object (in this case, a string list storing the nine squares of a tic-tac-toe grid) into a 
byte stream to be sent and back into an object to be read.

Development Environment :

Visual Studio Code

Python (3.9.4) 64-bit

Git / GitHub

Python: Socket, Pickle modules and streamlit.

System Environment: macOS Mojave/Version 10.14.2
Python3 Version: Python3.6.5

SUPPORT: W: White R: Red X: Solid O: Hollow

At the very beginning, execute module load python/3.5.1 on the shell

Run: Open shell->input python3 doublecard.py 
The project will run.

Start Step:
1. For Player1, choosing dots or colours. And Player 2 choose another.
2. Input player's step, for example: 0 3 C 3. When input player's step, the console will show the current board.
3. Alternate input until there is a win or a draw
4. When regular game ends in a draw(in 24 steps), players going to recycling game.
5. For recycling game, the input with different format, for example: A 9 B 9 2 C 5
6. Alternate input until there is a win or a draw(In 60 steps(regular + recycling))

All situation will input to txt file, which is located in same folder.
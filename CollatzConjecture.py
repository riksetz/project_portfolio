# Collatz Conjecture - One of the most famous unsolved problems in mathematics.
# Conjecture asks whether repeating 2 simple arithmetic operations will eventually transform every positive integer into 1.

import math

while True:
    programname = "Collatz Conjecture"
    print (f"\n{programname} Simulation\n")
    print ("Created as a part of a series of programs to determine if computers can be programmed to solve unsolved mathematical conjectures.\n")
    print (f"Disprove {programname} simply by solving for n where n is:")
    print (f"Any positive integer or a set of positive integers that do not eventually equal to 1 after the {programname} operations.\n")
    print (f"Alternatively, prove {programname} by solving for Ai(Stoping Time) without using a loop.\n")
    n = int(input("Enter n: "))
    n2 = n
    Ai = 0
    while n2 != 1: # Repeats operations until n reaches 1.
        if n2 % 2 == 0:
            # n is even.
            n2 = n2 / 2
        else:
            # n is odd.
            n2 = n2 * 3 + 1
        # Increment the total stopping time.
        Ai = Ai + 1
    print(f"The integer {n} will equal to 1, after performing the {programname} algorithm {Ai} times.")
    restart = input(f"Enter a different n value for {programname}? (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n")
        break
    else:
        print (f"Restarting {programname}...\n")
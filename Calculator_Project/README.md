PYTHON CALCULATOR PROJECT v1.2
------------------------------

1. WHAT ARE WE GOING TO BUILD?
We are building a simple calculator for calculating two numbers with an option for the user to check the history of calculations as well.


2. WHY ARE WE MAKING THIS?
We are making this just for practice on Loops and for improving the programming foundation.


3. HOW DOES IT WORK?
It works step-by-step like this:

   a. Firstly, we make variables to take input of numbers and the operator that the user wants to perform.

   b. Then we calculate those numbers on the basis of the operator with the help of a loop.

   c. After printing the result, we store it in a text file & ask the user to proceed further or if they want to see the history.

   d. If the user proceeds by typing 'no', then we start inputting the value again and the loop starts again.

   e. If the user wants to see the history by typing 'yes', then the program opens the text file in which past calculations are stored.

   f. If the user types 'exit', then the program breaks and gives a goodbye message.


4. TECHNICAL CONCEPTS USED
   - input(): To get the user's operations.
   - Loops: To organize the code for calculating and showing history.
   - Conditions (if-else): To decide what to do (proceed further, show history, or exit).
   - File Handling: To save and read history.


FEATURES
--------
1. Taking input (number and operator) in a single line.
2. Asking the user to continue calculation, see the history, or exit the program.
3. If user types 'yes' --> History will be shown till the last calculation.
4. If user types 'no' --> Calculation process starts again.
5. If user types 'exit' --> Program will finish with a "Goodbye" message.
6. Auto-Save: Saving the history with Date & Time.


IMPROVEMENTS DONE
-----------------
1. Removed Buffering Issue: Fixed file writing by proper indentation so that data writes immediately after calculation. The new process continues, and history is saved instantly.

2. Case Sensitivity Fixed: Removed errors during input by using .lower(). Now text is converted into lower case to match the condition without any error (e.g., EXIT works as exit).

# CSP-Sudoku-Solver
By Patrick Gavazzi (pgavaz01)


## Files:

sudokuSolver.py: Provides the solver for a Sudoku CSP problem that runs uses recursive backtracking along with conflit-directed backjumping to help it run faster. Also contains implementation for a node class that will be used to represent a hyper graph of the problem. 
    
sudokuSolver_tests.py: Contains unit test for some functions in my search implementation.





## run: 
To run the Sudoku solution finder program, run:
    
        python sudokuSolver_tests
     
Then enter either 'hard' or 'easy' depending on what kind of puzzle you would like to see the solver attempt. Then sit back and wait for the  answer, which will either be a failure message or a solution to the sudoku baord. 

     






## Asumptions/Comments:

I represented my soduku puzzle as a list of 9 lists where each one had9 elemtns in it : [ [A1 ... A9] [B1 ... B9 ] ... [I1 ... I9] ], and I assumed that the first list was the top right and the last list was the bottom most left. So it looks like this
      
      A A A  B B B  C C C 
      A A A  B B B  C C C 
      A A A  B B B  C C C 
      
      D D D  E E E  F F F
      D D D  E E E  F F F
      D D D  E E E  F F F
      
      G G G  H H H  I I I
      G G G  H H H  I I I
      G G G  H H H  I I I
      
With in each list, the first element is the top most right and the last elemtn is the bottoms most left. This looks like:
      
      A_1 A_2 A_3
      A_4 A_5 A_6
      A_7 A_8 A_9

To find a row, I checked every element in the horitonatlly neighboring boxes within the same range of 3, either 1-3 or 4-6 or 7-9. Here is a visual example of a row in the range 4-6 with boxes d,e, and f:
      
      D_4 D_5 D_6  E_4 E_5 E_6  F_4 F_5 F_6
      
To find a colmun, I checked every element in the vertically neighboringboxes and with their place the same range of either [1,4,7] or [2,5,8] or [3,6,9]. Here is a visual example of a column in the range [3,6,9] with boxes c,f, and i
      
      C_3
      C_6
      C_9 
      
      F_3
      F_6
      F_9
      
      I_3
      I_6
      I_9


## Testing:  
I wrote some unit test in the file sudokuSolver_tests.py, run it  to see messages printed out telling you how operations were preformed. Will also run recursive backtracking with another example sudoku baord. Run with:
       
           python sudokuSolver_tests.py

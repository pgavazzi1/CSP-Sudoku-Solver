# =============================================================================
# 
# sudokuSolver_tests.py
# hw 3, COMP131
# Fall 2020
#
# Simulates the unit tests for some functions in the sudokuSolver module
# =============================================================================

from sudokuSolver import print_puzzle
from sudokuSolver import is_complete
from sudokuSolver import recursive_backtracking
from sudokuSolver import Create_Hypergraph
            
    
# function name: make_finished_test
# Parameters: none
# Returns: A List of Lists of ints that represent a Sudoku board
# Does: Creates an already finished and correct Sudoku board
def make_finished_test():
    
    Square_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Square_b = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    Square_c = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    Square_d = [2, 3, 1, 5, 6, 4, 8, 9, 7]
    Square_e = [5, 6, 4, 8, 9, 7, 2, 3, 1]
    Square_f = [8, 9, 7, 2, 3, 1, 5, 6, 4]
    Square_g = [3, 1, 2, 6, 4, 5, 9, 7, 8]
    Square_h = [6, 4, 5, 9, 7, 8, 3, 1, 2]
    Square_i = [9, 7, 8, 3, 1, 2, 6, 4, 5]
    
    sudoku_board = [Square_a, Square_b, Square_c, Square_d, Square_e, Square_f,
                    Square_g, Square_h, Square_i]
    
    return sudoku_board


# function name: make_incomplete_test
# Parameters: none
# Returns: A List of Lists of ints that represent a Sudoku board
# Does: Creates an unfinished Sudoku board that is needing solving
def make_incomplete_test():
    
    Square_a = [8, 0, 0, 9, 6, 0, 0, 0, 7]
    Square_b = [3, 0, 9, 0, 0, 0, 2, 0, 0]
    Square_c = [0, 0, 0, 5, 0, 3, 0, 0, 0]
    Square_d = [0, 0, 6, 0, 2, 4, 0, 7, 0]
    Square_e = [4, 2, 0, 0, 0, 0, 0, 8, 0]
    Square_f = [0, 1, 0, 7, 0, 0, 0, 0, 0]
    Square_g = [0, 0, 1, 7, 0, 0, 0, 0, 0]
    Square_h = [7, 0, 0, 0, 0, 8, 0, 0, 0]
    Square_i = [8, 0, 0, 0, 6, 0, 0, 0, 4]
    
    sudoku_board = [Square_a, Square_b, Square_c, Square_d, Square_e, Square_f,
                    Square_g, Square_h, Square_i]
    
    return sudoku_board

  
# function name: test_completed_baord
# Parameters: none
# Returns: nothing
# Does: Tests that the goal test works on an already completed tree
def test_completed_baord():
    
    print('\n\n\n\n\n\n\n      Tetsing if an already complete and correct'
                               ' sudoku baord passes the complete test')  
    
    sudoku_board = make_finished_test() 
    print_puzzle(sudoku_board)
    if is_complete(sudoku_board):
       print('\n     And it passed the test, GOOD!')
    else:
       print('\n     it FAILED the test, BAD!')
     

# function name: Test_hyper_graph
# Parameters: none
# Returns: nothing
# Does: Creats a hypergraph of a sudoku baord and prints out the elements in 
#       both so the user can verify that the hypergraph was created correctly
#       to mirrior the sudoku board
def Test_hyper_graph():
    print('\n\n\n\n\n\n\n      Tetsing if the hyper graph values match the'
                               ' sudoku board') 
    
    sudoku_board = make_incomplete_test()
    hyper_graph = Create_Hypergraph(sudoku_board)
    
    print('\nHYPER GRAPH:\n\n')
    
    # Test if hypergraph values are correct
    for i in range( 0, 9 ):
        for x in range( 0, 9 ):
            print(hyper_graph[i][x].value, end=" ")
        print('\n')
    
    print('\n\nSUDOKU BOARD:\n\n')
    
    # Test if sudoku baord values are correct
    for i in range( 0, 9 ):
        for x in range( 0, 9 ):
            print(sudoku_board[i][x], end=" ")
        print('\n')
    
# function name: test_constraints
# Parameters: none
# Returns: nothing
# Does: Prints our the constraints of a couple of nodes so the user can verify
#       that the node's constraints were collected correctly
def test_constraints():
    print('\n\n\n\n\n\n\n     Tetsing if the constraints in the hypergraph'
                              'are collected correctly\n\n') 
        
    sudoku_board = make_incomplete_test()
    hyper_graph = Create_Hypergraph(sudoku_board)
    
    print( "     USING PUZZLE ")
    print_puzzle(sudoku_board)
    
    
    print( "\nVar in middle box of top row and at position 2 in the box "
           "has value", hyper_graph[1][2].value," and conflicts:")
    
    #TEST if hypergraph constriants are correct 
    print( '\nRow conflicts' )
    for i in range( 0, 8 ):
        if hyper_graph[1][2].conflict_set[i].value != 0: 
           print( hyper_graph[1][2].conflict_set[i].value)
    
    print( '\nCol conflicts' )
    for i in range( 8, 16 ):
        if hyper_graph[1][2].conflict_set[i].value != 0: 
            print( hyper_graph[1][2].conflict_set[i].value)
    
    print( '\nBoc conflicts' )
    for i in range( 16, 24 ):
        if hyper_graph[1][2].conflict_set[i].value != 0: 
            print( hyper_graph[1][2].conflict_set[i].value)
        
        
    print( "\nVar in right most box of bottom row and at position 3 in the box"
           " has no value and has conflicts:")
    
    #TEST if hypergraph constriants are correct 
    print( '\nRow conflicts' )
    for i in range( 0, 8 ):
        if hyper_graph[8][3].conflict_set[i].value != 0: 
           print( hyper_graph[8][3].conflict_set[i].value)
    
    print( '\nCol conflicts' )
    for i in range( 8, 16 ):
        if hyper_graph[8][3].conflict_set[i].value != 0: 
            print( hyper_graph[8][3].conflict_set[i].value)
    
    print( '\nBoc conflicts' )
    for i in range( 16, 24 ):
        if hyper_graph[8][3].conflict_set[i].value != 0: 
            print( hyper_graph[8][3].conflict_set[i].value)
            

  
# function name: test_incomplete_baord
# Parameters: none
# Returns: nothing
# Does: Preforms recursive backtracking on a different sudoku board just to
#       tests one more time that the solver works
def test_incomplete_baord():
    print('\n\n\n\n\n\n\n     Tetsing if an the recusive backtracking on' 
                              'another puzzle will solve it') 
    
    # sudoku_board = make_finished_test()
    sudoku_board = make_incomplete_test()
    hypergraph = Create_Hypergraph(sudoku_board)
    
    
    print('\n\n\n\n     BEFORE:')
    print_puzzle(sudoku_board)
    
    csp_result = recursive_backtracking (sudoku_board, hypergraph)
    
    if csp_result != 'FAILURE':
        print('\n\n\n\n     AFTER:')
        print_puzzle(csp_result)
        print('\n     it is completed and correct, GOOD!')
    else:
        print('\n     it is NOT completed nor correct, BAD!')




# function name: main
# Parameters: none
# Returns: nothing
# Does: Calls functions that run tests
if __name__ == "__main__":

    print('\n\n\nHI THERE! Welcome to the Unit Tests!')  
    
    
    test_completed_baord()
    Test_hyper_graph()
    test_constraints()
    test_incomplete_baord()

    

      
    
    
    print("\n\n\n\n\n\n\n\n\nALL DONE, Thanks for testing!")
    print("\n\n\n\n\n\n")
    
    
    

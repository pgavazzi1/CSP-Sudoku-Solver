# =============================================================================
# 
# sudokuSolver.py
# hw 3, COMP131
# Fall 2020
#
# Simulates the ....
# 
# =============================================================================




#################### Node Class for HyperGraph #######################

class Node:
    
    # function name: constructor
    # Parameters: An int that represents which box on the board the element 
    #             is in, an int that showes where in the box that index is
    #             and an int with the value of the box when consturcted
    # Returns: nothing
    # Does: Gives the node a location in the box, a 
    def __init__(self, box_index, in_box_index, value) :
        
        #Let node keep track where in the board it is
        self.box_index          = box_index
        self.in_box_index       = in_box_index
        
        #Node has a value to solve the puzzle
        self.value              = value
        
        # Conlfict set for conflict directed backjumping
        self.conflict_set       = []
        
        # Current values we can assign the current node 
        self.avaliable_values   = []
    
    # function name: add_row_constraints
    # Parameters: A list of lists of nodes that represent the hypergraph for 
    #             the board
    # Returns: Nothing
    # Does: Adds all nodes in the same row as the current node to act as 
    #       Constraints. 
    def add_row_constraints (self, hypergraph) :
        
        #Find which horizontal row of boxes to look for
        Box_bottom_range    = 0
        Box_top_range       = 3
        if self.box_index >= 3 and self.box_index <= 5  :
            Box_bottom_range = 3
            Box_top_range    = 6
        if self.box_index >= 6:
            Box_bottom_range = 6
            Box_top_range    = 9
        
        #Find which horizontal row of elements within the boxes to look for
        In_Box_bottom_range  = 0
        in_Box_top_range     = 3
        if self.in_box_index >= 3 and self.in_box_index <= 5  :
            In_Box_bottom_range = 3
            in_Box_top_range        = 6
        if self.in_box_index >= 6:
            In_Box_bottom_range = 6
            in_Box_top_range        = 9
        
        #Find neighbors in each row
        for i in range( Box_bottom_range, Box_top_range ):
            for x in range( In_Box_bottom_range, in_Box_top_range ):
                if hypergraph[i][x] == self:
                    continue
                self.conflict_set.append( hypergraph[i][x] )
    
        
    # function name: add_column_constraints
    # Parameters: A list of lists of nodes that represent the hypergraph for 
    #             the board
    # Returns: Nothing
    # Does: Adds all nodes in the same column as the current node to act as 
    #       Constraints.  
    def add_column_constraints (self, hypergraph) :
            
        #Find which vertical column of boxes to look for
        Box_bottom_range    = 0
        if ( self.box_index % 3 ) == 1:
            Box_bottom_range = 1
        if ( self.box_index % 3 ) == 2:
            Box_bottom_range = 2
        

        #Find which verticle column of elements within the boxes to look for
        In_Box_bottom_range  = 0
        if ( self.in_box_index % 3 ) == 1:
            In_Box_bottom_range = 1
        if ( self.in_box_index % 3 ) == 2:
            In_Box_bottom_range = 2
        
        #Find neighbors in each colmun
        for i in range( Box_bottom_range, 9, 3 ):
            for x in range( In_Box_bottom_range, 9, 3 ):
                if hypergraph[i][x] == self:
                    continue
                self.conflict_set.append( hypergraph[i][x] )

    # function name: add_box_constraints
    # Parameters: A list of lists of nodes that represent the hypergraph for 
    #             the board
    # Returns: Nothing
    # Does: Adds all nodes in the same box as the current node to act as 
    #       Constraints.  
    def add_box_constraints (self, hypergraph) :

        for x in range(0,9):
            if not hypergraph[self.box_index][x] == self:
                self.conflict_set.append( hypergraph[self.box_index][x] )
    
    
    # function name: __eq__
    # Parameters: another node
    # Returns: true if the two nodes represent the same box in the array, 
    #          false otherwise 
    # Does: compares two nodes
    def __eq__(self, other) : 
        
        return ( 
                 self.box_index == other.box_index 
                 and self.in_box_index == other.in_box_index 
               ) 













#################### Functions that Check Constraints #######################

    
# function name: check_columns
# Parameters: a list of lists of ints that represent the sudoku board
# Returns: True if all numbers are unique, false otherwise
# Does: preforms goal test on all columns by making sure that only that each 
#       slot has a unique number
def check_columns(sudoku_board, lower_range):
    
    # Check to see if the elements are distinct in the 1st colmun of three 
    # vertically neighboring boxes    
    avaliable_in_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range, 9, 3):
        for x in range(0, 7, 3):
            try:
                avaliable_in_col.remove( sudoku_board[i][x] )
            except:
                return False
    
    # Check to see if the elements are distinct in the middle colmun of three 
    # vertically neighboring boxes  
    avaliable_in_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range, 9, 3):
        for x in range(1, 9, 3):
            try:
                avaliable_in_col.remove( sudoku_board[i][x] )
            except:
                return False
    
    # Check to see if the elements are distinct in the 3rd colmun of three 
    # vertically neighboring boxes  
    avaliable_in_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range, 9, 3):
        for x in range(2, 9, 3):
            try:
                avaliable_in_col.remove( sudoku_board[i][x] )
            except:
                return False
            
    return True

    
# function name: check_rows
# Parameters: a list of lists of ints that represent the sudoku board
# Returns: True if all numbers are unique, false otherwise
# Does: preforms goal test on all rows by making sure that only that each slot 
#       has a unique number
def check_rows(sudoku_board, lower_range, upper_range):
    

    # Check to see if the elements are distinct in the top row of three 
    # horitonally neighboring boxes   
    avaliable_in_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range,upper_range):
        for x in range(0,3):
            try:
                avaliable_in_row.remove( sudoku_board[i][x] )
            except:
                return False
               
    # Check to see if the elements are distinct in the middle row of three 
    # horitonally neighboring boxes    
    avaliable_in_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range,upper_range):
        for x in range(3,6):
            try:
                avaliable_in_row.remove( sudoku_board[i][x] )
            except:
                return False
               
    # Check to see if the elements are distinct in the bottom row of three 
    # horitonally neighboring boxes    
    avaliable_in_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(lower_range,upper_range):
        for x in range(6,9):
            try:
                avaliable_in_row.remove( sudoku_board[i][x] )
            except:
                return False
            
    return True
    
# function name: check_boxes
# Parameters: a list of lists of ints that represent the sudoku board
# Returns: True if all numbers are unique, false otherwise
# Does: preforms goal test on boxes by making sure that only that each slot 
#       has a unique number
def check_boxes(sudoku_board):
    
    # Make sure all elements in a box of 9 are distinct 
    for i in range(0,9):
        avaliable_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(0,9):
            try:
                avaliable_in_box.remove( sudoku_board[i][j] )
            except:
                return False
    return True   

# function name: is_complete
# Parameters: a list of lists of ints that represent the sudoku board
# Returns: True if we have a fully complete baord, false otherwise
# Does: Prefroms goal tests on all constraints of the soduko graph
def is_complete(sudoku_board):
    
  
    # Preform tests on all column constraints 
    if check_columns(sudoku_board, 0) == False :
        return False
    if check_columns(sudoku_board, 1) == False:
        return False
    if check_columns(sudoku_board, 2) == False:
        return False
    
    # Preform tests on all row constraints 
    if check_rows(sudoku_board, 0, 3) == False :
        return False
    if check_rows(sudoku_board, 3, 6) == False:
        return False
    if check_rows(sudoku_board, 6, 9) == False:
        return False

    # Preform tests on all box constraints 
    if not check_boxes(sudoku_board):
       return False
    
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

##################### Functions that Assign Values #####################


# function name: select_unassigned_variable
# Parameters: Two list of lists, one full of ints that represents our variable
#             assignments and one full of nodes the represents our conflicts
# Returns: an unassigned node that represents a spot in the sudoku board
# Does: Finds the next spot in the table with no value assigned to it yet
def select_unassigned_variable( sudoku_board, hypergraph ):
    for i in range( 0, 9):
        for x in range( 0, 9):
            if sudoku_board[i][x] == 0:
                return hypergraph[i][x]
            
            
# function name: select_avilable_values
# Parameters: A node that represents a space in our sudoko puzzle
# Returns: Nothing
# Does: Finds acceptables value that we can assign to our variable
def select_avilable_values( var ):

    var.avaliable_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range( 0, 24):
        try:
            var.avaliable_values.remove( var.conflict_set[i].value )
        except:
            continue


# function name: conflict_directed_backjumping
# Parameters: A node that represents a space in our sudoko puzzle, A list of 
#             lists if ints that represents our sudoko puzzle, and a list of 
#             lists of nodes that represent the conflicts
# Returns: Nothing
# Does: Looks through the variables conflict set and resigns a value there
def conflict_directed_backjumping( var, sudoku_board, hypergraph ):
    
     # Look through the nodes entire conflict set
     for i in range( 0, 24):
         
            # If that conflicting node has more variables to try in its
            #  domain, try reasigning them to it 
            if not len( var.conflict_set[i].avaliable_values ) == 0:
                
                value  = var.conflict_set[i].avaliable_values[0]
                
                var.conflict_set[i].value = value
                box_index                 = var.conflict_set[i].box_index
                in_box_index              = var.conflict_set[i].in_box_index
                sudoku_board[ box_index ][ in_box_index ] = value
                
                # Check to see if there are more variables for current var to 
                # begin again
                select_avilable_values( var )
                if len(var.avaliable_values) != 0:
                    break


# function name: recursive_backtracking
# Parameters: Two list of lists, one full of ints that represents our variable
#             assignments and one full of nodes the represents our conflicts
# Returns: FAILURE if we could not find an acceptable value for the particular 
#          slot in the board, otherwise returns the completed sudoku board
# Does: Checks to see if the sudoku board is complet3ed, other wise will assign
#       a value to the next variable in the board and recurse. Will return
#       once we have found an acceptable table or we can not try to assign any 
#       more values to the table. 
def recursive_backtracking(sudoku_board, hypergraph):
    
    # If it current board satifies the goal test, return the current board
    if is_complete(sudoku_board):
        return sudoku_board
  
    # Find next unassigned variable in the board
    var = select_unassigned_variable(sudoku_board, hypergraph)
    select_avilable_values( var )
    
    # Apply conflict directed backjumping if no elements are aviable
    if len(var.avaliable_values) == 0:
        conflict_directed_backjumping( var, sudoku_board, hypergraph )

    # For every current avaliable value for the board, assign it and try
    # Recursing with this value in table 
    # for value in var.avaliable_values:
    while len(var.avaliable_values) != 0:
        value = var.avaliable_values[0]
        var.value = value
        sudoku_board[ var.box_index ][ var.in_box_index ] = value
        result = recursive_backtracking(sudoku_board, hypergraph)
        
        # Get rid of number if we have already tried it
        if len(var.avaliable_values) != 0:
            var.avaliable_values.pop(0)
            
        # return result if a solution was found
        if result != 'FAILURE':
            return result
    
    # Get rid of what ever 
    hypergraph[ var.box_index ][ var.in_box_index ].value = 0
    sudoku_board[ var.box_index ][ var.in_box_index ] = 0
        
            
        
    return 'FAILURE'





#####################  Functions that Printing  #####################
 

# function name: print_puzzle
# Parameters: none
# Returns: nothing
# Does: Prints out three consecutive boxes in the puzzle
def print_three(sudoku_board, lower_range, upper_range):
    
    # Print out the top row of elements in three boxes
    print("\n  - - - - - -     - - - - - -     - - - - - -")        
    print ('', end =' | ')
    for i in range(lower_range,upper_range):
        for x in range(0,3):
            if sudoku_board[i][x] == 0:
                print (" ", end =' | ')
            else:
                print (sudoku_board[i][x], end =' | ')
        if not i == upper_range - 1:
            print ('  | ', end ='')
   
    # Print out the middle row of elements in three boxes
    print("\n  - - - - - -     - - - - - -     - - - - - -")
    print ('', end =' | ')
    for i in range(lower_range,upper_range):
        for x in range(3,6):
            if sudoku_board[i][x] == 0:
                print (" ", end =' | ')
            else:
                print (sudoku_board[i][x], end =' | ')
        if not i == upper_range - 1:
            print ('  | ', end ='')
    
    # Print out the bottom row of elements in three boxes
    print("\n  - - - - - -     - - - - - -     - - - - - -")
    print ('', end =' | ')
    for i in range(lower_range,upper_range):
        for x in range(6,9):
            if sudoku_board[i][x] == 0:
                print (" ", end =' | ')
            else:
                print (sudoku_board[i][x], end =' | ')
        if not i == upper_range - 1:
            print ('  | ', end ='')
    print("\n  - - - - - -     - - - - - -     - - - - - -") 


# function name: print_puzzle
# Parameters: none
# Returns: nothing
# Does: Calls function that print out the current state of the puzzle 
def print_puzzle(sudoku_board):
    
    # Print three boxes at a time, and prints top, middle, the bottom
    print_three(sudoku_board, 0, 3)
    print_three(sudoku_board, 3, 6)
    print_three(sudoku_board, 6, 9)        
            
    
    
    
    
    
    
    

#####################  Functions that create the problems  #####################


# function name: Create_Hypergraph
# Parameters: none
# Returns: list of lists of nodes that represents a sudoku board in hyper
#          graph form
# Does: creates a hyper graph of nodes that represent the conflicts in the 
#       each space in the hyper graph has 
def Create_Hypergraph(sudoku_board):
    
    hyper_graph = [ [], [], [], [], [], [], [], [], [] ]
    
    #Create inital nodes in the hypergraph
    for i in range( 0, 9 ):
        for x in range( 0, 9 ):
            new_node = Node( i, x, sudoku_board[i][x])
            hyper_graph[i].append(new_node)
    
    #Create restiants (connections) between nodes
    for i in range( 0, 9 ):
        for x in range( 0, 9 ):
            hyper_graph[i][x].add_row_constraints(hyper_graph)
            hyper_graph[i][x].add_column_constraints(hyper_graph)
            hyper_graph[i][x].add_box_constraints(hyper_graph)
    
    return hyper_graph
    
    
    
# function name: make_easy
# Parameters: none
# Returns: list of lists of ints that represents a sudoku board
# Does: Creates a list of lists of ints that represent the easy sudoku puzzle
def make_easy():
    
    # Make board with already in place values
    Square_a = [6, 0, 8, 4, 0, 0, 0, 2, 5]
    Square_b = [7, 0, 2, 0, 1, 0, 4, 0, 0]
    Square_c = [1, 0, 0, 0, 0, 2, 0, 0, 0]
    Square_d = [7, 0, 1, 0, 8, 0, 5, 0, 9]
    Square_e = [0, 8, 0, 0, 0, 0, 0, 6, 0]
    Square_f = [4, 0, 5, 0, 7, 0, 3, 0, 1]
    Square_g = [0, 0, 0, 2, 0, 0, 0, 0, 6]
    Square_h = [0, 0, 6, 0, 9, 0, 8, 0, 5]
    Square_i = [7, 5, 0, 0, 0, 8, 2, 0, 3]
    
    sudoku_board = [ Square_a, Square_b, Square_c, 
                     Square_d, Square_e, Square_f,
                     Square_g, Square_h, Square_i ]
    
    return sudoku_board

    
    
# function name: make_hard
# Parameters: none
# Returns: list of lists of ints that represented a sudoku board
# Does: Creates a list of lists of ints that represent the hard sudoku puzzle
def make_hard():
    
    # Make board with already in place values
    Square_a = [0, 7, 0, 0, 0, 0, 3, 9, 0]
    Square_b = [0, 4, 2, 0, 0, 8, 0, 0, 0]
    Square_c = [0, 0, 0, 6, 1, 0, 0, 0, 7]
    Square_d = [0, 0, 0, 0, 0, 3, 5, 0, 0]
    Square_e = [0, 0, 4, 0, 0, 0, 1, 0, 0]
    Square_f = [0, 0, 9, 7, 0, 0, 0, 0, 0]
    Square_g = [8, 0, 0, 0, 5, 4, 0, 0, 0]
    Square_h = [0, 0, 0, 8, 0, 0, 6, 1, 0]
    Square_i = [0, 7, 6, 0, 0, 0, 0, 5, 0]
    
    sudoku_board = [ Square_a, Square_b, Square_c, 
                     Square_d, Square_e, Square_f,
                     Square_g, Square_h, Square_i ]
    
    return sudoku_board



# function name: get_input
# Parameters: none
# Returns: the created list that contains the sudoku board
# Does: Get's user input on what difficulty of puzzle to make, then calls a
#       function that makes the specified puzzle
def get_input():
    
    # Get input for puzzle and make sure it is correct
    print('\n\n     Would you like to solve a hard or easy puzzle?') 
    puzzle_diffculty = input('     (hard/easy): ')
    correct_response = False
    
    while correct_response == False:
        if puzzle_diffculty == 'hard' :
            return make_hard()
        elif puzzle_diffculty == 'easy' :
            return make_easy()
        else :
            puzzle_diffculty = input('     Please enter valid sensor input?'
                                     '\n     (hard/easy): ')
            continue
        correct_response = True


    

#####################  Main Function  #####################

# function name: main
# Parameters: none
# Returns: nothing
# Does: Calls function that creat sudoku boards and then solves them, and then
#       Prints the result of the search
if __name__ == "__main__":

    print('\n\n\nHI THERE! Welcome to the Sudoku Solve!')  

    # Make sudoku board based on user input and create corresponding hyper 
    # graph
    sudoku_board = get_input()
    hypergraph = Create_Hypergraph(sudoku_board)
    
    print('\n\n\nStarting Board:')
    print_puzzle (sudoku_board)
    csp_result = recursive_backtracking (sudoku_board, hypergraph)
    
    if csp_result != 'FAILURE':
        print('\n\nFound solution!!!!!, here it is:')
        print_puzzle(sudoku_board)
    else:
        print('FAILURE, could not find soltuion... better luck next time')
      
    
    
    print("\n\n\nAll done now, Thanks for PLaying!")
    print("\n\n\n\n\n\n")
    
    
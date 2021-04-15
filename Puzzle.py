from copy import deepcopy
from heapq import heappush, heappop, heapify

class PuzzleState():
    def __init__(self, puzzle_board):
        self.puzzle_board = puzzle_board
        
        try:
            self.blank_tile = puzzle_board.index(0)
        except:
            pass

        self.g = 0
        self.h = self.getHCost()
        self.f = 0

        self.parent = None

    def __hash__(self):
        """ Hash function for storing nodes in closed list dictionary """
        return hash((self.g, self.h))

    def __eq__(self, other):
        return self.puzzle_board == other.puzzle_board

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __str__(self):
        return (
            f'{self.puzzle_board[0]} {self.puzzle_board[1]} {self.puzzle_board[2]}\n'
            f'{self.puzzle_board[3]} {self.puzzle_board[4]} {self.puzzle_board[5]}\n'
            f'{self.puzzle_board[6]} {self.puzzle_board[7]} {self.puzzle_board[8]}\n'
        )

    def getHCost(self):
        count = 0

        if self.puzzle_board[0] != 1:
            count += 1

        if self.puzzle_board[1] != 2:
            count += 1
        
        if self.puzzle_board[2] != 3:
            count += 1
            
        if self.puzzle_board[3] != 8:
            count += 1
            
        if self.puzzle_board[4] != 0:
            count += 1
            
        if self.puzzle_board[5] != 4:
            count += 1

        if self.puzzle_board[6] != 7:
            count += 1

        if self.puzzle_board[7] != 6:
            count += 1
            
        if self.puzzle_board[8] != 5:
            count += 1

        return count

    def isSolvable(self):
        inversion_count = 0
        all_values = [0,1,2,3,4,5,6,7,8]

        # check if 0 - 8 is on the board
        if all(x in self.puzzle_board for x in all_values):

            # loop thru the array getting the element and index
            for index, element in enumerate(self.puzzle_board):
                if element == 0:
                    pass
                # Search the rest of the list for inversions
                for x in self.puzzle_board[index+1:]:
                    if x == 0:
                        pass
                    elif element > x:
                        inversion_count += 1
                
                # Check for even number of inversions
                if inversion_count % 2 == 0:
                    return True
                else:
                    return False 
        else:
            return False

    def generateMoves(self):
        """ Returns a dictionary of moves and their gcost """
        moves = {} # {index: Gcost, index: Gcost}

        if self.blank_tile == 0:
            moves[1] = self.puzzle_board[1] # Move top-middle
            moves[3] = self.puzzle_board[3] # Move middle-left

        elif self.blank_tile == 1:
            moves[0] = self.puzzle_board[0] # Move top-left
            moves[2] = self.puzzle_board[2] # Move top-right
            moves[4] = self.puzzle_board[4] # Move middle-middle

        elif self.blank_tile == 2:
            moves[1] = self.puzzle_board[1] # Move top-middle
            moves[5] = self.puzzle_board[5] # Move middle-right

        elif self.blank_tile == 3:
            moves[0] = self.puzzle_board[0] # Move top-left
            moves[4] = self.puzzle_board[4] # Move middle-middle
            moves[6] = self.puzzle_board[6] # Move bottom-left

        elif self.blank_tile == 4:
            moves[1] = self.puzzle_board[1] # Move top-middle
            moves[3] = self.puzzle_board[3] # Move middle-left
            moves[5] = self.puzzle_board[5] # Move middle-middle
            moves[7] = self.puzzle_board[7] # Move bottom-middle

        elif self.blank_tile == 5:
            moves[2] = self.puzzle_board[2] # Move top-middle
            moves[4] = self.puzzle_board[4] # Move middle-left
            moves[8] = self.puzzle_board[8] # Move top-middle

        elif self.blank_tile == 6:
            moves[3] = self.puzzle_board[3] # Move middle-left
            moves[7] = self.puzzle_board[7] # Move bottom-middle

        elif self.blank_tile == 7:
            moves[4] = self.puzzle_board[4] # Move middle-middle
            moves[6] = self.puzzle_board[6] # Move bottom-left
            moves[8] = self.puzzle_board[8] # Move bottom-right

        elif self.blank_tile == 8:
            moves[5] = self.puzzle_board[5] # Move middle-right
            moves[7] = self.puzzle_board[7] # Move bottom-middle

        # Order the dictionary by G-cost
        ordered_moves = {k: v for k, v in sorted(moves.items(), key=lambda item: item[1])}
        return ordered_moves
    
    def generateNeighbors(self):
        neighbors = {} # {PuzzleState: Gcost, PuzzleState: Gcost}
        moves = self.generateMoves()

        for index, gcost in moves.items():
            temp_board = deepcopy(self.puzzle_board) # Copy current board
            temp_board[self.blank_tile], temp_board[index] = temp_board[index], temp_board[self.blank_tile]

            neighbors[PuzzleState(temp_board)] = gcost

        # Order the dictionary by G-cost
        ordered_neighbors = {k: v for k, v in sorted(neighbors.items(), key=lambda item: item[1])}
        return ordered_neighbors

    def aStar(self):
        solution = [1,2,3,8,0,4,7,6,5]

        # Create open and closed lists
        open_list = []
        closed_list = []

        # Heapify the open list and add the starting node
        heapify(open_list)
        heappush(open_list, self)

        while len(open_list) > 0:
            # Get current node
            current_node = heappop(open_list)
            closed_list.append(current_node)

            # If goal is found
            if current_node.puzzle_board == solution:
                solution_path = []
                # Return the solution path by backtracking thru the parent
                while current_node:
                    solution_path.insert(0, current_node) 
                    current_node = current_node.parent
                return solution_path

            # Create children
            children = current_node.generateNeighbors()

            for child, gcost in children.items():

                if child in closed_list:
                    continue

                child.g = current_node.g + gcost
                child.f = child.g + child.h
                child.parent = current_node

                if child in open_list:
                    continue
                
                heappush(open_list, child)

        return None
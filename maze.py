import sys

class Node():
    def __init__(self,state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)   
        
    def empty(self, state):
        return len(self.frontier) == 0
        
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]            ## Pop the node off the stack and return it
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier():
    
    def remove(self):
        if self.empty()
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]            ## remove from queue and return it
            self.frontier = self.frontier[1:]
            return node
            
class Maze():
    def __init__(self, filename):
        
        # Read file and set height and width of maze
        with open(filename) as f: 
            #......  Bunch of code that was kipped over
           
           
    def solve(self):
        """FInds a solution to maze, of one exists."""
        
        # Keep track of number of states explored
        self.num_explored=0
        
        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()  ## << DEPTH FIRST SEARCH >>
        frontier.add(start)
        
        # Initialize an empty explored set
        self.explored = set()
        
        # Keep looping until solution found
        while True: 
            
            # If nothing left in the frontier, the no path
            if frontier.empty():
                raise Exception("no solution")
            
            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1
       
            # if node is the goal, then we have a solution
            if node.state == self.goal:
                actions = [] 
                cells = [] 
       
            # Follow parent nodes to find solution
            while node.parent is not None:
                actions.append(node.action) 
                cells.append(node.state) 
                node = node.parent 
                
            actions.reverse() 
            cells.reverse() 
            self.solution = (actions, cells) 
            return
        
       # Mark node as explored 
       self.explored.add(node.state)
       
       # Add neighbors to frontier
       for action, state in self.neighbors(node.state):
           if not frontier.contains_state(state) and state no in self.explored:
               child = Node(state=state, parent=node, action=action)
               frontier.add(child)

## MAP: Code is not complete, need to downlad file
"""
Example of maze file, maze1.txt
NOTE: Hashmarks are walls, start A, end B
#####B#
##### #            
####  #            
#### ##            
     ##            
A######
"""
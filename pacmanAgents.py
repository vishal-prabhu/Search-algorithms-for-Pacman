`# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
from heuristics import scoreEvaluation
import random

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class GreedyAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(scoreEvaluation(state), action) for state, action in successors]
        # get best choice
        bestScore = max(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        
        # Queue that stores the game states
        state_queue = []
        # List that stores the leaf nodes
        leaf_list = []
        # List that stores the win states
        win_state_list = []
        
        # Get legal pacman actions
        legal = state.getLegalPacmanActions()
        # Generate successors
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # Append successors to the Queue
        state_queue.extend(successors)
        
        
        while state_queue:
            # Pop first element of the Queue
            next_state, action = state_queue.pop(0)
            
            # Check for win state and append it and the action to the list of win state
            if next_state.isWin():
                win_state_list.append((next_state, action))
        
            # Get legal pacman actions
            legal = next_state.getLegalPacmanActions()
            # Generate successors
            next_successors = [(next_state.generatePacmanSuccessor(next_action), next_action) for next_action in legal]
            
            for tuple in next_successors:
                # Check if successor is None, append the parent state and action to the list of leaves
                if tuple[0] == None:
                    leaf_list.append((next_state, action))
                # Check if successor is a Win state, append the state to the list of Win states
                elif tuple[0].isWin():
                    win_state_list.append((tuple[0], action))
                # Else, append state and action to the original Queue
                else:
                    state_queue.append((tuple[0], action))


        # For all the win states, return the action leading to the win state with the best score
        while win_state_list:
            max_score = 0
            for win_pair in win_state_list:
                if scoreEvaluation(win_pair[0]) > max_score:
                    max_score = scoreEvaluation(win_state_list)
                    bestAction = win_pair[1]
            return bestAction
        
        
        # For all the leaf nodes, evaluate the score and return the action leading to the win state with the best score
        scored = [(scoreEvaluation(state), action) for state, action in leaf_list]
        bestScore = max(scored)[0]
        print bestScore
        for tuple in scored:
            if tuple[0] == bestScore:
                bestAction = tuple[1]
                break
        print bestAction
        return bestAction
            

        #return Directions.STOP
        

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP
        
        # Stack that stores the game states
        state_stack = []
        # List that stores the leaf nodes
        leaf_list = []
        # List that stores the win states
        win_state_list = []
        
        # Get legal pacman actions
        legal = state.getLegalPacmanActions()
        # Generate successors
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # Apend successors to the stack
        state_stack.extend(successors)
        
        
        while state_stack:
        
            # Pop the last element of the stack
            next_state, action = state_stack.pop()
            
            # Check for win state and append it and the action to the list of win state
            if next_state.isWin():
                win_state_list.append((next_state, action))
            
            # Get legal pacman actions
            legal = next_state.getLegalPacmanActions()
            # Generate successors
            next_successors = [(next_state.generatePacmanSuccessor(next_action), next_action) for next_action in legal]
            
            for tuple in next_successors:
                # Check if successor is None, append the parent and the action to the list of leaves
                if tuple[0] == None:
                    leaf_list.append((next_state, action))
                # Check if successor is a Win state, append the state and the action to the list of Win states
                elif tuple[0].isWin():
                    win_state_list.append((tuple[0], action))
                # Else, append state and action to the original Queue
                else:
                    state_stack.append((tuple[0], action))


        # For all the win states, return the action leading to the win state with the best score
        while win_state_list:
            max_score = 0
            for win_pair in win_state_list:
                if scoreEvaluation(win_pair[0]) > max_score:
                    max_score = scoreEvaluation(win_state_list)
                    bestAction = win_pair[1]
            return bestAction
    
    
        # For all the leaf nodes, evaluate the score and return the action leading to the win state with the best score
        scored = [(scoreEvaluation(state), action) for state, action in leaf_list]
        bestScore = max(scored)[0]
        for tuple in scored:
            if tuple[0] == bestScore:
                bestAction = tuple[1]
                break
        print bestAction
        return bestAction


        #return Directions.STOP


class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
        
        # Queue that stores the game states
        state_queue = []
        # Depth
        depth = 0
        # Cost function
        cost = 0
        # List that stores the leaf nodes
        leaf_list = []
        # List that stores the win states
        win_state_list = []

        # Get legal pacman actions
        legal = state.getLegalPacmanActions()
        # Increment depth
        depth = depth + 1
        
        for action in legal:
            # Generate successors
            successor = state.generatePacmanSuccessor(action)
            # Calculate cost of the node
            cost = depth - (scoreEvaluation(successor) - scoreEvaluation(state))
            # Append successor, action, cost of the node, and the depth of the node to the queue
            state_queue.append((successor, action, cost, depth))
        
        # Sort the queue in the increasing order of the cost function
        state_queue.sort(key=lambda tuples: tuples[2])
        
        while state_queue:
            
            # Pop the first element of the queue
            next_state, action, cost, depth = state_queue.pop(0)
            
            # Check for win state and append it and the action to the list of win state
            if next_state.isWin():
                win_state_list.append((next_state, action))
            
            # Get legal pacman actions
            legal = next_state.getLegalPacmanActions()
            # Increment depth
            depth = depth + 1

            for next_action in legal:
                # Generate successor
                child = next_state.generatePacmanSuccessor(next_action)
                # Check if successor is None, append the parent and the action to the list of leaves
                if child == None:
                    depth = depth - 1
                    next_cost = depth - (scoreEvaluation(next_state) - scoreEvaluation(state))
                    leaf_list.append((next_state, action, next_cost, depth))
                # Check if successor is a Win state, append the state and the action to the list of Win states
                elif child.isWin():
                    win_state_list.append((child, action))
                # Else, append state, action, cost of the node, and the depth of the node to the original Queue
                else:
                    next_cost = depth - (scoreEvaluation(child) - scoreEvaluation(next_state))
                    next_successors = (child, action, next_cost, depth)
                    state_queue.append(next_successors)
                
                # Sort the queue in the increasing order of the cost function
                state_queue.sort(key=lambda tuples: tuples[2])
            
            # Sort the queue in the increasing order of the cost function
            state_queue.sort(key=lambda tuples: tuples[2])
            
        
        # For all the win states, return the action leading to the win state with the best score
        while win_state_list:
            max_score = 0
            for win_pair in win_state_list:
                if scoreEvaluation(win_pair[0]) > max_score:
                    max_score = scoreEvaluation(win_pair[0])
                    bestAction = win_pair[1]
            return bestAction
        
        # Sort the list of leaves in increasing order of cost of the node
        leaf_list.sort(key=lambda tuples: tuples[2])

        # Return best action
        bestAction = leaf_list[0][1]
        return bestAction



        #return Directions.STOP

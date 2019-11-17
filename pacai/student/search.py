from pacai.util.stack import Stack
from pacai.util.queue import Queue
from pacai.util.priorityQueue import PriorityQueue
"""
In this file, you will implement generic search algorithms which are called by Pacman agents.
"""
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    ```
    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    ```
    """
    explored = []
    path = []
    fringe = Stack()
    fringe.push((problem.startingState(), 'SELF', 0))
    while (not fringe.isEmpty()):
        currentNode = fringe.pop()
        if (currentNode[0] not in explored):
            if (len(path) > 0):
                prevNode = path[-1]
            path.append(currentNode)
            explored.append(currentNode[0])
            if (problem.isGoal(currentNode[0])):
                solution = []
                for _, dir, _ in path:
                    if (dir != 'SELF'):
                        solution.append(dir)
                return(solution)
            successorStates = problem.successorStates(currentNode[0])
            if (len(path) > 1):
                adjListCurrentNode = []
                for state, _, _ in successorStates:
                    adjListCurrentNode.append(state)
                if (prevNode[0] not in adjListCurrentNode):
                    j = len(path) - 2
                    state = path[j]
                    count = 0
                    while(state[0] not in adjListCurrentNode):
                        count += 1
                        j = j - 1
                        state = path[j]
                    for i in range(0, count + 1):
                        del path[-1]
                    path.append(currentNode)
        for successor in successorStates:
            if (successor[0] not in explored):
                fringe.push(successor)
    return([])
    raise NotImplementedError()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """
    explored = []
    path = []
    fringe = Queue()
    memSuccessorStates = {}
    fringe.push((problem.startingState(), 'SELF', 0))
    while (not fringe.isEmpty()):
        currentNode = fringe.pop()
        path.append(currentNode)
        successorStates = problem.successorStates(currentNode[0])
        states = []
        for state, _, _ in successorStates:
            states.append(state)
        memSuccessorStates[currentNode[0]] = states
        for successor in successorStates:
            if(successor[0] not in explored):
                if (problem.isGoal(successor[0])):
                    deleteNodes = []
                    includeNode = path[-1]
                    for j in range(1, len(path)):
                        revIndex = len(path) - j - 1
                        currNode = path[revIndex]
                        if (includeNode[0] in memSuccessorStates[currNode[0]]):
                            includeNode = path[revIndex]
                        else:
                            deleteNodes.append(path[revIndex])
                    solution = []
                    for node in path:
                        if (node not in deleteNodes):
                            if (node[1] != 'SELF'):
                                solution.append(node[1])
                    solution.append(successor[1])
                    return (solution)
                fringe.push(successor)
                explored.append(successor[0])
    return ([])

    raise NotImplementedError()

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    # *** Your Code Here ***
    explored = []
    path = []
    fringe = PriorityQueue()
    memSuccessorStates = {}
    fringe.push((problem.startingState(), 'SELF', 0), 0)
    while (not fringe.isEmpty()):
        currentNode = fringe.pop()
        path.append(currentNode)
        successorStates = problem.successorStates(currentNode[0])
        states = []
        for state, _, _ in successorStates:
            states.append(state)
        memSuccessorStates[currentNode[0]] = states
        for successor in successorStates:
            if(successor[0] not in explored):
                if (problem.isGoal(successor[0])):
                    deleteNodes = []
                    includeNode = path[-1]
                    for j in range(1, len(path)):
                        revIndex = len(path) - j - 1
                        currNode = path[revIndex]
                        if (includeNode[0] in memSuccessorStates[currNode[0]]):
                            includeNode = path[revIndex]
                        else:
                            deleteNodes.append(path[revIndex])
                    solution = []
                    for node in path:
                        if (node not in deleteNodes):
                            if (node[1] != 'SELF'):
                                solution.append(node[1])
                    solution.append(successor[1])
                    return (solution)
                fringe.push(successor, successor[2])
                explored.append(successor[0])
    return ([])
    raise NotImplementedError()

def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # *** Your Code Here ***
    explored = []
    path = []
    fringe = PriorityQueue()
    memSuccessorStates = {}
    fringe.push((problem.startingState(), 'SELF', 0), 0)
    while (not fringe.isEmpty()):
        currentNode = fringe.pop()
        path.append(currentNode)
        successorStates = problem.successorStates(currentNode[0])
        states = []
        for state, _, _ in successorStates:
            states.append(state)
        memSuccessorStates[currentNode[0]] = states
        for successor in successorStates:
            if(successor[0] not in explored):
                if (problem.isGoal(successor[0])):
                    deleteNodes = []
                    includeNode = path[-1]
                    for j in range(1, len(path)):
                        revIndex = len(path) - j - 1
                        currNode = path[revIndex]
                        if (includeNode[0] in memSuccessorStates[currNode[0]]):
                            includeNode = path[revIndex]
                        else:
                            deleteNodes.append(path[revIndex])
                    solution = []
                    for node in path:
                        if (node not in deleteNodes):
                            if (node[1] != 'SELF'):
                                solution.append(node[1])
                    solution.append(successor[1])
                    return (solution)
                fringe.push(successor, successor[2] + heuristic(successor[0], problem))
                explored.append(successor[0])
    return ([])
    raise NotImplementedError()

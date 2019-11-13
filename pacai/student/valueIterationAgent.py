from pacai.agents.learning.value import ValueEstimationAgent
from pacai.util import counter

class ValueIterationAgent(ValueEstimationAgent):
    """
    A value iteration agent.

    Make sure to read `pacai.agents.learning` before working on this class.

    A `ValueIterationAgent` takes a `pacai.core.mdp.MarkovDecisionProcess` on initialization,
    and runs value iteration for a given number of iterations using the supplied discount factor.

    Some useful mdp methods you will use:
    `pacai.core.mdp.MarkovDecisionProcess.getStates`,
    `pacai.core.mdp.MarkovDecisionProcess.getPossibleActions`,
    `pacai.core.mdp.MarkovDecisionProcess.getTransitionStatesAndProbs`,
    `pacai.core.mdp.MarkovDecisionProcess.getReward`.

    Additional methods to implement:

    `pacai.agents.learning.value.ValueEstimationAgent.getQValue`:
    The q-value of the state action pair (after the indicated number of value iteration passes).
    Note that value iteration does not necessarily create this quantity,
    and you may have to derive it on the fly.

    `pacai.agents.learning.value.ValueEstimationAgent.getPolicy`:
    The policy is the best action in the given state
    according to the values computed by value iteration.
    You may break ties any way you see fit.
    Note that if there are no legal actions, which is the case at the terminal state,
    you should return None.
    """

    def __init__(self, index, mdp, discountRate = 0.9, iters = 100, **kwargs):
        super().__init__(index)
        self.mdp = mdp
        self.discountRate = discountRate
        self.iters = iters
        self.kthIteration = []
        self.policy = {}
        # Compute the values here.
        v_0 = {}
        iterationK = 1
        for state in self.mdp.getStates():
            v_0[state] = 0
        self.kthIteration.append(v_0)
        while (iterationK <= self.iters):
            self.kthIteration.append({})
            # save memory by keeping k and k+1 in memory only
            while (len(self.kthIteration) >= 3):
                del self.kthIteration[0]
            for state in self.mdp.getStates():
                vList = []
                bestAct = None
                currentMax = float('-inf')
                for action in self.mdp.getPossibleActions(state):
                    qVal = self.getQValue(state, action)
                    vList.append(qVal)
                    if qVal > currentMax:
                        currentMax = qVal
                        bestAct = action 
                self.policy[state] = bestAct  
                if (len(vList) > 0):
                    self.kthIteration[-1][state] = max(vList)
                else:
                    self.kthIteration[-1][state] = self.kthIteration[-2][state]
            iterationK += 1

    def getValue(self, state):
        """
        Return the value of the state (computed in __init__).
        """
        return self.kthIteration[-1][state]

    def getAction(self, state):
        """
        Returns the policy at the state (no exploration).
        """
        return self.getPolicy(state)

    def getQValue(self, state, action):
        QValue = 0
        for nextState, probability in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, nextState)
            vNextState = self.kthIteration[-2][nextState]
            QValue += probability * (reward + (self.discountRate * vNextState))
        return QValue

    def getPolicy(self, state):
        return (self.policy[state])

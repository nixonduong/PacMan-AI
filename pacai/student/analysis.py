"""
Analysis question.
Change these default values to obtain the specified policies through value iteration.
If any question is not possible, return just the constant NOT_POSSIBLE:
```
return NOT_POSSIBLE
```
"""

NOT_POSSIBLE = None

def question2():
    """
    [Enter a description of what you did here.]
    I set the noise to 0 so that the agent ends up
    in the intended successor state when they perform
    an action
    """

    answerDiscount = 0.9
    answerNoise = 0.0

    return answerDiscount, answerNoise

def question3a():
    """
    [Enter a description of what you did here.]
    All I did here was decrease the living reward. When
    the living reward is negative, you force the agent to
    find the closest solution
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = -2.0

    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    """
    [Enter a description of what you did here.]
    Increased the default noise to 0.4 so that the agent
    is scared to take riskier paths. Therefore causing our
    agent to take the longer and safer path. Decreased living
    reward so that the agent finds the closer solution.
    """

    answerDiscount = 0.7
    answerNoise = 0.4
    answerLivingReward = -1.5

    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    """
    [Enter a description of what you did here.]
    Decreased to noise to 0.0. This makes the agent safe
    taking paths closer to the cliff since the agent is
    fully in control of their successor state. Decreased
    living reward to -1 so that agent finds the closer solution.
    """

    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = -1.0

    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    """
    [Enter a description of what you did here.]
    Default arguments already prefer distant exit +10
    and avoid cliff
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    """
    [Enter a description of what you did here.]
    Default arguments already avoid both exits and
    cliffs
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward

def question6():
    """
    [Enter a description of what you did here.]
    """

    answerEpsilon = 0.3
    answerLearningRate = 0.5

    return answerEpsilon, answerLearningRate

if __name__ == '__main__':
    questions = [
        question2,
        question3a,
        question3b,
        question3c,
        question3d,
        question3e,
        question6,
    ]

    print('Answers to analysis questions:')
    for question in questions:
        response = question()
        print('    Question %-10s:\t%s' % (question.__name__, str(response)))

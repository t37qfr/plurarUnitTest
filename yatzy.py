def dice_counts(dice):
    '''
    >>> dice_counts([1,2,2,3,3])
    {1: 1, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}
    '''
    return  {x:dice.count(x) for x in range(1,7)}

def small_straight(dice):
    '''Score the given roll in the SMALL Straight
    
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0
    >>> small_straight({1,2,3,4,5})
    15
    >>> small_straight([5,4,3,2,1])
    15
    '''
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0
    
    
def yatzy(dice):
    '''
    >>> yatzy([1,1,1,1,1])
    50
    >>> yatzy([4,4,4,4,4])
    50
    >>> yatzy([4,4,4,4,1])
    0
    '''
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0
    
def full_house(dice):
    '''
     >>> full_house([1,1,2,2,2])
     8
     >>> full_house([6,6,6,2,2])
     22
     >>> full_house([1,2,3,4,5])
     0
     >>> full_house([1,2,2,1,3])
     0
    '''
    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0
 
    
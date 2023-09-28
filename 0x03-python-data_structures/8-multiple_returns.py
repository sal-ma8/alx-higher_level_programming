#!/usr/bin/python3
def multiple_returns(sentence):
    """
    hthhe jfhs,nr 
    fkkson dhfdjvdv
    kd jbfdknvkfjmvnllk,l,
    """

    if len(sentence) == 0:
        return (0, None)
    else:
        return len(sentence), sentence[0]

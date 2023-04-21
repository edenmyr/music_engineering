import numpy as np


def genNotes(n, octFreq=3):
    """
    Function for generating the notes
    Input:
    - n: number of notes in the octave
    Output: 
    - notes: list of 
    """
    notes = [3**(i/n) for i in range(n)]
    return notes

def easyFractions(N,eps=1e-6):
    """
    Code for finding the most basic fractions. 
    Input:
    - N: Highest value for the denominator
    - eps=1e-6: Tolerance for comparison
    Output:
    - sortedFrac: Sorted list of floats, with value <= 1.
    - sortedExactFrac: Sorted list of tuples, sorted in the same way as sortedFrac. 
                       Meant to be an exact representation of the fraction. 
    """
    frac = [1]
    exactFrac = [(1,1)]
    for i in range(N):
        for j in range(i):
            temp = (j+1)/(i+1)
            if not any(np.abs(temp-f) < eps for f in frac):
                frac.append(temp)
                exactFrac.append((j+1,i+1))
    #sortedFrac = sorted(frac)
    # https://stackoverflow.com/questions/6618515/sorting-list-according-to-corresponding-values-from-a-parallel-list
    #sortedExactFrac = [ef for _,ef in sorted(zip(frac,exactFrac))]
    #print(sortedFrac)
    #print(sortedExactFrac)
    return frac, exactFrac#sortedFrac, sortedExactFrac

def closestRelation(notes, fractions,cent_tol=25):
    """
    Function for finding the closest fraction relations for every note in the octave.
    Input:
    - notes: List of frequencies for the notes in the octave.
    - fractions: List of fractions, here >=1.
    - tol=0.01: Tolerance for where we find the note close enough to a fraction. 
    Output: 
    - closest: List of fracions closest to each note.
    - deviation: List of difference between each note and its closest fraction.
    - idx: List of indices for which element in the fractions list is closest to each note
           (should prob. add that step to this function and just return exactFracs for the elems)
    """
    closest = []
    cent_deviation = []
    idx = []
    for note in notes:
        for f in fractions:
            if np.abs(1200 * np.log(note/f)/np.log(2)) < cent_tol:
                closest.append(f)
                cent_deviation.append(1200 * np.log(f/note))
                idx.append(fractions.index(f))
                break
        if len(closest) != notes.index(note)+1:
            print("Not found for note " + str(note)) # HERE WE HAVE AN ERROR, IF IT DOESN'T FIND IT FOR ONE IT WILL PRINT THIS FOR THE REST OF THE LOOP
        #else:
        #    print("Found for note " + str(note))
    #devCents = deviation
    return closest, cent_deviation, idx

notes = genNotes(8)
print(notes)

frac, exactFrac = easyFractions(20)

invFrac = [1/f for f in frac]

closest, dev, idx = closestRelation(notes, invFrac)
print(closest)

exFracs = [exactFrac[i] for i in idx]
print(exFracs)
print(dev)
#tol = 2^20/1200 # given by deviation of 20 cents, as in ordinary 12 tone 


# generera lista med inverterade förhållanden
# spara cent för alla toner, exakta och approximerade

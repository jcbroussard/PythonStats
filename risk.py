"""
This file contains code to calculate the
probability of first-borns, other and all
children being born early, on-time or late.
"""

import survey
import first_solutions
import Pmf
import operator
import matplotlib

def ProbEarly(PMF):
    pmfDict = PMF.GetDict()
    eProb = 0
    for key, val in pmfDict.items():
        if key < 38: eProb += val

    return eProb

def ProbOnTime(PMF):
    pmfDict = PMF.GetDict()
    onTimeProb = 0
    for key, val in pmfDict.items():
        if key in [38,39,40]: onTimeProb += val

    return onTimeProb

def ProbLate(PMF):
    pmfDict = PMF.GetDict()
    lProb = 0
    for key, val in pmfDict.items():
        if key > 40: lProb += val

    return lProb

def GetPmfs(data_dir):
    """
    Gets PMFs of pregnancy length for firsts, others
    and all pregnancies resulting in live-births.
    """
    
    table, firsts, others = first_solutions.MakeTables(data_dir)
    first_solutions.ProcessTables(firsts, others)

    # Gets list of firsts pregnancy length
    firstLength = []
    for b in firsts.records:
        firstLength.append(b.prglength)

    otherLength = []
    for b in others.records:
        otherLength.append(b.prglength)

    allLength = firstLength + otherLength

    firstLengthPmf = Pmf.MakePmfFromList(firstLength)
    otherLengthPmf = Pmf.MakePmfFromList(otherLength)
    allLengthPmf = Pmf.MakePmfFromList(allLength)

    return firstLengthPmf, otherLengthPmf, allLengthPmf

def main(name, data_dir='.'):
    firstPmf, otherPmf, allPmf = GetPmfs(data_dir)
    print 'Probability that first-borns will be early:', round(ProbEarly(firstPmf),3)
    print 'Probability that non-first-borns will be early:', round(ProbEarly(otherPmf),3)
    print 'Probability that all live-briths will be early:', round(ProbEarly(allPmf),3)
    print
    print 'Probability that first-borns will be on time:', round(ProbOnTime(firstPmf),3)
    print 'Probability that non-first-borns will be on time:', round(ProbOnTime(otherPmf),3)
    print 'Probability that all live-briths will be on time:', round(ProbOnTime(allPmf),3)
    print
    print 'Probability that first-borns will be late:', round(ProbLate(firstPmf),3)
    print 'Probability that non-first-borns will be late:', round(ProbLate(otherPmf),3)
    print 'Probability that all live-briths will be late:', round(ProbLate(allPmf),3)
    print
    print 'The relative risk of first-borns coming early is:', round(ProbEarly(firstPmf)/ProbEarly(otherPmf),3)



if __name__ == '__main__':
    import sys
    main(*sys.argv)

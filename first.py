import survey

# copying Mean from thinkstats.py so we don't have to deal with
# importing anything in Chapter 1

def Mean(t):
    """Computes the mean of a sequence of numbers.

    Args:
        t: sequence of numbers

    Returns:
        float
    """
    return float(sum(t)) / len(t)

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirths = survey.Pregnancies()
firsts = survey.Pregnancies()
others = survey.Pregnancies()
firstPregLengths = []
otherPregLengths = []

for p in table.records:
    if p.outcome == 1:
        liveBirths.AddRecord(p)
        
        if p.birthord == 1:
            firsts.AddRecord(p)
            firstPregLengths.append(p.prglength)
        else:
            others.AddRecord(p)
            otherPregLengths.append(p.prglength)

avgFBP = Mean(firstPregLengths)
avgOBP = Mean(otherPregLengths)

print 'Number of live births', len(liveBirths)
print 'Number of first borns', len(firsts)
print 'Number of non-first borns', len(others)
print 'Average pregnancy length, in weeks, of first borns', avgFBP
print 'Average pregnancy length, in weeks, of non-first borns', avgOBP


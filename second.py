import survey
import first_solutions
import Pmf
import operator

first_solutions.Summarize('.')

def Mode(HistObj):
    modeVal = None
    modeFreq = None
    for val, freq in HistObj.Items():
        if freq > modeFreq: modeVal, modeFreq = val, freq
    return modeVal
            
def AllModes(HistObj):
    HistObjDict = HistObj.GetDict()
    return sorted(HistObjDict.iteritems(),key=operator.itemgetter(1), reverse=True)

def standardDev(data_dir):
    """
    Prints summary stabdard deviation for first babies and others.
    """

    table, firsts, others = first_solutions.MakeTables(data_dir)
    first_solutions.ProcessTables(firsts, others)
    
    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:' 
    print 'First babies', mu1 
    print 'Others', mu2
    
    print 'Difference in days', (mu1 - mu2) * 7.0
    print

    sigmasq1 = 0
    for b in firsts.records:
        sigmasq1 =+ pow(mu1 - b.prglength,2)
    sigmasq1 /= firsts.n
    stddev1 = pow(sigmasq1,0.5)

    sigmasq2 = 0
    for b in others.records:
        sigmasq2 =+ pow(mu2 - b.prglength,2)
    sigmasq2 /= others.n
    stddev2 = pow(sigmasq2,0.5)

    print 'Variance:'
    print 'First babies:', sigmasq1
    print 'Others:', sigmasq2
    print
    print 'Std Dev:'
    print 'First babies:', stddev1
    print 'Others:', stddev2

def main(name, data_dir='.'):
    standardDev(data_dir)
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)

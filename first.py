import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirths = survey.Pregnancies()
firsts = survey.Pregnancies()
others = survey.Pregnancies()

for p in table.records:
    if p.outcome == 1:
        liveBirths.AddRecord(p)
        
        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)
    
print 'Number of pregnancies', len(liveBirths)
print 'Number of first borns', len(firsts)
print 'Number of non-first borns', len(others)

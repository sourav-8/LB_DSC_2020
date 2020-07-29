import survey
table = survey.Pregnancies()
table.ReadRecords()
print ('Number of pregnancies %s'%len(table.records))
print(table.records.nbrnaliv)


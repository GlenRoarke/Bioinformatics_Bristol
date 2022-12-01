    
# SeqIO Parsing a Sequence File
# Parsing with LCT homologs
from Bio import SeqIO
# Parse is required when multiple sequences are present in a single file
myIDs = []  #  Summary of IDs in a list

my_dict
for i, getRecord in enumerate(SeqIO.parse("ppmerge_peptide.pep", "fasta")):   # get a counter and the value from the iterable
    print("Sequence:", i+1) # Number of Seq in file
    print(getRecord.id)  # accessionNo of the different
    #print(getRecord.seq)  # Actual sequence in the file being checked.S
    print(getRecord.description)
    print(len(getRecord.seq))
    myIDs.append(getRecord.id)



print(myIDs[:10])




with open('rosalind_dna.txt','r') as inp:
    with open('output_dna.txt','w') as out:
        mySeq = inp.readline()
        out.write(str(mySeq.count('A')) + ' ' + str(mySeq.count('C')) + ' ' + str(mySeq.count('G')) + ' ' + str(mySeq.count('T')))
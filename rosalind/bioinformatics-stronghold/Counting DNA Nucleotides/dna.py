with open('rosalind_dna.txt','r') as inp:
    with open('output_dna.txt','w') as out:
        mySeq=inp.readline()
        a=str(mySeq.count('A'))
        out.write(a+' '+str(mySeq.count('C'))+' '+str(mySeq.count('G'))+' '+str(mySeq.count('T')))
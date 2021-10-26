#!/usr/local/bin/python3
#Script for mission1, exercise, Lect_11
#input the raw file
plg=open('plain_genomic_seq.txt').read()

#change the base pair letter case
plglo=plg.replace('A','a')
plglo=plg.replace('T','t')
plglo=plg.replace('G','g')
plglo=plg.replace('C','c')

#keep the base pair
import string
trans=str.maketrans('','',string.ascii_uppercase)
#delete the capital letter
plglow=plglo.translate(trans)

#obtained the genomic sequence
plgup=plglow.upper()

#Then print into different files as requirement.
#exon1 is the file with the first exon.
exon1=plgup[:64]
#exon2 is the file with the second exon.
exon2=plgup[91:]
exon_1=open('exon1','w')
exon_2=open('exon2','w')
exon_1.write(exon1)
exon_2.write(exon1)

#output files of exons
exon_1.close()
exon_2.close()

#output file of coding_parts 
code=open('coding_parts','w')
code1=exon1+exon2
code.write(code1)
code.close()

#Then non-coding_parts
noncoding_parts=open('non-coding_parts','w')
noncoding=plgup.replace('exon1','')
noncoding=plgup.replace('exon2','')
noncoding_parts.write(noncoding)
noncoding_parts.close()

#Make them tidy
import os
os.renames('exon1','Mission1')
os.renames('exon2','Mission1')
os.renames('coding_parts','Mission1')
os.renames('non-coding_parts','Mission1')

#And give the sign of finish
print('End')

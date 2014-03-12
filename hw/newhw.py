#!/usr/bin/python

import re
import os
import sys
import datetime




os.makedirs(sys.argv[1])
os.chdir(sys.argv[1])
os.system('wget http://www.math.wisc.edu/~miller/m542/alg.tex')


dayvalue = ['Mon','Tue','Wed','Thurs','Fri','Sat']

monthvalue = ['Dummy','Jan','Feb','Mar']

currdate = map(int,sys.argv[1].split('.'))

d = datetime.date(2014,currdate[0],currdate[1])

dayofweek = d.weekday()

inprob = False

correctprob = False

problemtextbuffer = ''

problemtext = ''

print 'Looking for: ' + '('+str(dayvalue[dayofweek])+'.'+str(monthvalue[currdate[0]])+'.'+str(currdate[1]-7)+')'

with open('alg.tex','r') as alg:
    for line in alg:
        if re.search('\\\\begin{prob}',line):
            problemtextbuffer+=line
        if re.search('('+str(dayvalue[dayofweek])+'.'+str(monthvalue[currdate[0]])+'.'+str(currdate[1]-7)+')',line) or correctprob:
            problemtextbuffer+=line
            correctprob = True
        if re.search('\\\\end{prob}',line):
            if correctprob == False:
                problemtextbuffer = ''
            else:
                problemtext += problemtextbuffer
                problemtextbuffer = ''
                correctprob = False
        

print 'Problem text:' + problemtext

with open('hw'+str(sys.argv[1])+'.tex', 'w') as fout:
    with open('/Users/taylorlee/UW/math542/hw/542template.tex','r') as fin:
        for line in fin:
            fout.write(line.replace('DATE','\\formatdate{'+str(currdate[1])+'}{'+str(currdate[0])+'}{2014}').replace('PROBLEMS',problemtext))

os.system('pdflatex hw'+str(sys.argv[1])+'.tex')


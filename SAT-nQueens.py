# !wget https://www.labri.fr/perso/lsimon/option-ia/Search/Master-Class-SAT/pysat.zip
# !unzip -o pysat
# !mv lorensi-pysat-8625ab1d6cdf/src/* .

def gen_cnf(n):
    cnf=[]
    queen=[]
    # gen variables
    for i in range (n):
      rowQueen=[]
      for j in range (n):
        rowQueen.append ((i*n+j+1))
      queen.append(rowQueen)
    # at least one queen per row and col
    for i in range(n):
        queenInRow=[]
        queenInCol=[]
        for j in range(n):
            queenInRow.append(queen[i][j])
            queenInCol.append(queen[j][i])
        cnf.append(queenInRow)
        cnf.append(queenInCol)
    # only one queen per row / col
    for i in range (n):
        for j in range(n):
            for k in range(j+1,n):
              cnf.append([-queen[i][j],-queen[i][k]])
    for i in range (n):
        for j in range(n):
            for k in range(i+1,n):
              cnf.append([-queen[i][j],-queen[k][j]])
    # only one queen per diag
    for i in range (n):
        for j in range (n):
          for k in range (1,n):
            if (i+k<n and j+k<n):
              cnf.append([-queen[i][j],-queen[i+k][j+k]])
            if (i-k>=0 and j+k<n):
              cnf.append([-queen[i][j],-queen[i-k][j+k]])
    return cnf

from pysat import Solver

n = 8
cnf = gen_cnf(n)
print(cnf)

s=Solver()
for i in cnf:
  s.addClause(i)
s.buildDataStructure()
s.solve()

solution = s.finalModel
print(solution)
 
queen=[]
for i in range (n):
  rowQueen=[]
  for j in range (n):
    rowQueen.append (0)
  queen.append(rowQueen)

for i in solution:
    if i >0:
      x=i
      queen[(x-1)//n][(x-1)%n]="Q"
    else:
      x=int(-i)
      queen[(x-1)//n][(x-1)%n]="-"

for i in queen :
  print (i)


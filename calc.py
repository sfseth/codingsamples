#!/usr/bin/python

import sys


# TODO objectify this stuff, global methods for now
def mult(valA, valB):
  return valA * valB

def div(valA, valB):
  return valA / valB

def add(valA, valB):
  return valA + valB

def subt(valA, valB):
  return valA - valB

# global constants
i = 0


def computeIntermediate(innerList, i):
  tempres = []
  # TODO there's a bug in the indexing of the recursion here that needs fixing
  for arg in innerList:
    if arg.isdigit():
      lastVal = int(arg)
    elif arg == '*':
      tempres.append(mult(lastVal, int(innerList[i+1])))
    elif arg == '/':
      tempres.append(div(lastVal, int(innerList[i+1])))
    elif arg == '+':
      tempres.append(add(lastVal, int(innerList[i+1])))
    elif arg == '-':
      tempres.append(subt(lastVal, int(innerList[i+1])))
    i += 1
  print int(len(innerList))
  if len(tempres) > 1:
    return computeIntermediate(tempres, i)
    #return computeIntermediate(innerList, i)
  elif int(len(innerList)) == 0:
    return 'Error : must supply numbers to operate on'
  else:
    return tempres[0]

def unitTests():
  # TODO cant remember syntax of negative assertions, come back to these
  assert(add(1,1)==2)
  #assertRaises(add(1,2)==2)
  assert(subt(3,1)==2)
  #assertRaises(subt(3,1)==2)
  assert(mult(1,2)==2)
  #assertRaises(mult(1,3)==2)
  assert(div(8,4)==2)
  #assertRaises(div(9,1)==2)

if __name__ == '__main__':
  # basic unit tests to start
  unitTests()

  # dont pass in the name of the program as an argument
  print(computeIntermediate(sys.argv[1:], i))


         


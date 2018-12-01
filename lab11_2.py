#!/usr/bin/env python3

X = 0

def fillZeros(s : str, size : int) -> str:
  if len(s) >= size:
    return s[:size]
  for i in range(len(s),size):
    s = "0" + s
  return s

def Rand(seed : int  = 0) ->int:
  global X
  if(seed != 0):
    X = fillZeros(str(seed),6)
  X = fillZeros(str(X), 6)
  Y = int((X)[3:6] + (X)[:3])
  Sum = fillZeros(str(int(X) * int(Y)), 12)
  X = int(Sum[3:6]+Sum[6:9])
  return X

print(Rand(int(input("Seed"))))
for i in range(0,14):
  print(Rand())

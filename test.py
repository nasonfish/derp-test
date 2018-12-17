# do the execution/evaluation

successes = []

for i in range(1,0xFFFFFFFF):
    success = bitSplit(i) == 1235354
    if success:
      successes.append(i)

if len(successes) == 0xFFFFFFFF:
  return 100
else:
  return(successes/0xFFFFFF, "You succeeded the following test cases", successes)

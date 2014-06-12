perms = permutations(range(0,4))
for p in perms:
   print p
   gifted = [0 for i in range(0, 4)]
   for i in range(0, 4):
     neighbors = g.neighbors(i)
     print neighbors
     giftedID = max([p[j] for j in neighbors])
     print giftedID
     print [p[j] for j in neighbors]
     giftedCoworker = [j for j in neighbors if p[j] == giftedID]
     print giftedCoworker
     giftedCoworker = giftedCoworker[0]
     print giftedCoworker
     gifted[giftedCoworker] = 1
   print "gifted indicators"
   print gifted
   try:
     total = total + len(gifted)
     total_gifted = total_gifted + sum(gifted)
   except:
     total = len(gifted)
     total_gifted = sum(gifted)

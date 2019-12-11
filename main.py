


names = ['hello','lol', 'bob']

def stuff(names):
  pairs = []
  for i in range(len(names)-1):
    pairs.append([names[i], names[i+1]])
  pairs.append([names[0],names[-1]])
  return pairs


print (stuff(names))


  
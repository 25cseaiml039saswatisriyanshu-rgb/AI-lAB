#-------alpha-beta--------
import math
def alpha_beta(depth,nodeIndex,MaximizePlayer,values,alpha,beta,height):
  #base case : leafnode reached
  if depth==height:
    return values[nodeIndex]
  if MaximizePlayer:
    best= -math.inf

    for i in range(0,2):
      val=alpha_beta(depth+1,nodeIndex*2+i,False,values,alpha,beta,height)
      best=max(best,val)
      alpha=max(alpha,best)

      #beta cut-off
      if beta<=alpha:
        break
    return best
  else:
    best=math.inf
    for i in range(2):
      value=alpha_beta(depth+1,nodeIndex*2+i,True,values,alpha,beta,height)
      best=min(best,value)
      beta=min(beta,best)

      #alpha cut-off
      if beta<=alpha:
        break
    return best
#main program
values=list(map(int,input("enter 8 leaf node values:").split()))
height=3
result=alpha_beta(0,0,True,values,-math.inf,math.inf,height)
print("\nThe optimal value is:",result)
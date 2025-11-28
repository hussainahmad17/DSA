def task(ind,total,brackets,result):
    if ind >= len(brackets):
        result.append("".join(brackets))
        return
    if total > (brackets)//2:
        return
    if total < 0:
        return
    
    brackets[ind] = "("
    sum=total+1
    task(ind+1,sum,brackets,result)
    brackets[ind]= ")"
    sum=total-1
    task(ind+1,sum,brackets,result)
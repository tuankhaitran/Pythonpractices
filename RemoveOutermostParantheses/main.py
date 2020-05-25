# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
S= "(()())(())"
a="0123456789"

print(a[1:-1])
def removeOuterParentheses(S: str):
    count=1 # count start as 1 because the first index of every decomposition will always be '(' so count increase 1
    resultstring=""
    i=1 # Start with i = 1 because the first index or every decomposition will always be '(' and we will not take that in our result string
    while i < len(S):
        if S[i]=='(':
            count+=1
        else:
            count-=1    
        if count==0:  # If count = zero means we just found a valid parantheses so we should skip the next index because that next index will be a '(' and we dont want to that into our string anyway
            count=1 # set count = 1 again because we gonna skip the next index which will be the '('
            i+=2 # i increases by 2 to skip the next index
            print(resultstring)
            continue # continue so that we are not gonna execute 2 below command to put this value into our result string because it is surely the outer ')'
        resultstring+=S[i]
        i+=1

    return resultstring

print(removeOuterParentheses(S))


a=['1','2','1','2','1','2','1','2']
a=a[::-1]
print(a)
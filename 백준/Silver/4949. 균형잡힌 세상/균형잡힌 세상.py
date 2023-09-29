while(1):
    line=input()
    line_1=list(line)
    stack=[]
    temp=True

    if(line=='.'):
        break
    for i in line_1:
        if(i=='(' or i=='['):
            stack.append(i)
        elif(i==')'):
            if not stack or stack[-1]=='[':
                temp=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif(i==']'):
            if not stack or stack[-1]=='(':
                temp=False
                break
            elif stack[-1]=='[':
                stack.pop()
    if temp==True and not stack:
        print("yes")
    else:
        print("no")
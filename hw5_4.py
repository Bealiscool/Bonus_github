import math


#num_index=[]
content='0123456789+-*/().'
numbers='0123456789'
def calculate(sub_eqn):
    operator_index=[]
    operator=[]
    num=[]
    for i in range(len(sub_eqn)):
        if sub_eqn[i] not in content:
            print("Error: Unsupported character error")
            return False
    for i in range(len(sub_eqn)): #find operators 
        if sub_eqn[i]=='+':
            operator_index.append(i)
            operator.append('+')
        elif sub_eqn[i]=='-':
            operator_index.append(i)
            operator.append('-')
        elif sub_eqn[i]=='*':
            operator_index.append(i)
            operator.append('*')
        elif sub_eqn[i]=='/':
            operator_index.append(i)
            operator.append('/')
    
    for i in range(len(operator_index)):
        if operator_index[0]==0:# if operator at first means error
            print("Error: Operand error")
            return False
        if operator_index[i]+1 < len(sub_eqn):
            if sub_eqn[operator_index[i]+1] not in numbers:
                print("Error: Operand error")
                return False
        elif operator_index[i] == len(sub_eqn)-1:
            print("Error: Operand error")
            return False
    if len(operator)==0:
        result=float(sub_eqn)
        return result
    for i in range(len(operator_index)):# find numbers
        if i==0:
            index=operator_index[0]
            num.append(float(sub_eqn[0:index]))
        if i==len(operator_index)-1:
            index=operator_index[-1]
            num.append(float(sub_eqn[index+1:]))
        else:
            index1=operator_index[i]
            index2=operator_index[i+1]
            num.append(float(sub_eqn[index1+1:index2]))

    total_eqn=[] #seperate operator and numbers in a single list
    for i in range(len(num)):
        total_eqn.append(num[i])
        if i < len(operator):
            total_eqn.append(operator[i])
    for i in range(len(total_eqn)):#remove division and substraction
        if total_eqn[i]=='/':
            total_eqn[i]='*'
            if total_eqn[i+1]>0:  
                total_eqn[i+1]=1/total_eqn[i+1]
            else:
                print("Error: Division by zero")
                return False
        if total_eqn[i]=='-':
            total_eqn[i]='+'
            total_eqn[i+1]=0-total_eqn[i+1]
    result=0
    num_mult=0
    num_adds=0
    for i in range(len(total_eqn)):
        if total_eqn[i]=='*':
            num_mult+=1
    for i in range(len(total_eqn)):
        if total_eqn[i]=='+':
            num_adds+=1
    
    while (num_mult>0):
        for i in range(len(total_eqn)):
            if total_eqn[i]=='*':
                num1=float(total_eqn[i-1])
                num2=float(total_eqn[i+1])
                result=num1*num2
                del total_eqn[i-1:i+2]
                total_eqn.insert(i-1,result)
                break
        num_mult-=1
    
    while (num_adds>0):
        for i in range(len(total_eqn)):
            if total_eqn[i]=='+':
                num1=float(total_eqn[i-1])
                num2=float(total_eqn[i+1])
                result=num1+num2
                del total_eqn[i-1:i+2]
                total_eqn.insert(i-1,result)
                break
        num_adds-=1
        

    return result

end=0       
while (end==0):
    
    eqn=input("Enter an expression to evaluate or 'q' to quit: ")
    if eqn=='q':
        break
    single_end=-1
    
    while (single_end<0):
        left_bracket_index=[]
        right_bracket_index=[]
        for i in range(len(eqn)):
            if eqn[i]=='(':
                left_bracket_index.append(i)
            elif eqn[i]==')':
                right_bracket_index.append(i)
                
        if len(left_bracket_index) != len(right_bracket_index):
            print("Error: Unbalanced parentheses")
            break
        if len(left_bracket_index)==0 and len(right_bracket_index)==0:
            if calculate(eqn)==False:
                break
            else:
                print("Result: ",calculate(eqn))
                break
        if left_bracket_index[-1] > right_bracket_index[0]:
            sub_eqn=eqn[left_bracket_index[-1]+1:right_bracket_index[1]]
        else:
            sub_eqn=eqn[left_bracket_index[-1]+1:right_bracket_index[0]]
        result=calculate(sub_eqn)
        if result==False and result!=0:
            break
        eqn_left1=eqn[0:left_bracket_index[-1]]
        eqn_left2=eqn[right_bracket_index[0]+1:]
        result_str=str(result)
        eqn=eqn_left1+result_str+eqn_left2
        #print("eqn_left",eqn)
    
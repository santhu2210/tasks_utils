def tokenList(s):
    s = s.replace(" ","")

    tokens = []
    i = 0
    while i< len(s):
        if s[i] == "*" or s[i] == '/' or s[i] == '^' or s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i = i+1

        elif s[i] == "+" or s[i] == "-":
            if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1] == ")"):
                tokens.append(s[i])
                i = i+1
            else:
                num = s[i]
                i = i + 1

                while i < len(s) and s[i] >= "0" and s[i] <="9":
                    num = num+s[i]
                    i = i + 1
                tokens.append(num)

        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
            tokens.append(num)

        else:
            return []

    return tokens
   
def infix_to_postfix(tokens):
    operators = []
    postfix = []
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    
    for tok in tokens:
        if tok.lstrip('+-').isdigit():
            postfix.append(tok)
     
        elif tok in ['+','-','*','/','^']:
            while len(operators) > 0 and operators[-1] != '(' and precedence[tok] < precedence[operators[-1]]:
                postfix.append(operators.pop())
            operators.append(tok)
        
        elif tok == '(':
            operators.append(tok)
        
        elif tok == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())            
            operators.remove('(')
    
    while len(operators) > 0:
        postfix.append(operators.pop())    
    
    return postfix

def eval_postfix(postfix_tokens):
    values = []
#     right = ''
#     left = ''
    
    for tok in postfix_tokens:
        if tok.lstrip('+-').isdigit():
            values.append(tok)
        else:
            right = values.pop()
            left = values.pop()
            result = eval(str(left)+str(tok)+str(right))
            values.append(result)
    
    return values[0]

def main():
    exp = input("Enter a Valid Mathematical Expression: ")
    tokens = tokenList(exp)
    postfix = infix_to_postfix(tokens)
    postfix_str = ''.join(postfix)
    final_value = eval_postfix(postfix)
    print("The Tokens are :", tokens) 
    print("The postfix are :", postfix) 
    print('The final_value :',final_value)            
    
    
if __name__ == "__main__":
    main()
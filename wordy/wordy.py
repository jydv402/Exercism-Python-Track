def answer(question):
    question = question.rstrip("?")
    statement = question.replace("What is ", "").replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").split()
    statement.insert(0 , "(")
    statement.insert(4 , ")")

    check = ['plus' , 'minus' , 'multiplied by' , 'divided by']
    opt = ['+', '-', '*', '/']

    if question == "What is":
        raise ValueError("syntax error")
    else:
        try:
            return eval(" ".join(statement))
        except:
            if not(opt[0] in statement or opt[1] in statement or opt[2] in statement or opt[3] in statement):
                raise ValueError("unknown operation")
            
            for item in question:
                if item not in check:
                    raise ValueError("syntax error")
                    
    
    

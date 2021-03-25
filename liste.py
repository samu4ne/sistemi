def push_ (stack, element):
    stack.append(element)

def pop_(stack):
    return stack.pop()

def main():
    pilaAlContr=[]
    pila= ["(": ")","[":"]", "{":"}"]
    for p in stringaControllo:
        if p=="(" or p=="[" or p=="{":
            push_(pilaContr, p)
        if p==")" or p=="]" or p=="}":
            if p.pop_()!=dizioPar[p]:
                print("errore nelle parentesi")
                return

if __name__== "__main__":
    main()

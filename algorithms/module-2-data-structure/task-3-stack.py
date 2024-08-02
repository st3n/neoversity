from queue import LifoQueue


def check_brackets(expression):
    stack = LifoQueue()
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.put(char)
        elif char in closing_brackets:
            if not stack:
                return "Несиметрично"
            elif opening_brackets.index(stack.get()) != closing_brackets.index(char):
                return "Несиметрично"

    if stack.empty():
        return "Симетрично"
    else:
        return "Несиметрично"


def main():
    expressions = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( [] 99 ( 2 - 3));", "( 17 }"]

    for expression in expressions:
        print(f"{expression}: {check_brackets(expression)}")


if __name__ == "__main__":
    main()

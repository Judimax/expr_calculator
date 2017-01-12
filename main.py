import Parsers
import os
def help():
    print("q -- quit")
    print("debug on-- turn on debug printing in print_eval")
    print("debug off -- turn off debug printing")
    print("help -- this message")
    print("? -- same as help")
    print("<filename -- read lines from a file whose name is filename")
    print("[anything else] -- sequence of expressions or assignment statements")
def main():
    global stop
    stop = 'green'
    x=0
    while stop != 'red' :
        expression = input("Enter program, or filename starting with < ")
        if expression == "q":
            break
        elif expression == "debug on":
            Parsers.debugging = True
        elif expression == "debug off":
            Parsers.debugging = False
        elif expression == "help" or expression == "?":
            help()
        elif expression.find("<") != -1:
            compute_files(expression)
        else:
            evaluate(expression)
                   
def compute_files(problem):
    problem = problem.strip("<")
    file = open(problem, 'r')
    expressions = file.readlines()
    for solve in expressions:
                solve = str(solve)
                solve = solve.strip("\n")
                print("Enter program, or filename starting with <   ",solve)
                if solve != "q":
                    if solve == "debug on":
                        Parsers.debugging = True
                    elif solve =="debug off":
                        Parsers.debugging = False
                    elif solve.find("<") != -1:
                        file_in_file = True
                        compute_files(solve)
                    else:
                        evaluate(str(solve))
                else:
                    global stop
                    stop = 'red'
    file.close()
    
def evaluate(s):
    for part in s.split(";"):
        if "=" in part:
            pieces= part.split("=")
            val = Parsers.parse_eval(pieces[1])
            Parsers.variables[pieces[0]] = val
        else:
            print(Parsers.parse_eval(part))
main()

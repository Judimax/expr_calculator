"""----------------------------------------------------------------------------
Assignment Name: Project 2
Assignment Author: Michael Odumosu
Date: 5/16/16
The purpose of this program is to behave like calucator that does basic mathematical
operations, along with variable assignments and retrivals. This program
takes an expersion written from user input and comes up with the correct answerwer
according to PEMDAS. If a variable equation is typed in, the experssion is
computed and its result is assigned to the variable. If a variable is typed
the number it is equal to is returned.
----------------------------------------------------------------------------------------"""
from Simplestack import *
import os
variables= dict(a=5,b=2,r=3,z=7)
debugging = True
def factorial(s):
    if s < 2:
        return s
    else:
        return s* factorial(s-1)
def evaluate_binary(value1, operator, value2):
    if operator == '^': operator = '**'
    s = str(value1) + operator + str(value2)
    return eval(s)
def is_number(s):
    legals = "0123456789."
    for ch in s:
        if ch not in legals:
            return False
    return True
def is_identifier(s):
    return s.isalpha()
def is_operator(s):
    return s in "+-*%/^!"
def expand(s):
    s += "$"
    news = ""
    NUMBERS = "0123456789"
    for i in range(len(s)-1):
        ch = s[i]
        nextch = s[i+1]
        if ch == '_':
            news += "0 - "
        elif is_operator(ch):
            if nextch != " ":
                news += ch + " "
            else:
                news += ch
        elif ch == " ":
            news += ch
        elif ch in NUMBERS and nextch not in NUMBERS:
            news += ch + " "
        elif ch.isalpha() and not nextch.isalpha():
            news += ch + " "
        elif ch == '(' or ch == ')':
            news += ch + " "
        else:
            news += ch
    return news
def operator_less_than(op1, op2):
    if op1 == "$":
        return True
    if op2 == "$":
        return False
    if op1 == '+' or op1 == '-':
        if op2 == '+' or op2 == '-':
            return False
        else:
            return True
    if op1 == '*' or op1 == '/':
        if op2 in ['+', '-', '*', '/', '%']:
            return False
        else:
            return True
    if op1 == '^':
        if op2 == "^" or op2 == '!':
            return True
        else:
            return False
    if op1 == '!':
        return False
def empty(L):
    return L == []
def head(L):
    return L[0]
def tail(L):
    return L[1:]
def remove_blanks(s):
    if len(s) == 0:
        return s
    elif head(s) == " ":
        return remove_blanks(tail(s))
    else:
         return head(s)+ remove_blanks(tail(s))
def parse_eval(s):
    try:
        global identifier
        identifier = 0
        if debugging == True:
            print("evaluating...",s)
        s = remove_blanks(s)
        s = expand(s+"$")
        tokens=  s.split(" ")
        if debugging == True:
            print("tokens=",tokens)
        opstack = Simplestack("$")
        numstack = Simplestack("$")
        while len(tokens) > 0:
                token = tokens[0]
                if debugging == True:
                    print("token =",token)
                    print("Num stack:",numstack)
                    print(" Op stack:",opstack)
                if identifier == 1:
                    opstack.pop()
                    identifier = 0
                if is_identifier(token):
                    if token in variables:
                        print("Found identifier...", token)
                        coord= variables[token]
                        token=str(coord)
                    else:
                        raise ParseError(token)
                        return
                if token == "!":
                    start= numstack.pop()
                    start= int(start)
                    multi= factorial(start)
                    numstack.push(multi)
                    opstack.push(token)
                    identifier =1
                    del tokens[0]
                elif token == '$':
                    while opstack.top() != '$':
                        num_ii= numstack.pop()
                        ops = opstack.pop()
                        num_i= numstack.pop()
                        answer= evaluate_binary(num_i, ops ,num_ii)
                        numstack.push(answer)
                        if debugging == True:
                            print("Evaluating:",num_i,ops,num_ii)
                    final= numstack.pop()
                    if debugging == True:
                        print('Returning result',final)
                        for value in variables.keys():
                            if s.find(str(value)) != -1:
                                print('dict is')
                                print(variables)
                    if opstack.top() == '$':
                        return final
                elif is_number(token):
                    numstack.push(float(token))
                    del tokens[0]
                elif is_operator(token):
                    if opstack.top() == '(':
                        opstack.push(token)
                        del tokens[0]
                    elif operator_less_than(opstack.top(),token):
                        if token == "!":
                            pass
                        opstack.push(token)
                        del tokens[0]
                    else:
                        num_ii= numstack.pop()
                        ops= opstack.pop()
                        num_i = numstack.pop()
                        answer= evaluate_binary(num_i,ops,num_ii)
                        numstack.push(answer)
                elif token == '(':
                    opstack.push(token)
                    del tokens[0]
                elif token == ')':      
                    if opstack.top() != '(' :
                        num_ii= numstack.pop()
                        ops= opstack.pop()
                        num_i = numstack.pop()
                        answer= evaluate_binary(num_i,ops,num_ii)
                        numstack.push(answer)
                        if debugging ==True:
                            print("Evaluating: ",num_i,ops,num_ii)
                    opstack.pop()       
                    del tokens[0]
                if debugging == True:
                    print("-----------------------------")
    except Exception as e:
        print ("Parse Error:  ERROR: Unassigned variable:",e)
        
class ParseError(Exception):
    def __init__(self,error):
        self.error= error

    def __str__(self):
        return self.error
        
    

    
        
        
												  
												  
					

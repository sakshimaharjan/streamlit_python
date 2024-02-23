import streamlit as st
def check_primenum(number):
    count = 0 
    prime = False
    for i in range(1, number+1):
        if(number % i == 0):
            count += 1
    if(count == 2):
        prime = True    
    return prime

def multiplicationtable(number):
    for i in range(1,11):
        st.write(f"{number} * {i} = {number*i}")

# def pass_to_func(x): 
#        return x**2+5*x+2

# def reverse_word(sentence):
#     words = sentence.split()
#     reversed_word = [word[::-1] for word in words][::-1]
#     reversed_sentence = ' '.join(reversed_word)
#     return reversed_sentence



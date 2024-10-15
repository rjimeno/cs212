#/usr/bin/env python3

import re

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in some order as parms of function. For example, 'YOU == ME**2' returns
    (lambda Y. M, E. U, ): (U+10*O+100*Y) == (E+10*M)**2, 'YMEOU' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

def compile_word(word):
    tokens = list()
    i = 1
    for c in word[::-1]:
        if c.isupper():
            tokens.append("{0}*{1}".format(i,c))  # tokens.append(f"{i}*{c}")
            i *= 10
        else:
            tokens.append(c)
        result = '+'.join(tokens)
    print(result)
    return result

def compile_word1(word):
    tokens  = list()
    i = 1
    for c in word[::-1]:
        if c.isupper():
            tokens.append("{0}*{1}".format(i,c))  # tokens.append(f"{i}*{c}")
            i *= 10
        else:
            tokens.append(c)
        result = '+'.join(tokens)
    print(result)
    return result

if __name__ == '__main__':
    assert(compile_word('+') == '+')
    assert(compile_word('YOU') == '1*U+10*O+100*Y')
    print(compile_word('lower'))
    #assert(compile_word('lower') == 'lower')

## pip installs needed:
### random, colored, nltk (names and words corpus)
import random
from colored import fg, attr
import nltk
#nltk.download() # opens gui to download names/words corpus (more can be found, though =])
from nltk.corpus import words

def create_name_bank():
    word_bank = []
    for i in nltk.corpus.names.words():
        word_bank.append(i.upper())
    return(word_bank)
    
def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)
    return(a, b)

def create_word_bank(word_length=5):
    name_bank = create_name_bank()
    word_bank = []
    for i in words.words():
        if len(i) == word_length:
            word_bank.append(i.upper())
    name_bank, word_bank = remove_common(name_bank, word_bank)
    return(word_bank)

class color:
   GREEN = fg('green') + attr('bold')
   YELLOW = fg('yellow') + attr('bold')
   RED = fg('red') + attr('bold')
   BOLD = attr('bold')
   END = attr('reset')

def return_qwerty(right, wrong, guessed, line1, line2, line3):
    print(color.BOLD+"\n Available keyboard remaining:"+color.END)
    line1_comp = ' '
    line2_comp = '  '
    line3_comp = '   '
    for i in line1:
        if i in right:
            line1_comp = line1_comp + ' ' + color.GREEN + i + color.END
        elif i in wrong:
            line1_comp = line1_comp + ' ' + color.YELLOW + i + color.END
        elif i in guessed:
            line1_comp = line1_comp + ' ' + color.BOLD + '-' + color.END
        else:
            line1_comp = line1_comp + ' ' + color.BOLD + i + color.END
    for i in line2:
        if i in right:
            line2_comp = line2_comp + ' ' + color.GREEN + i + color.END
        elif i in wrong:
            line2_comp = line2_comp + ' ' + color.YELLOW + i + color.END
        elif i in guessed:
            line2_comp = line2_comp + ' ' + color.BOLD + '-' + color.END
        else:
            line2_comp = line2_comp + ' ' + color.BOLD + i + color.END
    for i in line3:
        if i in right:
            line3_comp = line3_comp + ' ' + color.GREEN + i + color.END
        elif i in wrong:
            line3_comp = line3_comp + ' ' + color.YELLOW + i + color.END
        elif i in guessed:
            line3_comp = line3_comp + ' ' + color.BOLD + '-' + color.END
        else:
            line3_comp = line3_comp + ' ' + color.BOLD + i + color.END
    print(line1_comp)
    print(line2_comp)
    print(line3_comp+'\n')
        
def check_letter(word, guess, letter, line1, line2, line3, right, wrong, guessed, checked):
    repeat_guess = guess.count(guess[letter])
    repeat_word = word.count(guess[letter])
    repeat_checked = len([x for x in checked if x == guess[letter]])
    if repeat_guess <= repeat_word:
        checked.append(guess[letter])
        if word[letter] == guess[letter]:
            right.append(guess[letter])
            wrong = [x for x in wrong if x != guess[letter]]
            guessed = [x for x in guessed if x != guess[letter]]
            return(color.GREEN+guess[letter]+color.END, line1, line2, line3, right, wrong, guessed, checked)
        elif guess[letter] in word:
            if guess[letter] not in right:
                wrong.append(guess[letter])
            guessed = [x for x in guessed if x != guess[letter]]
            return(color.YELLOW+guess[letter]+color.END, line1, line2, line3, right, wrong, guessed, checked)
        else:
            guessed.append(guess[letter])
            return('_', line1, line2, line3, right, wrong, guessed, checked)
    elif repeat_guess > repeat_word and repeat_guess!=repeat_checked+1:
        checked.append(guess[letter])
        if word[letter] == guess[letter]:
            checked.append(guess[letter])
            right.append(guess[letter])
            wrong = [x for x in wrong if x != guess[letter]]
            guessed = [x for x in guessed if x != guess[letter]]
            return(color.GREEN+guess[letter]+color.END, line1, line2, line3, right, wrong, guessed, checked)
        elif guess[letter] in word:
            if guess[letter] not in right:
                wrong.append(guess[letter])
            guessed = [x for x in guessed if x != guess[letter]]
            return('_', line1, line2, line3, right, wrong, guessed, checked)
        else:
            guessed = [x for x in guessed if x != guess[letter]]
            return('_', line1, line2, line3, right, wrong, guessed, checked)
    else:
        checked.append(guess[letter])
        if word[letter] == guess[letter]:
            right.append(guess[letter])
            wrong = [x for x in wrong if x != guess[letter]]
            guessed = [x for x in guessed if x != guess[letter]]
            return(color.GREEN+guess[letter]+color.END, line1, line2, line3, right, wrong, guessed, checked)
        elif guess[letter] in word:
            if guess[letter] not in right:
                wrong.append(guess[letter])
            guessed = [x for x in guessed if x != guess[letter]]
            return(color.YELLOW+guess[letter]+color.END, line1, line2, line3, right, wrong, guessed, checked)
        else:
            guessed.append(guess[letter])
            return('_', line1, line2, line3, right, wrong, guessed, checked)

for i in range(0, 1):
    
    word_length = 0
    while word_length <4 or word_length>8:
        word_length = int(input(' Select word length between 4 and 8:  '))
        if word_length < 4:
            print(' Words are too small. Choose again!')
        elif word_length > 8:
            print(' Words are too large. Choose again!')
    word_bank = create_word_bank(word_length)

    print("\n {}{}-letter word chosen, enter {}CANCEL{}{} to end{}\n".format(color.BOLD, word_length, color.RED, color.END, color.BOLD, color.END))
    print(" _: letter not in word")
    print(" {}Yellow{}: letter in the wrong spot".format(color.YELLOW, color.END))
    print(" {}Green{}: letter in correct spot\n".format(color.GREEN, color.END))
    rand_word = 'CANCEL'
    while rand_word == 'CANCEL':
        rand_word = word_bank[random.randint(0, len(word_bank))]
    l1='_'
    l2='_'
    l3='_'
    l4='_'
    l5='_'
    l6='_'
    l7='_'
    l8='_'
    line1 = ['Q','W','E','R','T','Y','U','I','O','P']
    line2 = ['A','S','D','F','G','H','J','K','L']
    line3 = ['Z','X','C','V','B','N','M']
    right=[]
    wrong=[]
    guessed=[]
    for i in range(0, 6):
        
        guess = ''
        while len(guess) != word_length and guess != 'CANCEL' and guess not in word_bank:
            guess = input(" Enter Guess {} of 6:  ".format(i+1)).upper()
            if guess != 'CANCEL' and len(guess)!= word_length:
                print('\n{} Sorry, {}{}{}{} is not the right length{}\n'.format(color.BOLD, color.RED, guess, color.END, color.BOLD, color.END))
                guess = ''
            elif guess != 'CANCEL' and guess not in word_bank:
                print('\n{} Sorry, {}{}{}{} is not in the word bank{}\n'.format(color.BOLD, color.RED, guess, color.END, color.BOLD, color.END))
                guess = ''
        if guess == 'CANCEL':
            print(color.BOLD+color.RED+"\n\n You're giving up?... The word was:\n"+color.END+color.BOLD+rand_word+color.END)
            break
        if guess == rand_word:
            print(color.BOLD+color.GREEN+"\n\n  YOU DID IT!!"+color.END)
            break
        else:
            checked = []
            if word_length == 8:
                l8, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 7, line1, line2, line3, right, wrong, guessed, checked)
            if word_length >= 7:
                l7, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 6, line1, line2, line3, right, wrong, guessed, checked)
            if word_length >= 6:
                l6, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 5, line1, line2, line3, right, wrong, guessed, checked)
            if word_length >= 5:
                l5, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 4, line1, line2, line3, right, wrong, guessed, checked)
            l4, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 3, line1, line2, line3, right, wrong, guessed, checked)
            l3, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 2, line1, line2, line3, right, wrong, guessed, checked)
            l2, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 1, line1, line2, line3, right, wrong, guessed, checked)
            l1, line1, line2, line3, right, wrong, guessed, checked=check_letter(rand_word, guess, 0, line1, line2, line3, right, wrong, guessed, checked)
            
            if word_length == 8:
                print('\n  '+l1+' '+l2+' '+l3+' '+l4+' '+l5+' '+l6+' '+l7+' '+l8)
            elif word_length == 7:
                print('\n  '+l1+' '+l2+' '+l3+' '+l4+' '+l5+' '+l6+' '+l7)
            elif word_length == 6:
                print('\n  '+l1+' '+l2+' '+l3+' '+l4+' '+l5+' '+l6)
            elif word_length == 5:
                print('\n  '+l1+' '+l2+' '+l3+' '+l4+' '+l5)
            if word_length == 4:
                print('\n  '+l1+' '+l2+' '+l3+' '+l4)
            
            return_qwerty(right, wrong, guessed, line1, line2, line3)
        if i == 5:
            print(color.BOLD+color.RED+"\n\n You ran out of chances... The word was:\n"+color.END+color.BOLD+rand_word+color.END)
    if guess == 'CANCEL':
        break

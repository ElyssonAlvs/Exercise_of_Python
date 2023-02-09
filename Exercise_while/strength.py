print('*********************************')
print('***Welcome to Hangman!***')
print('*********************************')
secret_word = 'banana'
right_letters = ['_', '_', '_', '_', '_', '_']
hanged = False
hit = False
erros = 0
print(right_letters)
while(not hanged and not hit):
    kick = input("What letter? ")
    if(kick in secret_word):
        position = 0
        for letter in secret_word:
            if(kick.upper() == letter.upper()):
                right_letters[position] = letter
            position = position + 1
        else:
            erros += 1
        hanged = erros == 6
        hit = '_' not in right_letters
        print(right_letters)
if(hit):
    print('You win!!')
else:
    print('You defeat!!')
print('End Game!')
# """

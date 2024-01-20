fh=open('output7.txt','w')
number = input('Enter text: ')
reverse = number [::-1]
if(reverse == number):
    print('Palindrome')
    fh.write(f'{number} is a palindrome ')
else:
    print('not a palindrome')
    fh.write(f'{number} is not a palindrome')

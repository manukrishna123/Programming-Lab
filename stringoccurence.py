str=input("Enter a string : ")
char=str[0]
str=str.replace(char,'$')
print(char+str[1:])
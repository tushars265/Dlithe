string = input()  #lower case

n = len(string)

words = []
vowels = []
vov = ['a','e','i','o','u']
sub = ""
vo = ""
for i in range(n):
    if string[i] in vov:
        if sub != "":
           words.append(sub)
        vo = vo + string[i]     # if vovels occurs together
        sub = ""
    elif i == n-1 and string[i] not in vov:
        sub += string[i]
        words.append(sub)
    else:
        sub += string[i]
        if vo != "":
            vowels.append(vo)
        vo = ""
vo = ""
for i in range(n-1,-1,-1):
    if string[i] in vov:
        vo += string[i]
    else:
        vowels.append(vo)
        break

words.reverse()

reversed = ""
if string[0].lower() in "aeiou":
    for index in range(len(vowels)):
        if index < len(vowels):
            reversed += vowels[index]
        if index < len(words):
            reversed += words[index]
else:
    for index in range(len(words)):
        if index < len(words):
            reversed += words[index]
        if index < len(vowels):
            reversed += vowels[index]
print (reversed)


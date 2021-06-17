#removing nth occurance
sentence= list(input().split())
word,n=input().split()
cnt=0
for i in range(len(sentence)):
   if sentence[i]==word:
      cnt = cnt + 1
   if cnt==int(n):
         del sentence[i]
         break
print(sentence)
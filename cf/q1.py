s = input()
s = s.lower()
ans = ""
 
for x in s:
    if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" and x != "y":
        ans += "." + x
        
print(ans)
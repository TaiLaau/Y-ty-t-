s = input ( str ( "Input Jyutping: "))
a=['']
c=0
for i in range (len(s)):
  if s[i] == " ":
    c+=1
    a.append(' ')
  elif s[i] == "j":
    a[c] += "y"
  else:
    a[c] += s[i]
s=''
b=''
vowel = ["a", "e", "i", "o", "u"]
tone = ["1", "2", "3", "4", "5", "6"]
for i in range (len(a)):
  b=a[i]
  if b[-1] == "1":
    for i in range (len(b)):
      if b[i] in tone:
        c+=1
      elif b[i] not in vowel:
        s+=b[i]
      elif b[i-1] in vowel:
        s+=b[i]
      elif b[i]=="a":
        s+="ā"
      elif b[i]=="e":
        s+="ē"
      elif b[i]=="i":
        s+="ī"
      elif b[i]=="o":
        s+="ō"
      elif b[i]=="u":
        s+="ū"

  if b[-1] == "2":
    for i in range (len(b)):
      if b[i] in tone:
        c+=1
      elif b[i] not in vowel:
        s+=b[i]
      elif b[i-1] in vowel:
        s+=b[i]
      elif b[i]=="a":
        s+="á"
      elif b[i]=="e":
        s+="é"
      elif b[i]=="i":
        s+="í"
      elif b[i]=="o":
        s+="ó"
      elif b[i]=="u":
        s+="ú"

  if b[-1] == "3":
    for i in range (len(b)):
      if b[i] not in tone:
        s+=b[i]

  if b[-1] == "4":
    for i in range (len(b)):
      if b[i] in tone:
        c+=1
      elif b[i] not in vowel:
        s+=b[i]
      elif b[i-1] in vowel:
        s+=b[i]
      elif b[i]=="a":
        s+="à"
      elif b[i]=="e":
        s+="è"
      elif b[i]=="i":
        s+="ì"
      elif b[i]=="o":
        s+="ò"
      elif b[i]=="u":
        s+="ù"
        
  if b[-1] == "5":
    for i in range (len(b)):
      if b[i] in tone:
        c+=1
      elif b[i] not in vowel:
        s+=b[i]
      elif b[i-1] in vowel:
        s+=b[i]
      elif b[i]=="a":
        s+="ã"
      elif b[i]=="e":
        s+="ẽ"
      elif b[i]=="i":
        s+="ĩ"
      elif b[i]=="o":
        s+="õ"
      elif b[i]=="u":
        s+="ũ"
        
  if b[-1] == "6":
    for i in range (len(b)):
      if b[i] in tone:
        c+=1
      elif b[i] not in vowel:
        s+=b[i]
      elif b[i-1] in vowel:
        s+=b[i]
      elif b[i]=="a":
        s+="ạ"
      elif b[i]=="e":
        s+="ẹ"
      elif b[i]=="i":
        s+="ị"
      elif b[i]=="o":
        s+="ọ"
      elif b[i]=="u":
        s+="ụ"



        
print (s)
    

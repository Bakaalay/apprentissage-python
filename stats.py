notes = [12, 8, 15, 9.5, 17, 10, 6, 14]
total=0
nb=0

for i in range(len(notes)):
    total=total+notes[i]
    if notes[i]>=10:
        nb=nb+1
moyenne=total/len(notes)

print("moyenne=",moyenne)

print("max=",max(notes))

print("min=",min(notes))

print("nb notes > 10 =",nb)
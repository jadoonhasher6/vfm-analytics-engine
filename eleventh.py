with open('names.txt','w') as file:
    file.write('hashir\nzainab\nesa\nsherkhan\njadoon')
print('reading the names from the file')
with open('names.txt','r') as file:
    for line in file:
        print(line.strip())


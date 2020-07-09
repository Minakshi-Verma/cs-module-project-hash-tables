# Your code here
with open("robin.txt") as f:
    words = f.read() # put words into an array
    word_split = words.split() # split array into words

cache = {}

for word in word_split: # check word and see if it is in cache.

    #ignored charcters " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    new_string= word.replace('"','').replace(':','').replace(';','').replace(',','').replace('.','').replace('-','').replace('+','').replace('=','').replace('/','').replace("|",'').replace('[','').replace(']','').replace('{','').replace('}','').replace('(','').replace(')','').replace('*','').replace('^','').replace('&','').replace('?','').replace('!','').replace('\\','')

    # print(new_string)

    if new_string not in cache:
        cache[new_string] = '#'
    else:
        cache[new_string] += '#'   

items = list(cache.items())
print(items)

items.sort(key=lambda x: x[1], reverse=True) # sort frequency descending (higher to lower)


for key, value in items:   
    print(f'{key:<20} {value}')  # key and values are 20 spaces apart
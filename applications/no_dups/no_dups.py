def no_dups(s):
    # Your code here
    #split the text string to a list of string
    s_word = s.split()
    # print(type(s_word))
    # print(s_word)
    
    cache = {}
    output = ""
    for i in range(len(s_word)):    
        if s_word[i] not in cache:
            #Add to cache if not there           
            cache[s_word[i]] = True
            print(cache)
            output += s_word[i] + " "
            # print(output)                     
    
    # remove the extra last space at the end of the last string 
         
    return output[:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
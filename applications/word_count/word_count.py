def word_count(s):
    # Your code here
    # takes single string--split the strings at whitespace
    # returns frequency of strings
    # output keys must be lowercase

    s_word = s.split()

    s_lower= s.word()   
    word_cache ={}

    
    for i in range (len(s_lower)):
        if s_lower[i] not in  word_cache:
            word_cache[i] = True
        # if not char.isspace():
        # if char != " ":
        if character >= 'a' and character <= 'z':
            if character not in word_cache:
                word_cache[character] = 1
            else:
                word_cache[character] += 1

    # print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
    # sorted gives back a new function

    # sort works in place
    tally_list = list(word_cache.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)

    # alternate way to reverse sort
    # tally_list.sort(key = lambda x: (-(x[1]))

    for pair in tally_list:
        print(f'Count: {pair[1]}, letter: {pair[0]}')


    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
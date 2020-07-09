
def word_count(s):
    # Your code here
    # replace bad/ ignored charcters
    # if input contains no ignored characters, return an empty dictionary
    # takes single string--split the strings at whitespace
    # returns frequency/count of strings
    # output keys must be lowercase  

    #  " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    # '":;,.-+=/\\|[]{}()*^&'
    # Hello, my cat. And my cat doesn't say "hello" back.

    # replace the bad charctere from the list above

    new_string= s.replace('"','').replace(':','').replace(';','').replace(',','').replace('.','').replace('-','').replace('+','').replace('=','').replace('/','').replace('','').replace("|",'').replace('[','').replace(']','').replace('{','').replace('}','').replace('(','').replace(')','').replace('*','').replace('^','').replace('&','').replace('\\','')

    # print(new_string)

    #input contains no ignored characters, return an empty dictionary
    if new_string == '':
        return {}

    #split the strings at whitespace and lower the case
    split_lower = new_string.lower().split()
    print(split_lower)
    
    # get the count
    words = {i:split_lower.count(i) for i in split_lower}
    return words





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
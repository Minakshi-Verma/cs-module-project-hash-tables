# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
    words = f.read() # put words into an array
    word_split = words.split() # split array into words
    print(word_split)

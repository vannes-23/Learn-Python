# Bring in the urllib library to connect to the internet
import urllib.request, urllib.parse, urllib.error

address = input('Please enter the address: ')
# Change the address to a file handle
fahand = urllib.request.urlopen(address)

# Initialize a dictionary to count word occurrences
word_count = {}
for line in fahand:
    # Decode means to convert from bytes to string
    words = line.decode().split()
    # This code is to find the number of times each word appears in the text
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

bigword = None
bigcount = None
# This code is to find the word that appears the most in the text
for word, count in word_count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

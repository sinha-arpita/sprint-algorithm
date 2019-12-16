'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    i=word.find("th")
    if i==-1:   #first occurrence of th in the word is found
        return 0
    # We have found first occurance of "th" starting at index i. So we have 1
    # So now call this function again with rest of word starting from i + 2 (length of "th")
    # TBC
    
    return 1+ count_th(word[i+2:])
print(count_th("abcdethefthghitheth"))




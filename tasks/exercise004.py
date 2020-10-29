# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    new_text = ''
    new_word = ''
    final_characteres = ''
    for word in text.split(" "):
        c = 0
        n = len(word) - 1
        while n > 0:
            if word[n].isalpha():
                new_word = word[1:n+1] + word[0] + 'ay'
                n = 0
            else:
                final_characteres = final_characteres + word[n]
            n -= 1
        new_word = new_word + final_characteres
        if new_text == '':
            new_text = new_word
        else:
            new_text = new_text + ' ' + new_word
    return new_text

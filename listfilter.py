text = input('Type your text here: ').lower()
#making list of text input
text_data = text.split()
#return words to be replaced
words = filter(lambda word: not word.isalpha(), text_data)
new_text = list(words)
#replace to normal words
for i in range(len(new_text)):
    word = new_text[i]
    for letter in word:
        if not letter.isalpha():
            new_text[i] = new_text[i].replace(letter, '')
#normal words list
correct_words = filter(lambda word: word.isalpha(), text_data)
correct_words_list = list(correct_words)
#recreating final list and counting words
final_list = new_text + correct_words_list
max_counted_word = None
max_counted = 0

for i, word in enumerate(final_list):
    if word is None:
        continue

    count = final_list.count(word)

    if count > max_counted:
        max_counted = count
        max_counted_word = word

    # Mark all occurrences of the word as None to avoid counting them again
    for j in range(i, len(final_list)):
        if final_list[j] == word:
            final_list[j] = None


print(max_counted_word)
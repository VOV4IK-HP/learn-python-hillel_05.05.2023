input_message = input("введи строку : ")
print(input_message[::-1])

input_name = input("Введи имя: ")
answer = f"Hello, {input_name}"
print(answer)

word = input("Write your word: ")
word = word.lower()
print(word)
word2 = word[::-1]
if word == word2:
    print("Yes")
else:
    print("No")
str = input('Please, input your string\n-> ')
str = str.lower()
str = str.replace(",", "")
str = str.replace(".", "")
str = str.replace("-", "")
str = str.replace(":", "")
str = str.replace(";", "")
str = str.replace("?", "")
str = str.replace("!", "")
str = str.replace(":", "")
str = str.replace(")", "")
str_what = input('What do you want to replace?\n-> ')
word = str.find(str_what)
print(str_what, 'was found at position', word)
str_with = input('With what do you want to replace?\n-> ')
str = str.replace(str_what, str_with)
print('Here is your result:\n->', str)
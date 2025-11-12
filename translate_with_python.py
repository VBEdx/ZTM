from translate import Translator
try:
    with open("test.txt", mode='r') as f:
        my_text = f.read()
except IOError as err:
    print(err)
except FileNotFoundError as err:
    print(err)

my_translator = Translator(to_lang='es')
my_text_ja = my_translator.translate(my_text)

with open("test_jap.txt", mode='w') as f2:
    f2.write(my_text_ja)


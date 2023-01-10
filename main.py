import copy
import random
import time


def list_to_str(words):
    sentence = ''
    for word in words:
        sentence = sentence + word + ' / '
    sentence += "\n"
    sentence = sentence.replace('+', ' ')
    return sentence


def get_file_paths():
    input_file = "sentences.txt"
    output_file = "shuffled.txt"
    return input_file, output_file


def get_text(input_file, output_file):
    return open(input_file, 'r', encoding="utf8"), open(output_file, 'w', encoding="utf8")


def make_word_list(text):
    split_sentence = text.split()
    return split_sentence


def make_shuffled_str(split_sentence):
    temp = copy.deepcopy(split_sentence)
    while temp == split_sentence:
        random.shuffle(temp)
        print(temp)
        print(split_sentence)
    shuffled_sentence_str = list_to_str(temp)
    return shuffled_sentence_str


def iterate_file(text, new_text):
    for newLine in text:
        split_sentence = make_word_list(newLine)
        new_text.write(make_shuffled_str(split_sentence))


def close_documents(text, new_text):
    new_text.close()
    text.close()


def main():
    filepath, filepath_new = get_file_paths()
    text, new_text = get_text(filepath, filepath_new)
    iterate_file(text, new_text)
    close_documents(text, new_text)


if __name__ == '__main__':
    main()

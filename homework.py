# 3. 读取一个文本，
#             × 分别匹配文本中所有的以大写字母开头的单词，包含特殊字符不算
#             × 数字， 包括整数，小数，负数，分数，百分数
import re


def read_file(filename):
    with open(filename, 'rt', encoding='utf-8') as rf:
        return rf.read()


def get_words(content):
    '''获取大写字母开头的单词，返回列表'''
    pattern = r'[A-Z][a-z]+\b'
    words = re.findall(pattern, content)
    return words


def get_numbers(content):
    '''获取内容中的数字'''
    pattern = r'[-]*\d*/*\.*\d+%*'
    numbers = re.findall(pattern, content)
    return numbers


def main():
    content = read_file('book.txt')
    words = get_words(content)
    numbers = get_numbers(content)
    print(words)
    print(numbers)


if __name__ == '__main__':
    main()



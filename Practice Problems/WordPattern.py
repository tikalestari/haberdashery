'''Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
'''


def is_pattern(pattern, string):
    p_list = list(pattern)
    s_list = string.split()
    dic = {}
    i = 0

    if len(p_list) != len(s_list):
        return False

    for p in p_list:
        if p not in dic:
            if s_list[i] in dic.values():
                return False
            else:
                dic[p] = s_list[i]
        elif dic[p] != s_list[i]:
            return False
        i += 1

    return True








print(is_pattern("abba","dog cat cat dog"))
print(is_pattern("abba","dog cat cat fish"))
print(is_pattern("aaaa","dog cat cat dog"))
print(is_pattern("abba","dog dog dog dog"))

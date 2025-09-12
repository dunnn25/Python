def check_len_string(s):
    return len(s) >= 5
words = ["python", "java", "ruby", "c++", "javascript", "html"]
long_str = filter(check_len_string,words)
print(list(long_str))
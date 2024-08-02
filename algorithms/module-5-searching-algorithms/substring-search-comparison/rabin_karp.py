def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

    base = 256
    prime = 101
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i

        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % prime
            if text_hash < 0:
                text_hash += prime

    return -1

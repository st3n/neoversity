from collections import deque


def is_palindrome(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True

    s = s.casefold()
    punctuation_chars = "',.?! "
    s = "".join(c for c in s if c not in punctuation_chars)

    deq = deque(s)

    while deq:
        try:
            if deq.pop() != deq.popleft():
                return False
        except IndexError:
            return True
    return True


def test_true_polindorms():
    # Паліндроми
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert (
        is_palindrome("Madam In Eden, I'm Adam") is True
    ), "Провалено: 'Madam In Eden, I'm Adam'"
    assert is_palindrome("A Santa at NASA") is True, "Провалено: 'A Santa at NASA'"


def test_not_polindroms():
    # Не паліндроми
    assert is_palindrome("Python") is False, "Провалено: 'Python'"
    assert is_palindrome("OpenAI") is False, "Провалено: 'OpenAI'"


def test_true_polindroms_with_punctuation():
    # Зі знаками пунктуації та пробілами
    assert (
        is_palindrome("Was it a car or a cat I saw?") is True
    ), "Провалено: 'Was it a car or a cat I saw?'"
    assert is_palindrome("No 'x' in Nixon") is True, "Провалено: 'No 'x' in Nixon'"


def test_short_polidroms():
    # Короткі рядки та пустий рядок
    assert is_palindrome("a") is True, "Провалено: 'a'"
    assert is_palindrome("ab") is False, "Провалено: 'ab'"
    assert is_palindrome("") is True, "Провалено: пустий рядок"


def test_mixed_upper_lower():
    # Змішаний регістр
    assert (
        is_palindrome("Eva, Can I Stab Bats In A Cave?") is True
    ), "Провалено: 'Eva, Can I Stab Bats In A Cave?'"
    assert (
        is_palindrome("Mr. Owl Ate My Metal Worm") is True
    ), "Провалено: 'Mr. Owl Ate My Metal Worm'"


def main():
    test_true_polindorms()
    test_not_polindroms()
    test_true_polindroms_with_punctuation()
    test_short_polidroms()
    test_mixed_upper_lower()


if __name__ == "__main__":
    main()

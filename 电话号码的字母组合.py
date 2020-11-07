def letterCombinations(digits):
    if not digits:
        return []

    phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    queue = ['']
    for digit in digits:
        for _ in range(len(queue)):
            tmp = queue.pop(0)
            for letter in phone[ord(digit)-50]:
                queue.append(tmp+letter)
    return queue

print(letterCombinations("23"))
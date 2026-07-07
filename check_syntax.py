import sys

def check_brackets(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    stack = []
    lines = content.split('\n')
    pairs = {'}': '{', ')': '(', ']': '['}
    openers = {'{', '(', '['}
    
    for i, line in enumerate(lines):
        for char in line:
            if char in openers:
                stack.append((char, i + 1))
            elif char in pairs:
                if not stack:
                    print(f"Extra closing {char} at line {i+1}")
                    return
                top, top_line = stack.pop()
                if top != pairs[char]:
                    print(f"Mismatched {char} at line {i+1}. Expected closing for {top} from line {top_line}")
                    return
    
    if stack:
        for char, line in stack:
            print(f"Unclosed {char} starting at line {line}")
    else:
        print("Brackets are balanced.")

if __name__ == "__main__":
    check_brackets('app.js')

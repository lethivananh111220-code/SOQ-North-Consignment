with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "'oda_input': latestOdaInput > 0 ? Number(latestOdaInput.toFixed(2)) : '',"
replacement = "'oda_input': latestOdaDate > 0 ? Number(latestOdaInput.toFixed(2)) : '',"
if target in text:
    text = text.replace(target, replacement)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed oda_input successfully')
else:
    print('Target not found')

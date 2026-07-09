import codecs
import re

with codecs.open('app.js', 'r', 'utf-8') as f:
    text = f.read()

text = text.replace('AIzaSyBHG5WoQVon5lgoyZNZ7agIVYJDjyZdRrY', 'AIzaSyAXLLILSZAmquyIJCXOS3z8ZiPIBvZoQio')
text = text.replace('soq-south-consignment', 'soq-north-consignment')
text = re.sub(r'measurementId:\s*"[^"]+"', 'measurementId: "G-MSG7VKL5QQ"', text, count=1)

with codecs.open('app.js', 'w', 'utf-8') as f:
    f.write(text)

print('Firebase config fixed!')

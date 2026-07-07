import os

path = r'd:\DHF\QLKV_WM\web_app\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

print("Has update.py changes:", 'let isWknd = false;' in content)

import os

for path in [r'd:\DHF\QLKV_WM\web_app\app.js', r'd:\DHF\SOQ - HÀ NỘI\website\app.js']:
    print(f"Checking {path}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        print("Length:", len(content))
        has_khuvuc = 'khu v\u1ef1c' in content.lower()
        has_khuvc = 'khuv?c' in content.lower()
        print("Has khu vuc:", has_khuvuc)
        print("Has khuv?c:", has_khuvc)
    except Exception as e:
        print("Error reading utf-8:", e)

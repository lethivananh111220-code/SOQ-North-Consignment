import codecs

with codecs.open('D:/DHF/QLKV_WM/web_app/index.html', 'r', 'utf-8') as f:
    text = f.read()

# Replace Tồn (Inv) and Nhập (Input) with (Hệ thống) just in case
text = text.replace('Tồn (Inv)', 'Tồn (Hệ thống)')
text = text.replace('Nhập (Input)', 'Nhập (Hệ thống)')

# Insert Nhập (ODA) into the headers where appropriate
old_header = "<th>Nhập (Hệ thống)</th>"
new_header = "<th>Nhập (Hệ thống)</th>\n                                <th>Nhập (ODA)</th>"
text = text.replace(old_header, new_header)

old_th2 = '<th class="sortable" data-sort="input" title="Tổng lượng hàng nhập trong chu kỳ Leadtime">Nhập (Hệ thống) <span class="sort-icon"></span></th>'
new_th2 = '<th class="sortable" data-sort="input" title="Tổng lượng hàng nhập trong chu kỳ Leadtime">Nhập (Hệ thống) <span class="sort-icon"></span></th>\n                                <th class="sortable" data-sort="oda_input" title="Nhập thực tế">Nhập (ODA) <span class="sort-icon"></span></th>'
text = text.replace(old_th2, new_th2)

# Save
with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)

print("index.html restored properly!")

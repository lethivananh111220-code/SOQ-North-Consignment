import codecs
import re

with codecs.open('D:/DHF/QLKV_WM/web_app/app.js', 'r', 'utf-8') as f:
    text = f.read()

# 1. Replace Firebase config
south_firebase = '''const firebaseConfig = {
    apiKey: "AIzaSyBHG5WoQVon5lgoyZNZ7agIVYJDjyZdRrY",
    authDomain: "soq-south-consignment.firebaseapp.com",
    databaseURL: "https://soq-south-consignment-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "soq-south-consignment",
    storageBucket: "soq-south-consignment.firebasestorage.app",
    messagingSenderId: "491007756368",
    appId: "1:491007756368:web:8ea77f51a2a0f3b151a955",
    measurementId: "G-MSG7VKL5QQ"
};'''

north_firebase = '''const firebaseConfig = {
    apiKey: "AIzaSyAXLLILSZAmquyIJCXOS3z8ZiPIBvZoQio",
    authDomain: "soq-north-consignment.firebaseapp.com",
    databaseURL: "https://soq-north-consignment-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "soq-north-consignment",
    storageBucket: "soq-north-consignment.firebasestorage.app",
    messagingSenderId: "491007756368",
    appId: "1:491007756368:web:8ea77f51a2a0f3b151a955",
    measurementId: "G-MSG7VKL5QQ"
};'''

text = text.replace(south_firebase, north_firebase)

# 2. Replace rawDate parsing
old_rawdate = "let rawDate = row['orderdate'] || row['Order date'] || 0;"
new_rawdate = "let rawDate = row['orderdate'] || row['Order date'] || row['completeddate'] || row['Completed date'] || row['date'] || row['ngaydathang'] || row['ngay'] || row['ngaytao'] || row['createddate'] || 0;"
text = text.replace(old_rawdate, new_rawdate)

# 3. Add globalLatestOdaDate logic
# a. Declare globalLatestOdaDate
old_declare = '''        const actualODA_Names = new Map(); // Lưu Tên ODA chuẩn nhất từ file vận hành'''
new_declare = '''        const actualODA_Names = new Map(); // Lưu Tên ODA chuẩn nhất từ file vận hành\n        let globalLatestOdaDate = 0;'''
text = text.replace(old_declare, new_declare)

# b. Update globalLatestOdaDate
old_update = '''                let cDeliveryDate = cOrderDate > 0 ? cOrderDate + 86400000 : 0; // Cộng thêm 1 ngày giao\n\n                let T = storeMasterDateMap.get(storeID);'''
new_update = '''                let cDeliveryDate = cOrderDate > 0 ? cOrderDate + 86400000 : 0; // Cộng thêm 1 ngày giao\n                if (cDeliveryDate > globalLatestOdaDate) globalLatestOdaDate = cDeliveryDate;\n\n                let T = storeMasterDateMap.get(storeID);'''
text = text.replace(old_update, new_update)

# c. Update latestOdaDate and latestOdaInput in final calculation
old_final = '''            let finalInput = inputData.currentInput || 0;
            let latestOdaInput = inputData.latestOdaInput || 0;
            let latestOdaDate = inputData.latestOdaDate || 0;'''
new_final = '''            let finalInput = inputData.currentInput || 0;
            let latestOdaDate = (inputData.latestOdaDate === globalLatestOdaDate) ? inputData.latestOdaDate : 0;
            let latestOdaInput = (inputData.latestOdaDate === globalLatestOdaDate) ? (inputData.latestOdaInput || 0) : 0;'''
text = text.replace(old_final, new_final)

# d. Fix oda_input conditional to handle 0
old_push = '''                'oda_input': Number(latestOdaInput.toFixed(2)),
                'oda_date_str': formatDateStr(latestOdaDate),'''
new_push = '''                'oda_input': latestOdaDate > 0 ? Number(latestOdaInput.toFixed(2)) : '',
                'oda_date_str': latestOdaDate > 0 ? formatDateStr(latestOdaDate) : '','''
text = text.replace(old_push, new_push)

# HTML template fix inside app.js
old_html = '''<td class="highlight" title="Nhập (ODA) ghi nhận ngày ${item.oda_date_str}">${item.oda_input}</td>'''
new_html = '''<td class="highlight" title="${item.oda_date_str ? 'Nhập (ODA) ghi nhận ngày ' + item.oda_date_str : ''}">${item.oda_input !== '' ? item.oda_input : '-'}</td>'''
text = text.replace(old_html, new_html)

with codecs.open('app.js', 'w', 'utf-8') as f:
    f.write(text)

print("Restoration complete.")

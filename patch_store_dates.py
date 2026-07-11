import codecs

with codecs.open('app.js', 'r', 'utf-8') as f:
    content = f.read()

# Normalize CRLF
content = content.replace('\r\n', '\n')

old_step_0 = """// --- BƯỚC 0: TÌM NGÀY LỚN NHẤT CỦA TỪNG STORE LÀM MỐC (T) ---
        const storeMaxInvDateMap = new Map();
        const storeMaxOrderDateMap = new Map();

        window.dateFmtDetected = 0;
        if (datasets.inventory && datasets.inventory.length > 0) {
            datasets.inventory.forEach(row => {
                let store = row['sap'] || row['storecode'] || row['nickname'] || row['storename'] || row['store'] || row['mach'] || row['article'];
                if (!store) return;
                let storeID = extractSAP(store);
                if (storeID && isNaN(parseInt(storeID))) {
                    let lookedUp = reverseStoreNamesMap.get(normalizeKey(store));
                    if (lookedUp) storeID = lookedUp;
                }
                let rawDate = row['date'] || row['Date'] || row['ngay'] || row['ngày'] || 0;
                let cDate = parseDateStrToTime(rawDate);
                if (cDate > 0) {
                    let currentMax = storeMaxInvDateMap.get(storeID) || 0;
                    if (cDate > currentMax) storeMaxInvDateMap.set(storeID, cDate);
                }
            });
        }"""

new_step_0 = """// --- BƯỚC 0: TÌM NGÀY LỚN NHẤT CỦA TỪNG STORE LÀM MỐC (T) ---
        const storeMaxInvDateMap = new Map();
        const storeMaxInputDateMap = new Map();
        const storeMaxOrderDateMap = new Map();

        window.dateFmtDetected = 0;
        if (datasets.inventory && datasets.inventory.length > 0) {
            datasets.inventory.forEach(row => {
                let store = row['sap'] || row['storecode'] || row['nickname'] || row['storename'] || row['store'] || row['mach'] || row['article'];
                if (!store) return;
                let storeID = extractSAP(store);
                if (storeID && isNaN(parseInt(storeID))) {
                    let lookedUp = reverseStoreNamesMap.get(normalizeKey(store));
                    if (lookedUp) storeID = lookedUp;
                }
                let rawDate = row['date'] || row['Date'] || row['ngay'] || row['ngày'] || 0;
                let cDate = parseDateStrToTime(rawDate);
                if (cDate > 0) {
                    let invStr = String(row['tonkho'] || row['stock'] || row['ton'] || row['inventory'] || row['inventoryquantity'] || row['inventoryamount'] || row['stkinv'] || '').trim();
                    let inputStr = String(row['import amount'] || row['importamount'] || row['nhap'] || row['nhapinput'] || '').trim();
                    
                    if (invStr !== '') {
                        let currentMax = storeMaxInvDateMap.get(storeID) || 0;
                        if (cDate > currentMax) storeMaxInvDateMap.set(storeID, cDate);
                    }
                    if (inputStr !== '') {
                        let currentMax = storeMaxInputDateMap.get(storeID) || 0;
                        if (cDate > currentMax) storeMaxInputDateMap.set(storeID, cDate);
                    }
                }
            });
        }"""

old_store_master = """        const storeMasterDateMap = new Map();
        for (let storeID of new Set([...storeMaxInvDateMap.keys(), ...storeMaxOrderDateMap.keys()])) {
            let sInvDate = storeMaxInvDateMap.get(storeID) || 0;
            let sOrderDate = storeMaxOrderDateMap.get(storeID) || 0;"""

new_store_master = """        const storeMasterDateMap = new Map();
        for (let storeID of new Set([...storeMaxInvDateMap.keys(), ...storeMaxInputDateMap.keys(), ...storeMaxOrderDateMap.keys()])) {
            let sInvDate = Math.max(storeMaxInvDateMap.get(storeID) || 0, storeMaxInputDateMap.get(storeID) || 0);
            let sOrderDate = storeMaxOrderDateMap.get(storeID) || 0;"""

old_inv_loop = """                if (!inventoryMap.has(key)) {
                    inventoryMap.set(key, {
                        latestInvDate: 0, sumInv: 0,
                        latestInputDate: 0, sumInput: 0,
                        latestDispDate: 0, sumDisp: 0,
                        prevInv: 0, prevInvDate: 0,
                        prevInput: 0, prevInputDate: 0,
                        prodOrig: prodStd, storeID: storeID
                    });
                }

                let data = inventoryMap.get(key);
                if (hasInv) {
                    if (cDate > data.latestInvDate) {
                        data.latestInvDate = cDate;
                        data.sumInv = inv;
                    } else if (cDate === data.latestInvDate) {
                        data.sumInv += inv;
                    }
                    if (cDate < T) {
                        if (cDate > data.prevInvDate) {
                            data.prevInvDate = cDate;
                            data.prevInv = inv;
                        } else if (cDate === data.prevInvDate) {
                            data.prevInv += inv;
                        }
                    }
                }

                if (hasInput) {
                    if (cDate > data.latestInputDate) {
                        data.latestInputDate = cDate;
                        data.sumInput = inputAmt;
                    } else if (cDate === data.latestInputDate) {
                        data.sumInput += inputAmt;
                    }
                    if (cDate < T) {
                        if (cDate > data.prevInputDate) {
                            data.prevInputDate = cDate;
                            data.prevInput = inputAmt;
                        } else if (cDate === data.prevInputDate) {
                            data.prevInput += inputAmt;
                        }
                    }
                }"""

new_inv_loop = """                let storeLatestInvDate = storeMaxInvDateMap.get(storeID) || 0;
                let storeLatestInputDate = storeMaxInputDateMap.get(storeID) || 0;

                if (!inventoryMap.has(key)) {
                    inventoryMap.set(key, {
                        latestInvDate: storeLatestInvDate, sumInv: 0,
                        latestInputDate: storeLatestInputDate, sumInput: 0,
                        latestDispDate: 0, sumDisp: 0,
                        prevInv: 0, prevInvDate: 0,
                        prevInput: 0, prevInputDate: 0,
                        prodOrig: prodStd, storeID: storeID
                    });
                }

                let data = inventoryMap.get(key);
                if (hasInv) {
                    if (cDate === storeLatestInvDate) {
                        data.sumInv += inv;
                    }
                    if (cDate < T) {
                        if (cDate > data.prevInvDate) {
                            data.prevInvDate = cDate;
                            data.prevInv = inv;
                        } else if (cDate === data.prevInvDate) {
                            data.prevInv += inv;
                        }
                    }
                }

                if (hasInput) {
                    if (cDate === storeLatestInputDate) {
                        data.sumInput += inputAmt;
                    }
                    if (cDate < T) {
                        if (cDate > data.prevInputDate) {
                            data.prevInputDate = cDate;
                            data.prevInput = inputAmt;
                        } else if (cDate === data.prevInputDate) {
                            data.prevInput += inputAmt;
                        }
                    }
                }"""

success = True

if old_step_0 in content:
    content = content.replace(old_step_0, new_step_0)
    print("Replaced step 0")
else:
    print("Failed step 0")
    success = False

if old_store_master in content:
    content = content.replace(old_store_master, new_store_master)
    print("Replaced store master")
else:
    print("Failed store master")
    success = False

if old_inv_loop in content:
    content = content.replace(old_inv_loop, new_inv_loop)
    print("Replaced inv loop")
else:
    print("Failed inv loop")
    success = False

if success:
    with codecs.open('app.js', 'w', 'utf-8') as f:
        f.write(content)
    print("All patched!")

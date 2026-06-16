const fs = require('fs');

function parseDateStrToTime(val) {
    if (!val && val !== 0) return 0;
    if (typeof val === 'number') {
        let utcDate = new Date(Math.round((val - 25569) * 86400 * 1000));
        return new Date(utcDate.getUTCFullYear(), utcDate.getUTCMonth(), utcDate.getUTCDate()).getTime();
    }
    let s = String(val).trim().split(' ')[0]; 

    let m2 = s.match(/^(\d{4})[\/\-](\d{1,2})[\/\-](\d{1,2})/);
    if (m2) {
        return new Date(parseInt(m2[1], 10), parseInt(m2[2], 10) - 1, parseInt(m2[3], 10)).getTime();
    }

    let m = s.match(/^(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{2,4})/);
    if (m) {
        let p1 = parseInt(m[1], 10);
        let p2 = parseInt(m[2], 10);
        let yr = parseInt(m[3], 10);
        if (yr < 100) yr += 2000;

        let d, mth;
        if (p1 > 12) {
            d = p1; mth = p2; 
        } else if (p2 > 12) {
            mth = p1; d = p2; 
        } else {
            d = p1; mth = p2; 
        }
        return new Date(yr, mth - 1, d).getTime();
    }

    const parsed = new Date(s).getTime();
    if (!isNaN(parsed)) {
        let d = new Date(parsed);
        return new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime();
    }
    return 0;
}

let date1 = "15/06/2026";
console.log("15/06/2026 ->", new Date(parseDateStrToTime(date1)));

let date2 = 46187; // Excel serial
console.log("Excel 46187 ->", new Date(parseDateStrToTime(date2)));

let date3 = "7/11";
console.log("7/11 ->", new Date(parseDateStrToTime(date3)));

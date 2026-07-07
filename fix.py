import codecs
import re

with codecs.open('app.js', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

idx_start = text.find('let totalDemandRaw = totalDemand + penaltyApplied;')
idx_end = text.find('finalResults.push({', idx_start)

if idx_start != -1 and idx_end != -1:
    new_text = text[:idx_start] + '''let totalDemandRaw = totalDemand + penaltyApplied;
            let breakdownTip = `Công thức: Demand (Nhu cầu gốc) + SafetyStock. \\n- Nhu cầu gốc (Coverage): ${basePeriodDemand.toFixed(2)}\\n- SafetyStock: +${safetyStock.toFixed(2)} \\n- Penalty (Giảm trừ): -${penaltyApplied.toFixed(2)}`;

            ''' + text[idx_end:]
    with codecs.open('app.js', 'w', 'utf-8') as f:
        f.write(new_text)
    print('Fixed via python script file!')
else:
    print('Could not find indices!', idx_start, idx_end)

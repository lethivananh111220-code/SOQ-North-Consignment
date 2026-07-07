import codecs

path = r'd:\DHF\SOQ - HÀ NỘI\website\app.js'
with codecs.open(path, 'r', 'utf-8') as f:
    content = f.read()

old_str = "${coverageDemandBase.toFixed(2)}"
new_str = "${basePeriodDemand.toFixed(2)}"

if old_str in content:
    content = content.replace(old_str, new_str)
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found!")

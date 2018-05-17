
i = 1
data = ''

while i < 1001:
    data += '{"model": "api.product","pk": "'+ str(i) +'", "fields": { "name": "name_'+ str(i) +'", "category": "category_'+ str(i) +'", "description": "description_'+ str(i) +'" } },'
    i += 1

data = '[ ' + data + ' ]'

with open('data.json', 'w') as f:
  f.write(data)

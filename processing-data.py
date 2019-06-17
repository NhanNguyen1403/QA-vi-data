import json

with open('qa-vi-data.json', encoding='utf-8') as f:
        data = json.load(f)


for i, item in enumerate(data['data'][0]['paragraphs']):
        with open(str(i)+'.json', 'w', encoding='utf-8') as outfile:
                json.dump(item, outfile,ensure_ascii=False, indent=4)
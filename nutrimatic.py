import requests
import re

q = 'hello'
x = requests.get('https://nutrimatic.org/?q={}'.format(q))
values = re.findall(
    '<span style=\'font-size: \d*\.\d*em\'>(.*)</span><br>', x.text)
print(values)
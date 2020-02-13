'''
import uuid
print(uuid.uuid4().hex)
print(len(uuid.uuid4().hex))

from datetime import date
person = {'name': 'Eric', 'age': 74}
print(f"ansible-log-{date.today()}.txt")


from configparser import ConfigParser
conf = ConfigParser(allow_no_value=True)
conf.read('ansible/hosts')
hosts = [i for k in conf.sections() for i in conf[k]]
print(hosts)

for i in conf.sections():
    print(i)
    for j in conf[i]:
        print(j)
'''

hoss = {'A':1,'B':3,'C':2}
sec = {'K':7,'A':9}
hoss.update(sec)
print(hoss)
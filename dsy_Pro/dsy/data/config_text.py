import configparser
config = configparser.ConfigParser()
config.read('config.conf')

# lists_header = config.sections()
# print(lists_header)

s = config.getint("sgZ", "user")
print(type(s))
print(s)

s = config.get("sgZ", "user")
print(type(s))
print(s)
fd = open('config.conf')
data = fd.read()
print(data[:3])


def set_headers(name, value):
    config.set("EMAIL", name, value)
    with open('config.conf', 'w+') as f:
        config.write(f)
set_headers("hah", "2")

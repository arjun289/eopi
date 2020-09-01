dict = {
    'joe': 18,
    'Adam': 16,
    'emily': 56
}

print(dict['joe'])
dict['joe'] = 19
print(dict['joe'])


print(dict.items())
print(dict.values())

for key, value in dict.items():
    print(key, value, sep=" => ")

# * break, continue, pass
name = ['jone','maria','anik','','ram']
# break : stops the loop
for name in name:
    if name == '':
        print("No name detected")
        break
    print(f'name is {name}')

# continue : skips the current iteration and jumps to the next
for name in name:
    if name == '':
        continue
    print(f'name is {name}')

# pass : placeholder, nothing happens, it continues normally
for name in name:
    if name == '':
        pass
    print(f'name is {name}')
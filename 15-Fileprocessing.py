f = open("essay.txt", "r")
contents = f.read()
print(contents.title())
print(len(contents))
f.close()

new_member = input("Add a new member")

f = open("members.txt","r")
existing_members = f.readlines()
f.close()

existing_members.append(new_member+"\n")
print(existing_members)

f = open("members.txt","w")
f.writelines(existing_members)
f.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()






f=open("f.txt","r")
print(f.readline())
'''
ls=['中国','美感']
f.writelines(ls)
f.seek(0)
for line in f:
    print(line)
#f.writelines(['中国','法国'])
'''
f.close()

#open text file
with open('Secret.txt','r') as hid:
    #Read text file line by line
    read_line = hid.read()
    #convert text file to octal values
    for c in read_line:
        octa =' '.join(format(ord(c),'o') for c in read_line)
        
#write octal values in text file 
with open('Mask.txt','w+') as encrypt:
    encrypt.write(octa)

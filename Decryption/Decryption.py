#open text file
with open('Mask.txt','r') as show:
     #Read text file line by line
     read_line = show.read()
     octal = read_line.split()
     ascii_str = ""
     #convert to base 8 integer
     for value in octal:
         integer = int(value, 8)
         #convert to ascii
         ascii_character = chr(integer)
         #append characters
         ascii_str += ascii_character

#write converted text into text file 
with open('Unmask.txt','w+') as decrypt:
    decrypt.write(ascii_str)

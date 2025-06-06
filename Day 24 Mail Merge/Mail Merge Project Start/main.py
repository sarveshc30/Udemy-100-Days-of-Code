#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
name_file = open(r'F:\Udemy 100 Days of Code\Day 24 Mail Merge\Mail Merge Project Start\Input\Names\invited_names.txt', 'r')
name_list = name_file.readlines()
name_list2 = []
for i in name_list:
    name_list2.append(i.strip('\n'))

for i in name_list2:
    with open(r'F:\Udemy 100 Days of Code\Day 24 Mail Merge\Mail Merge Project Start\Input\Letters\starting_letter.txt', 'r') as file:
        letter = file.read()
        x = letter.replace('[name]', i)
    with open(fr'F:\Udemy 100 Days of Code\Day 24 Mail Merge\Mail Merge Project Start\Output\ReadyToSend\{i}.txt', 'w') as output:
        output.write(x)





#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
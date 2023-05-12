#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#path = """C:\Users\Usuario\Desktop\python_projects\merge_emails\Mail Merge Project Start\Names\invited_names.txt"""
names_path = r"""C:\Users\Usuario\Desktop\python_projects\merge_emails\Mail Merge Project Start\Input\Names\invited_names.txt"""
letter_path = r"""C:\Users\Usuario\Desktop\python_projects\merge_emails\Mail Merge Project Start\Input\Letters\starting_letter.txt"""
out_path = r"""C:\Users\Usuario\Desktop\python_projects\merge_emails\Mail Merge Project Start\Output\ReadyToSend"""
with open(names_path) as names:
    file_names = names.read().splitlines()
#print(file_names)
for names in file_names:
    with open(letter_path) as letter:
        edit_letter = letter.read()
    edit_letter = edit_letter.replace("[name]",names)
    print(edit_letter)
    with open(f"{out_path}\letter_for_{names}.txt",'x') as letter_edited:
        letter_edited.write(edit_letter)


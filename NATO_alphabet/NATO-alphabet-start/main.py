import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]}

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# {student:score for (student, score) in student_data_frame.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

NATO_path = r"""./NATO_alphabet/nato-alphabet-start/nato_phonetic_alphabet.csv"""
NATO = pd.read_csv(NATO_path)
NATO_dict = {row.letter:row.code for (index,row) in NATO.iterrows()}
print(NATO_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Which word did you say?: ").upper()
user_word = [NATO_dict[code] for code in user]
print(user_word)

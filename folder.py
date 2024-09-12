import os

words = [
    "Pencil",
    "Exam",
    "Result",
    "Curriculum/Lesson",
    "Eat",
    "Drink",
    "Sleep",
    "Play",
    "Work",
    "Bath",
    "Dress",
    "Brush",
    "Run",
    "Walk",
    "Sir",
    "Stand",
    "Write",
    "Clean",
    "Visit",
    "Tv",
    "Family",
    "Mother",
    "Father",
    "Sister",
    "Brother",
    "Friends",
    "Neighbour",
    "Doctor",
    "Nurse",
    "Hello",
    "Goodbye",
    "Please",
    "Thank you",
    "Sorry",
    "Teacher",
    "Student",
    "Desk",
    "Paper",
    "Grandfather",
    "Grandmother",
    "Uncle",
    "Aunt",
    "Son",
    "Daughter",
    "Husband",
    "Wife",
    "File",
    "Bag",
    "Clock",
    "Tree"
]

# Specify the directory where you want to create the folders
target_directory = "/Users/bugruster/Developer/MjrPrj/datafolders"

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Create folders for each word
for word in words:
    folder_path = os.path.join(target_directory, word)
    os.makedirs(folder_path)  # Use os.makedirs() to create folders and their parents
    print(f"Folder '{folder_path}' created successfully.")
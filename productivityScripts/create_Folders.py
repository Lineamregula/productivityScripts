import os

# Define the base path where you want to create the folders
base_path = r'C:\Users\samsk\Desktop'  # Change this to your desired path

# Define the folder structure as a dictionary
folder_structure = {
#   Examples
#   'Work': ['Projects', 'Meetings', 'Reports'],
#   'Chores': ['Cleaning', 'Groceries', 'Bills'],
#   'Study': ['Math', 'Science', 'Literature'],
    'Math-100': ['Lectures', 'Labs', 'Tutorials', 'Assignments' ],
    'CSC-105': ['Lectures', 'Labs', 'Tutorials', 'Assignments' ],
    'CSC-109': ['Lectures', 'Labs', 'Tutorials', 'Assignments' ],
    'ENGL-103': ['Lectures', 'Labs', 'Tutorials', 'Assignments' ],
    
}

# Create the folders and subfolders
for folder_name, subfolders in folder_structure.items():
    # Combine the base path with the folder name
    folder_path = os.path.join(base_path, folder_name)
    
    try:
        # Create the main folder
        os.makedirs(folder_path, exist_ok=True)
        print(f"Main folder created: {folder_path}")
        
        # Create each subfolder within the main folder
        for subfolder_name in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"  Subfolder created: {subfolder_path}")
            
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")

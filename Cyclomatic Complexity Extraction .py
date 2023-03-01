import lizard
import os 
import pandas as pd 

# Define directory path
dir_path = "C:\\Users\\Asus\\Desktop\\Mining Software Repositories Lab - test\\JavaFiles"
df = pd.DataFrame(columns=["file name", "CCN"])

# Loop over files in directory
for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)
    results = lizard.analyze_file(file_path)
    # Get Cyclomatic Complexity value from results
    ccn = results.average_cyclomatic_complexity
    # Print Cyclomatic Complexity value
    #print(f"Cyclomatic Complexity of {file_path}: {ccn}")
    df = df.append({"file name":filename, "CCN":ccn}, ignore_index=True)

df.to_excel("C:\\Users\\Asus\\Desktop\\Mining Software Repositories Lab - test\\CCN_JavaFiles.xlsx", index=False)
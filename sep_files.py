
def separate_files(files):
    numeric_files = []
    text_files = []
    for file in files:
        if file.split('.')[0].isdigit():
            numeric_files.append(file)
        else:
            text_files.append(file)
    return numeric_files, text_files
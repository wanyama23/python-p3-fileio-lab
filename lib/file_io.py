def write_file(file_name, file_content):
    file_path = str(file_name) +'.txt'
    with open(file_path,mode='w',) as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_path = str(file_name) +'.txt'
    with open(file_path,mode='a',) as file:
        file.write(append_content)
    

def read_file(file_name):
    file_path = str(file_name) +'.txt'
    with open(file_path,mode = 'r') as file:
        file_content=file.read()
        return file_content

    
def save_data(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_data(filename):
    try:
        with open(filename,"r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
def save_int(filename, int_number):
    save_str(filename, str(int_number))


def load_int(filename):
    with open(filename) as f:
        int_number = int(f.read())
    return int_number


def save_str(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


def append_str_to_txt_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)


def load_str(filename):
    with open(filename) as f:
        return f.read()

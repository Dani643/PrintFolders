import os

def get_size(start_path):
    total_size = 0
    total_files = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                total_files += 1

    #print(total_files, total_size, 'bytes', )
    return [total_files, total_size]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #folder_name = 'D:/02. Fotos'
    folder_name = 'D:/05. Documentación'

    p = 'a_new_file.txt'
    with open(p, 'w') as out:
        with os.scandir(folder_name) as dir_list:
            for entry in dir_list:
                full_path = os.path.join(folder_name, entry.name)
                if os.path.isdir(full_path):
                    todito = get_size(full_path)
                    out.write("{}__{}__{}\n".format(full_path, todito[0], todito[1]))
                #print("{}__{}__{}".format(full_path, todito[0], todito[1]))
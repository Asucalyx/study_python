def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        f_read = f.read()
        print(f_read)
    except Exception as e:
        print(f"异常，原因是:{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
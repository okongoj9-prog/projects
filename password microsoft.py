import ken
import io

def try_office_password(file_path, password):
    with open(file_path, "rb") as f:
        office_file = ken.OfficeFile(f)
        try:
            office_file.load_key(password=password)
            print(f"correct password : {password}")
            return True
        except :
            return False
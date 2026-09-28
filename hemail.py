while True:
    try:
        email = input("enter your email: ")
        if email.count("@") != 1:
            raise ValueError
        username, domain = email.split("@")
        if username =="":
            raise ValueError
        if "-" not in domain:
            raise ValueError
        
        print("----Vlid email------")
        print(f"username: {username}")
        print(f"domain: {domain}")
        break
    except ValueError:
        print("invalid email format")


def login_req(funct):
    def wrapper(user):
        if user == "admin":
            funct(user)
        else:
            print("access denied")
    return wrapper


@login_req
def view_dashboard(user):
    #print(f"welcome {user} here is your dashboard") we can use this or nxt statement this also works
    print("welcome {} here is your dashboard".format(user))
    
view_dashboard("admin")
view_dashboard("siri")
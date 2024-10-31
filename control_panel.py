import shortuuid , random
 
def generate_id():    
    return (shortuuid.random(length=3))

generate_id()

users = []

##############################
def add_user():
    try:
        print("#"*30)
        id = generate_id()
        print("Add user")
        name = input("Enter name:\t")
        user = {"id" : id, "name" : name}
        users.append(user)
        show_menu()
    except Exception as e:
        show_menu()

 
##############################
def show_user():
    try:
        print("#"*30)
        header = "id\t\tname"
        print(header)
        name = input("Enter the name of the user: ")
        for user in users:
            if user["name"] == name:
                print(f"{user['id']}\t\t{user['name']}")
    except Exception as ex:
        print(ex)
    finally:
        show_menu()

    
 
##############################
def update_user():
    print("#"*30)
    print("Update user")
 
##############################
def show_users():
    try:
        print("#"*30)
        print("Show users")
        header = "id\t\tname"
        print(header)
        for user in users:
            row = user["id"]+"\t\t"+user["name"]
            print(row)  
    except Exception as ex:
        print(ex)
    finally:
        # it runs after the try or except.
        # No matter if the try or except runs
        show_menu()  
 
##############################
def delete_user():
    try:
        print("#" * 30)
        print("Delete user")
        for user in users:
            print(user)
        print("Delete user")
        id = input("Enter the id of the user you want to delete: ")
        for user in users:
            if user["id"] == id:
                users.remove(user)
                print(f"User with id {id} deleted")
                break
    except Exception as e:
        print(e)
        show_menu()
    finally:
        show_menu()
 
 
##############################
def show_menu():
    print("#"*30)
    print("1. Add a user")
    print("2. See details about a user")
    print("3. Update a user")
    print("4. See all users")
    print("5. Delete a user")
    print("9. Back to main menu")
    print("x. quit")

    option = input("Choose an option:\t")  
    # print(option) # any chosen key
    # print(type(option)) # class str
    if option == "1": add_user()
    if option == "2": show_user()
    if option == "3": update_user()
    if option == "4": show_users()
    if option == "5": delete_user()
    if option == "x": exit()
    show_menu()
 
show_menu()
 
 
     
 
 
 
 
 
 
 



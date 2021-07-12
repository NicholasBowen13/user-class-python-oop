class User:
    def __init__(self, first_name, last_name, number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.password = password
        print("New user created")
    def status_update(self, mood):
        self.mood = mood
    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
        else: 
            print("Passwords don't match")
        nick13.change_password("old_password", new_password)

nick13 = User("Nicholas", "Bowen", 763463489, "Nick13@gmail.com", 89)
nick13.mood = "Happy"

print(nick13.mood)

nick13.change_password
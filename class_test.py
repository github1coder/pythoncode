# user1={'name':'tom','hp':100}
# user2={'name':'jerry','hp':80}

# def print_role(rolename):
#     print('%s %s'%(rolename['name'],rolename['hp']))

# print_role(user1)


class player():
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def print_role(self):
        print('%s: %s'%(self.name,self.hp))


user1 = player('tom',100)
user2 = player('jerrt',90)
user1.print_role()
user2.print_role()
import file_manager as fm
import entry as en

#initializing the data base
db = fm.database()
db.set_path("scores.txt")

scores = []

def update(table):
    db.replace(table)


#if the database is ok then we will continue into the program
if db.integrity_test():
    help_count = 0
    scores = db.get_table()
    while True:
        update(scores)
        opt = input(">>>")
        opt = opt.split(" ")
        if opt[0] == "help" or opt[0] == "man":
            print("Help menu")
            print("print - prints out all the students")
            print("add <score> - adds the student id and score to the database")
            print("remove/delete/rem <id> <stop> - removes the student with the specified id and if specified,"
                  "removes students until the stop id is reached. The stop parameter is optional")
            print("modify/mod <id> <score> - modifies the student with the specified id and changes its score to the specified score")
            help_count = 0
        elif opt[0] == "print":
            for row in scores:
                print(row.to_string())
        elif opt[0] == "add" :
            try:
                x = en.entry()
                tx = int(opt[1])
                x.create_entry(db.get_entries() + 1,tx)
                if x.add_entry(scores):
                    print("user added succesfully")
                    help_count = 0
                else:
                    print("user already existing")
            except:
                print("insert only one int after the command ")
        elif opt[0] == "remove" or opt[0] == "rem" or opt[0] == "delete":
            try:
                tx = int(opt[1])
                ty = int(opt[2])
                for i in range(tx,ty + 1):
                    x = en.entry()
                    x.set_id(i)
                    if x.rem_entry(scores):
                        print("users removed successfully")
                    else:
                        print("unable to remove the users. Maybe wrong indexes?")
                    help_count = 0
            except:
                try:
                    tx = int(opt[1])
                    x = en.entry()
                    x.set_id(tx)
                    if x.rem_entry(scores):
                        print("user removed successfully")
                    else:
                        print("unable to remove the user. Maybe wrong index?")
                    help_count = 0
                except:
                    print("insert the correct index")
        elif opt[0] == "modify" or opt[0] == "mod":
            try:
                tx = int(opt[1])
                ty = int(opt[2])
                x = en.entry()
                x.create_entry(tx,ty)
                if x.mod_entry(scores):
                    print("user modified successfully")
                else:
                    print("unable to modify the user. Maybe wrong index?")
                help_count = 0
            except:
                print("please insert only ints after the command")
        elif help_count >= 2:
            print('Maybe typing "help" will... help')
        else:
            print("Please insert a valid instruction")
            help_count += 1
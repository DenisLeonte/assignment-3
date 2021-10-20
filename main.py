import file_manager as fm

db = fm.database()
db.set_path("scores.txt")

scores = []

def update():
    db.set_entries()
    n = db.get_entries()
    tx_score = []
    for i in range (1,n+1):
        tx = db.get_entry(i)
        tx_score.append(tx)
    return tx_score

if db.test():
    while True:
        scores = update()
        opt = input(">>>")
        opt = opt.split(" ")
        if opt[0] == "print":
            for row in scores:
                print(row)
        elif opt[0] == "add":
            tx = [0,"",0,0,0,0,0,0,0,0,0,0,0]
            tx[1] = opt[1]
            complete = True
            db.set_entries()
            tx[0] = db.get_entries()+1
            for i in range(3,13):
                try:
                    tx[i] = int(opt[i-1])
                    tx[2] += tx[i]
                except:
                    print("Insert only ints after the name")
                    complete = False
                    break
            if complete:
                db.add_entry(tx)
        elif opt[0] == "delete" or opt[0] == "remove" :
            try:
                entry = opt[1]
                until = opt[2]
                db.remove_entry(entry,until)
            except:
                try:
                    entry = opt[1]
                    db.remove_entry(entry)
                except:
                    print("Invalid values")
        elif opt[0] == "quit" or opt[0] == "exit":
            break
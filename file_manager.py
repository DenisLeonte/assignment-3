import csv

class database:
    __path = ""
    __entries = 0

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def set_entries(self):
        with open(self.__path) as f:
            for row in f:
                self.__entries += 1

    def get_entries(self):
        return self.__entries

    def get_entry(self, entry):
        try:
            tx = int(entry)
            with open(self.__path) as f:
                reader = csv.reader(f)
                for row in reader:
                    if int(row[0]) == tx:
                        return row
        except:
            tx = entry
            with open(self.__path) as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[1] == tx:
                        return row

    def __generate_entry(self, entry):
        tx = ""
        tx += str(entry[0])
        for i in entry[1::]:
            tx += ","+str(i)
        tx += " \n"
        return tx

    def add_entry(self, entry):
        tx = self.__generate_entry(entry)
        with open(self.__path, "a") as f:
            f.write(tx)

    def test(self):
        i = 1
        with open(self.__path) as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    tx = int(row[0])
                    for i in range(2,12):
                        tx = int(row[i])
                    i+=1
                except:
                    print("Problem at line ",i)
                    return False
        return True

    def modify_entry(self,entry):
        tx = []
        with open(self.__path,"r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == entry[0]:
                    tx.append(entry)
                else:
                    tx.append(row)
        with open(self.__path, "w") as f:
            for row in tx:
                entry = self.__generate_entry(row)
                f.write(entry)

    def remove_entry(self,entry, until = -1):
        try:
            tx = int(entry)
            ty = int(until)
            temp_scores = []
            with open(self.__path,"r") as f:
                for row in f:
                    row = row.split(",")
                    if until == -1 and int(row[0]) == entry:
                        pass
                    elif until != -1 and (int(row[0]) >= entry and int(row[0]) <= until) or (int(row[0]) <= entry and int(row[0]) >= until):
                        pass
                    else:
                        temp_scores.append(row)
            with open(self.__path,"w") as f:
                for row in temp_scores:
                    tz = self.__generate_entry(row)
                    f.write(tz)
        except:
            print("Insert valid values")
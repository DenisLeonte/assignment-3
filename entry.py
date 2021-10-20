# entry class
# will be thigthly implemented in the database class,
# having its setters, getters, generating function and variables
class entry:
    # private variables
    __id = 0
    __score = 0

    # setters
    # sets the id in the object. Only accepts int as a parameter
    def set_id(self, id: int):
        try:
            self.__id = id
        except:
            print("Invalid ID value")

    # sets the score in the object. Only accepts int as a parameter
    def set_score(self, score: int):
        try:
            self.__score = score
        except:
            print("Invalid score value")

    # getters
    # gets the id from the object. Returns an int
    def get_id(self):
        return self.__id

    # gets the score from the object. Returns an int
    def get_score(self):
        return self.__score

    # generators
    # generate a string object from the entry object.
    # the string object will be generated in the csv format and then returned
    def to_string(self):
        tx = str(self.__id) + "," + str(self.__score)
        return tx

    # converts a string and generates an entry from it. Takes a string as a parameter
    def to_entry(self, row):
        row = row.split(",")
        self.__id = int(row[0])
        self.__score = int(row[1])

    # same as the setters but does both at once. Takes 2 int parameters
    def create_entry(self, id, score):
        self.__id = id
        self.__score = score

    # I/O functions
    # adds the object to the database. Returns a bool if the operation was successfull
    def add_entry(self, scores):
        for row in scores:
            if row.get_id() == self.__id:
                return False
        scores.append(self)
        return True

    # removes the object from the database. Returns a bool if the operation was successfull
    def rem_entry(self, scores):
        for row in scores:
            if row.get_id() == self.__id:
                del (row)
                return True
        return False

    # modifies the object in the database. Returns a bool if the operation was successfull
    def mod_entry(self, scores):
        for row in scores:
            if row.get_id() == self.__id:
                row.set_score = self.__score
                return True
        return False

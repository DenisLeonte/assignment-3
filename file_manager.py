import entry as en


# database class
# the purpose of this class is to facilitate communication
# between the main program and the database
class database:
    # private variables
    __path = ""
    __entries: int = 0

    # setters
    # sets the pat of the database. Only accepts string as its parameter
    def set_path(self, path: str):
        self.__path = path

    # sets the number of entries. Has an optional int parameter that should be used for testing purposes only.
    # Private function
    def __set_entries(self, entries: int = -1):
        if entries == -1:
            self.__entries = 0
            with open(self.__path, "r") as f:
                for row in f:
                    self.__entries += 1
        else:
            self.__entries = entries

    # getters
    # gets the number of entries. Returns an int
    def get_entries(self):
        self.__set_entries()
        return self.__entries

    # testers
    # test the row for any non int elements. Takes a string as a parameter. Returns a bool
    # Private function
    def __row_test(self, row: str):
        row = row.split(",")
        try:
            for i in row:
                int(i)
            return True
        except:
            return False

    # test the entire file trying to find a non int element. Returns a bool
    def integrity_test(self):
        i = 1
        with open(self.__path, "r") as f:
            for row in f:
                if not self.__row_test(row):
                    print("Problem at row ", i)
                    return False
                i += 1
        return True

    # I/O functions
    # replace the entire database with a new one
    def replace(self, scores):
        with open(self.__path, "w") as f:
            for row in scores:
                f.write(row.to_string())

    # returns the entire database in a matrix. Return a table
    def get_table(self):
        table = []
        with open(self.__path, "r") as f:
            for row in f:
                x = en.entry()
                x.to_entry(row)
                table.append(x)
        return table

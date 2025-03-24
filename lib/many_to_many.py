class Author:
    all = []

    def __init__(self, name=""):
        self.name = name 
        Author.all.append(self)
        self._contracts = []

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [book for book in Book.all if book._author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties) 
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []

    def __init__(self, title="", author=None):
        self.title = title
        self._author = author
        Book.all.append(self)
        self._contracts = []
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def add_contracts(self, contract):
        self._contracts.append(contract)

    def authors(self):      
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties=0):
        self.author_name = author
        self.book = book
        self.date = date
        self._royalties = royalties 

        if not isinstance(author, Author):
            raise Exception("Invalid author type. Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise TypeError("Invalid date type. Date must be a string.")
        if not isinstance(royalties, int):
             raise Exception("Royalty percentage must be an int")

        
        Contract.all.append(self)
        book._author = author
        author._contracts.append(self)  

    @property
    def author(self):
        return self.author_name

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Author has to be a string")
        self._name = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalty percentage must be an int")
        # if value < 0 or value > 100:
        #     raise Exception("Royalty percentage must be between 0 and 100")
        self._royalties = value


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

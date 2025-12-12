# super class
class Person:
    
    # public data member
    name = None

    # protected data member
    _age = None

    # private data member
    __aadhar = None

    # constructor
    def __init__(self, name, age, aadhar):
        self.name = name          # public
        self._age = age           # protected
        self.__aadhar = aadhar    # private

    # public member function
    def showName(self):
        print("Public Data (Name):", self.name)

    # protected member function
    def _showAge(self):
        print("Protected Data (Age):", self._age)

    # private member function
    def __showAadhar(self):
        print("Private Data (Aadhar):", self.__aadhar)

    # public function to access private data
    def accessPrivate(self):
        self.__showAadhar()


# derived class
class Student(Person):

    # constructor
    def __init__(self, name, age, aadhar):
        Person.__init__(self, name, age, aadhar)

    # public function to access protected members
    def accessProtected(self):
        self._showAge()


# creating object of subclass
s = Student("Siri", 22, "1234-5678-9999")

# calling public methods
s.showName()
s.accessProtected()
s.accessPrivate()

# accessing protected variable (allowed but not recommended)
print("Accessing protected variable directly:", s._age)

# accessing private variable directly → ERROR
# print(s.__aadhar)

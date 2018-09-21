class Employee:
    
    __matricule_pointer = 100000

    def __init__(self, name, surname, nb_enfant, date_arrive, years_of_experience=0):
        self.__name = name
        self.__surname = surname
        self.__nb_enfant = nb_enfant
        self.__date_arrive = date_arrive
        self.__login = self.make_login()
        self.__years_of_experience = years_of_experience

        # must be defined by daughter class
        self.__salaire = None
        self.__vacation = None

        # initialize the matricule
        self.__matricule = Employee.__matricule_pointer
        Employee.__matricule_pointer += 1
    
    def make_login():
        return self.surname[0] + self.name[0] + str(self.__matricule)

    def get_login():
        return self.__login
    
    def calculate_salary(self):
        self.__salaire.calculate(self.__nb_enfant)
    
    def calculate_vacation(self):
        self.__vacation.calculate()

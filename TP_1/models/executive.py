from employee import Employee

class Executive(Employee):
    def __init__(self, name, surname, nb_enfant, date_arrive, tel=None):
        super(name, surname, nb_enfant, date_arrive)

        self.__employee_type = "Executive"
        self.__employee_status = "Business"
        self.__tel = tel
        self.__salaire = Salaire(self.__employee_type)
        self.__conge = Conge(self.__employee_type)


# This Company class is the master class, ie it's the main models which refers to
# all the other model of this project.

class Company:
    def __init__(self):
        self.__employee_dict = {}
        self.__available_type = ["Employe","Cadre","Directeur"]
    
    def create_employe(self,employee_type,name,surname,mobile=None):
        new_matricule = self.__generate_matricule()
        if employee_type in self.__available_type:
            self.employee_dict[new_matricule] = 
        else:
            print("{} is not a known type of employee.".format(employee_type))
    
    def get_employee_list(self):
        return self.__employee_dict.values()
    
    def get_employee(self,matricule):
        if matricule in self.__employee_dict:
            return self.__employee_dict[matricule]
        else:
            print("Error, there is no employee with the id {}.".format(matricule))
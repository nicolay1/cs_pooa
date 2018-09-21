import date from datetime

class Vacation:

    __base_annual_vacation = 5

    def __init__(self, date_now):
        # rtt
        self.__rtt = []
        self.__nb_rtt = __calculate_rtt_year_prorata(date_now)

        # annual vacation
        self.__annual_vacation = []
        self.__nb_annual_vacation = self.__base_annual_vacation

        # last reset
        self.__last_reset = None
    
    def reset_if_needed(self):
        pass
    
    def __calculate_rtt_year_prorata(self, date_now):
        # calculate the distance between the actual date in the year and it's
        # beginning, used to calculate the prorata
        rtt = 52 - int(
            52*(date_now - date(date_now.year)) 
            // 
            (365
                + (date_now.year % 4 == 0)
                - (date_now.year % 100 == 0)
                + (date_now.year % 400 == 0)
            )
        )/2
    
    def take_rtt(self,)
    
    def __calculate_rtt(employee_type):

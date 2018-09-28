import date from datetime

class Vacation:

    __base_annual_vacation = 5

    def __init__(self, date_now, employee_type):
        # rtt
        self.__rtt = []
        self.__rtt_available = employee_type == "Executive"
        self.__nb_rtt = __calculate_rtt_year_prorata(date_now)

        # annual vacation
        self.__annual_vacation = []
        self.__nb_annual_vacation = self.__base_annual_vacation

        # last reset
        self.__last_reset = date_now
        self.
    
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
    
    def take_rtt(self,rtt_list):
        # rtt_list must be a list of dict :
        # {date: date(datetime), type:[morning|afternoon|all_day]}

        if not __rtt_available:
            print("Error, this type of employee does not apply to RTT.")
            return

        # we calculate the rtt cost as the sum of all the rtt the user as asked for
        # we imply that all rtt given are unique.
        rtt_cost = sum([map(lambda x: 1 if x.type == "all_day" else 0.5,rtt_list)])

        # first, employee must have enough rtt
        if self.__nb_rtt < rtt_cost:
            print("Not enough rtt available to process the RTT query.")
        
        # then we check for each rtt in the rtt list if it's okay
        for rtt_to_be_taken in rtt_list:
            is_rtt_okay = True
            for rtt_taken in self.__rtt:
                if (rtt_taken.date.isoformat() == rtt_to_be_taken.date.isoformat:
                    and (rtt_to_be_taken.type == rtt_taken.type or rtt_taken.type=="all_day")):
                    print("Warning, rtt as been alreeady taken : {} {}".format(
                        rtt_taken.date.isoformat(),
                        rtt_to_be_taken.type
                    ))
                    is_rtt_okay = False
            if is_rtt_okay:
                self.__rtt.append(rtt_to_be_taken)
    
    def __calculate_rtt(employee_type):

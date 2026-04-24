class EmployeeDetails:
    def __init__(self, e_no, e_name, bsc_pay):         #construcator
        self.__e_no = e_no
        self.__e_name = e_name
        self.__bsc_pay = bsc_pay
        self.__da = 20.0          #standard set by client
        self.__hra = 10.0         #standard set by client
        self.__pf = 5.5           #standard set by client

    #def get_e_no(self):
    #    return self.__e_no
    #def set_e_no(self, eno):
    #    self.__e_no = eno
    @property
    def e_no(self):
        return self.__e_no
#    @e_no.setter
#    def e_no(self, eno):
#        self.__e_no = eno

    @property
    def e_name(self):
        return self.__e_name
#    @e_name.setter
#    def e_name(self, en):
#        self.__e_name = en
    @property
    def bsc_pay(self):
        return self.__bsc_pay
#    @bsc_pay.setter
#    def bsc_pay(self,bp):
#        self.__bsc_pay = bp


    def __calculate_allowance(self):
        allowance = (self.__bsc_pay * self.__da / 100) + (self.__bsc_pay * self.__hra / 100)
        return allowance


    def __calculate_deduction(self):
        deduction = (self.__bsc_pay * self.__pf / 100)
        return deduction

    def calculate_netsal(self):
        netsal = self.__bsc_pay + self.__calculate_allowance() - self.__calculate_deduction()
        return netsal
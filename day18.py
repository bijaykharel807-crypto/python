
class A():
    a = 10
    __b =11

    def __test(self):
        return "this is for public method"

    def public_test(self):
        return self.__test() + "modified"

    password = "12345"

    def login(self):
        if self.password =="12345":
            return "login success"

class B(A):
    data = "this is public"


try:
    obj = A()
    # print(obj.b)
    print(obj.b)
except AttributeError as e:
    print(e)



class Hosiptal():
    hospital_name="RAHS"
    location="Dang"
    __license_number="RAHS-12-34"
    pub_lic = __license_number +"123"

    def hospital_info(self):
        result = f'hospital name:{self.hospitsal_name} {self.__license_number}'
        return result

class Doctor(Hosiptal):
    doctor_name="121"
    specialization="1212"

    def doctor(self):
        return f'{self.doctor_name} {self.hospital_name}'


obj = Doctor()

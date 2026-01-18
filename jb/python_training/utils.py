
class Utils_jb61:

    def age_calculator(self,age,ref_age=18):
        if age>ref_age:
            print(f"age is greater than {ref_age}")
            age_new =age+5
        else :
            print(f"age is less than {ref_age}")
            age_new =age-5

        return age_new

    def email_validator(email):
        print("trying to analyze if email is valid ")

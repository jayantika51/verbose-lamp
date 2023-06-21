class Doctor():
    def__init__(self):
        print("This is class Doctor")
        
    def BMI(weight, height):
        bmi = weght/(height*height)
        print("Your BMI is"+str(bmi))
        
    def heart_rate(heart_rates) 
        if(heart_rates>60 and heart_rates<1000):
            print("Great your heart rate is normal")
        else:
            print("You heart rate does not seem normal,please visit the clinic ")

class Paitent(Doctor):
      
    def__init__(self, name, weight, height, heart_rates):
         self.paitent_name= name
         self.paitent_weight=weight
         self.paitent_height=height
         self.paitent_heart_rates = heart_rates
       
      def healthCheck(self):
          print("\n Patient Name:", self.paitent_)
          Doctor.BMI(self.paitent_weight, self.paitent_height)
          Doctor.heart_rate(self.patient_heart_rates)
          

paitent1 = Paitent("Michel", 30, 0.9144, 80)
patient1.healthCheck()

patient2 = Paitent("Jenna", 42, 5, 100)
paitent2.healthCheck()

paitent3 = Paitent("Cassey", 25, 7, 95)
patient3.healthCheck()

patient4 = Patient("Katey", 50, 6.5, 105)
patient4.healthCheck()          
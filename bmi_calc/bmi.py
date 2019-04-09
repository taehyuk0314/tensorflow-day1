class Bmi:

        def __init__(self,name,t,w):
            self.name = name
            self.t = t
            self.w = w




        def bm(self):
             bmi = (self.w / (self.t * self.t)) * 10000
             if  bmi >= 40 : return "고도비만"
             elif bmi >=35 : return "중도비만"
             elif bmi >=30 : return "경도비만"
             elif bmi >=25 : return "과체중"
             elif bmi >=18.5 : return "정상"
             else : return "저체중"


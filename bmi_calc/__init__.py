from bmi_calc.bmi import Bmi

def main():

    bmi = Bmi(input("이름")
        ,float(input("키"))
        ,float(input("몸무게")))
    print("{}님의 bmi는 {} 입니다"
          .format(bmi.name
                  ,bmi.bm()))


if __name__ == '__main__':
    main()
class mulFunc:
    def Subfields():
        AI=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        for list in AI:
            print(list,end='\n')
    def oddEven():
        num=int(input("Enter the number:"))
        if ((num%2) == 1):
             print("Odd Number")
             msg="Odd Number"
        else:
            print("Even Number")
            msg="Even Number"
        return msg
    
    def BMI():
        bmi_index = float(input("Enter the BMI Index :"))
        if (bmi_index < 18.5):
            print("Under Weight")
            msg="Under Weight"
        elif(bmi_index < 24.9):
            print("Normal Weight")
            msg="Normal Weight"
        elif(bmi_index < 29.9):
            print("Pre-obesity")
            msg="Pre-obesity"
        elif(bmi_index < 34.9):
            print("Very Overweight")
            msg="Very Overweight"
        elif(bmi_index < 39.9):
            print("Obesity Class-II")
            msg="Obesity Class-II"
        else:
            print("Obesity Class-III")
            msg="Obesity Class-III"
        return msg
    
    def Elegible():
        gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gen=="Male"):
            if (age >=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gen=="Female"):
            if (age >=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
    def percentage():
        import decimal
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        per=decimal.Decimal(total/5)
        print ("Total : ",total)
        print ("Percentage : ",per)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=float((height*breadth)/2)
        print ("Area of Triangle:",area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        peri=h1+h2+b1
        print ("Perimeter of Triangle:",peri)

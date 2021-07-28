def input_data():
      amount = float(input("Enter the amount of the bill: "))
      period = input("Enter the period of the bill--'month year': ")

      flatmate1 = input('Enter the name of the flatmate1: ')
      days_in_house1 = int(input("Enter the number of the days flatmate1 \
stayed on the flat: "))
      flatmate2 = input("Enter the name of the flatmate2: ")
      days_in_house2 = int(input("Enter the number of the days flatmate2 \
stayed on the flat: "))

      return amount, period, flatmate1, days_in_house1, flatmate2,\
      days_in_house2

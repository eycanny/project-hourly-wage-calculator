# Project Idea: Make a calculator based on pay rate times amount of time worked.

# Overall Flow
  # Greet the user
  # Ask for user's pay rate
    # Convert input into XX.XX format
    # Screen for valid inputs
    # Repeat back to user what they have inputted as pay rate
  # Ask user to confirm pay rate
    # If no, allow user to edit
    # If yes, print message confirming pay rate
  # Ask for time worked in hours, minutes, and seconds
    # Screen for valid inputs
    # Repeat back to user what they have inputted as time worked
   # Ask user to confirm time worked
    # If no, allow user to edit
    # If yes, print message confirming time worked
  # Calculate result based on confirmed pay rate and time worked
    # Format result
  # Show user the result
  # Provide user with options
    # Do another calculation
    # Forecast multiple amounts
    # Apply tax rates
    # Quit program

# Greet the user
def greet_the_user():
  """This function greets the user and explains the application of the whole code"""
  print("Welcome!")
  print()
  print("This will calculate a dollar amount based on an hourly pay rate and total time worked in a month. This is meant to be helpful in calculating to the seconds.")

greet_the_user()

# Ask for and covert user's pay rate into a XX.XX format while screening for valid inputs
def get_pay_rate():
  """This function converts user's inputted pay rate into the appropriate format for calculations, tells user what they inputted, and returns this value for future use."""
  while True:
    print("\nPlease input hourly pay rate.")
    pay_rate = input("> ")

    if pay_rate == "":
      print("An hourly pay rate is required in order to calculate a dollar amount.")

    elif "." in pay_rate:
      dot_count = 0
      letter_count = 0
      for char in pay_rate:
        if char == ".":
          dot_count += 1
        if char in "abcdefghijklmnopqrstuvwxyz":
          letter_count += 1

      if (dot_count > 1) or (letter_count > 0):
        print("That is invalid. Please try again.")

      else:
        float_of_pay_rate = float(pay_rate)
        formatted_pay_rate= "{:.2f}".format(float_of_pay_rate)
        break
        
    elif pay_rate.isnumeric(): #or not pay_rate.isalnum():
      float_of_pay_rate = float(pay_rate)
      formatted_pay_rate= "{:.2f}".format(float_of_pay_rate)
      break

    else:
      print("That is invalid. Please try again.")
    
  print("\nYou have entered ${} as your hourly pay rate.".format(formatted_pay_rate))

  return formatted_pay_rate

# Ask user to confirm pay rate or to edit pay rate.
def confirm_pay_rate():
  """This function allows the user to confirm pay rate if correct and edit if incorrect. Prints message confirming pay rate."""
  formatted_pay_rate = get_pay_rate()

  while True:
    print("\nWas the statement about your hourly pay rate correct? (YES or NO)")
    user_confirmation = input("> ")
    user_confirmation = user_confirmation.upper()

    if user_confirmation == "NO":
      print("\nOk, let's change it.")
      formatted_pay_rate = get_pay_rate()

    elif user_confirmation == "YES":
      print("\nConfirming ${} as your hourly pay rate.".format(formatted_pay_rate))
      break
      
    else:
      print("That is not a valid option.")

  confirmed_pay_rate = formatted_pay_rate
  return confirmed_pay_rate

# Ask user for amount of time worked in hours, minutes, and seconds
def get_time_worked():
  """This function gets user input for time worked in hours, minutes, and seconds while screening for invalid inputs."""

  print("\nPlease input hours, minutes, and seconds with numeric values for total time worked in a month.")
  print("You will be asked for each unit of time separately.")
  print()

  time_worked = []

  # Loop for numeric values
  while True:
    hours = input("How many hours? > ")

    if hours.isnumeric():
      hours = int(hours)
      time_worked.append(hours)
      break
    else:
      print("You have entered an invalid character. Try again.")
      print()

  while True:
    minutes = input("How many minutes? > ")

    if minutes.isnumeric():
      minutes = int(minutes)
      time_worked.append(minutes)
      break
    else:
      print("You have entered an invalid character. Try again.")
      print()

  while True:
    seconds = input("How many seconds? > ")

    if seconds.isnumeric():
      seconds = int(seconds)
      time_worked.append(seconds)
      break
    else:
      print("You have entered an invalid character. Try again.")
      print()

  print("\nYou have entered {} hours, {} minutes, and {} seconds as time worked.".format(hours, minutes, seconds))

  return time_worked


# Ask user to confirm time worked or to edit time worked.
def confirm_time_worked():
  """This function allows the user to confirm time worked if correct and edit if incorrect. Prints message confirming time worked."""
  
  time_worked = get_time_worked()

  while True:
    print("\nWas the statement about your amount of total time worked correct? (YES or NO)")
    user_confirmation = input("> ")
    user_confirmation = user_confirmation.upper()

    if user_confirmation == "NO":
      print("\nOk, let's change it.")
      print()
      
      time_worked = []

      # Loop for numeric values
      while True:
        hours = input("How many hours? > ")

        if hours == "":
          hours = 0
          time_worked.append(hours)
          break

        elif hours.isnumeric():
          hours = int(hours)
          time_worked.append(hours)
          break

        else:
          print("You have entered an invalid character. Try again.")
          print()

      while True:
        minutes = input("How many minutes? > ")

        if minutes == "":
          minutes = 0
          time_worked.append(minutes)
          break
        
        elif minutes.isnumeric():
          minutes = int(minutes)
          time_worked.append(minutes)
          break
        
        else:
          print("You have entered an invalid character. Try again.")
          print()

      while True:
        seconds = input("How many seconds? > ")

        if seconds == "":
          seconds = 0
          time_worked.append(seconds)
          break

        elif seconds.isnumeric():
          seconds = int(seconds)
          time_worked.append(seconds)
          break

        else:
          print("You have entered an invalid character. Try again.")
          print()

      print("\nYou have entered {} hours, {} minutes, and {} seconds as time worked.".format(hours, minutes, seconds))

    elif user_confirmation == "YES":
      print("\nConfirming {} hours, {} minutes, and {} seconds as total time worked in a month.".format(time_worked[0], time_worked[1], time_worked[2]))
      break
      
    else:
      print("That is not a valid option.")

  confirmed_time_worked = [time_worked[0], time_worked[1], time_worked[2]]
  return confirmed_time_worked


def convert_time_worked_into_hours(amount_of_time_worked):
  """This function converts time into a float."""
  time_worked_in_hours = amount_of_time_worked[0] + (amount_of_time_worked[1] / 60) + (amount_of_time_worked[2] / 3600)
  converted_time_worked = time_worked_in_hours
  return converted_time_worked

def show_calculated_dollar_amount():
  confirmed_pay_rate = confirm_pay_rate()
  confirmed_time_worked = confirm_time_worked()
  converted_time_worked = convert_time_worked_into_hours(confirmed_time_worked)

  import time
  countdown = 5

  time.sleep(2)

  print()
  print("Showing calculated dollar amount based on pay rate of ${} and total time worked of {} hours, {} minutes, and {} seconds in...".format(confirmed_pay_rate, confirmed_time_worked[0], confirmed_time_worked[1], confirmed_time_worked[2]))

  time.sleep(1)

  while countdown > 0:
    print(countdown, "...")
    time.sleep(1)
    countdown = countdown - 1

  # Result = Pay Rate x Time Worked
  calculated_dollar_amount = float(confirmed_pay_rate) * float(converted_time_worked)

  calculated_dollar_amount = "{:.2f}".format(calculated_dollar_amount)

  print("\nYour calculated dollar amount is ${}!".format(calculated_dollar_amount))

  while True:
    print()
    print("What would you like to do next?")
    print()
    print("[1] Do another calculation")
    print("[2] Forecast amounts for 1 month, 3 months, 6 months, and 12 months")
    print("[3] Calculate a percentage of calculated amount")
    print("[4] Quit the program")
    print()

    user_choice = input("> ")

    if user_choice == "1":
      confirmed_pay_rate = confirm_pay_rate()
      confirmed_time_worked = confirm_time_worked()
      converted_time_worked = convert_time_worked_into_hours(confirmed_time_worked)

      import time
      countdown = 5

      time.sleep(0.25)

      print()
      print("Showing calculated dollar amount based on pay rate of ${} and total time worked of {} hours, {} minutes, and {} seconds in...".format(confirmed_pay_rate, confirmed_time_worked[0], confirmed_time_worked[1], confirmed_time_worked[2]))

      time.sleep(0.75)

      while countdown > 0:
        print(countdown, "...")
        time.sleep(0.5)
        countdown = countdown - 1

      # Result = Pay Rate x Time Worked
      calculated_dollar_amount = float(confirmed_pay_rate) * float(converted_time_worked)

      calculated_dollar_amount = "{:.2f}".format(calculated_dollar_amount)

      print("\nYour calculated dollar amount is ${}!".format(calculated_dollar_amount))
      
    elif user_choice == "2":
      calculated_dollar_amount = float(confirmed_pay_rate) * float(converted_time_worked)
      calculated_dollar_amount = "{:.2f}".format(calculated_dollar_amount)

      calculated_dollar_amount1 = float(confirmed_pay_rate) * float(converted_time_worked) * 3
      calculated_dollar_amount1 = "{:.2f}".format(calculated_dollar_amount1)

      calculated_dollar_amount2 = float(confirmed_pay_rate) * float(converted_time_worked) * 6
      calculated_dollar_amount2 = "{:.2f}".format(calculated_dollar_amount2)

      calculated_dollar_amount3 = float(confirmed_pay_rate) * float(converted_time_worked) * 12
      calculated_dollar_amount3 = "{:.2f}".format(calculated_dollar_amount3)

      print()
      print("Forecasting based on provided hourly pay rate and total time worked in a month...")
      print("1 month = ${}".format(calculated_dollar_amount))
      print("3 months = ${}".format(calculated_dollar_amount1))
      print("6 months = ${}".format(calculated_dollar_amount2))
      print("12 months = ${}".format(calculated_dollar_amount3))

    elif user_choice == "3":
      while True:
        print()
        print("What percent would you like to calculate?")
        percent = input("> ")
        if percent.isnumeric(): #not percent.isalnum():
          percent = float(percent)
          percentage = percent / 100
          percent_of_amount = float(calculated_dollar_amount) * percentage
          print()
          print("{}% of ${} is ${:.2f}.".format(percent, calculated_dollar_amount,percent_of_amount))
          break

        #BUG: If using letters but decimal in right place
        # elif ("." in percent[:-2] or percent[:-1]):
        #   percent = float(percent)
        #   percentage = percent / 100
        #   percent_of_amount = float(calculated_dollar_amount) * percentage
        #   print()
        #   print("{}% of ${} is ${:.2f}.".format(percent, calculated_dollar_amount,percent_of_amount))
        #   break
        elif "." in percent:
          count = 0
          for char in percent:
            if char in "1234567890.":
              count += 1

          dot_count = 0
          for char in percent:
            if char == ".":
              dot_count += 1

          if dot_count > 1:
            print("Invalid input. Try again.")

          if count == len(percent):
            percent = float(percent)
            percentage = percent / 100
            percent_of_amount = float(calculated_dollar_amount) * percentage
            print()
            print("{}% of ${} is ${:.2f}.".format(percent, calculated_dollar_amount,percent_of_amount))
            break

          else:
            print("Invalid input. Try again.")
        
        else:
          print("Invalid input. Try again.")


    elif user_choice == "4":
      print("Thanks for using this calculator. Goodbye!")
      break

    else:
      print("Invalid input. Please use numeric values.")
      print()


show_calculated_dollar_amount()

# Nice to Have
# [x] Loop when user input invalid hourly pay rate
# [X] Should not error when rate is not whole
# [X] Allow user to edit pay rate input
# [x] Loop when user input invalid time worked
  # [x] Improve how to ask user to input time worked
# [x] Allow user to edit time worked input
  # [ ] Allow user to edit time worked input by individual components
# [x] Build anticipation when calculating result
# [x] Add next step options
  # [x] Do another calculation
  # [x] Forecast multiple amounts
  # [x] Apply percentage
  # [x] Add goodbye message


# Citations
# .isnumeric() - https://www.w3schools.com/python/ref_string_isnumeric.asp
# {.2f} - https://runestone.academy/ns/books/published/thinkcspy/Strings/StringMethods.html?highlight=decimal%20point
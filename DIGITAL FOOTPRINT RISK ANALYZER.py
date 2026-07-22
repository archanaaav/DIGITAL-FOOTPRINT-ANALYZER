print("=" * 50)
print("     DIGITAL FOOTPRINT RISK ANALYZER")
print("=" * 50)
print("START ASSESSMENT")
def get_user_input():
        try:
          social_account=int(input("Enter number of social account:"))
          same_username=str(input("Is Same Username used everywhere:")).upper()
          public_instagram=str(input("Pubic instagram?:")).upper()
          public_facebook=str(input("Public Facebook?:")).upper()
          same_password=str(input("Is Same Password used everywhere:")).upper()
          two_factor=str(input("Uses Two Factor Authentication?:")).upper()
          email_breach=str(input("E-mail found in known data breaches?:")).upper()
          public_phonenumber=str(input("Same phone number publicly:")).upper()
          return(
            social_account,same_username,public_instagram,public_facebook,same_password,two_factor , email_breach,public_phonenumber
        )
        except ValueError:
            print("Enter only valid number of social median accounts")
user_data=get_user_input()
print(user_data)
def calculate_risk(user_data):
    social_account, same_username, public_instagram,public_facebook,\
        same_password, two_factor, email_breach, public_phonenumber=user_data
    risk_point=0
    if same_username == 'Y':
        risk_point += 15
    if public_instagram == 'Y':
        risk_point += 10
    if public_facebook == 'Y':
        risk_point += 10
    if same_password == 'Y':
        risk_point += 25
    if two_factor == 'N':
        risk_point += 20
    if email_breach == 'Y':
        risk_point += 30
    if public_phonenumber == 'Y':
        risk_point += 20
    return risk_point
risk=calculate_risk(user_data)
print(risk)
def show_result(risk):
    print("\n" + "=" * 45)
    print("      DIGITAL FOOTPRINT REPORT")
    print("=" * 45)
    print("Risk Score:",risk)
    if risk<=20:
      print("Risk Level: LOW")
    elif risk<=50:
      print("Risk Level: MEDIUM")
    else:
      print("Risk Level: HIGH")
risk=calculate_risk(user_data)
show_result(risk)
def show_recommendations(user_data):
    print("\n" + "-" * 45)
    print("Recommendations")
    print("-" * 45)
    social_account, same_username, public_instagram, public_facebook, \
        same_password, two_factor, email_breach, public_phonenumber = user_data
    risk_point = 0
    if same_username == 'Y':
        print("-Use DIfferent Passwords for evert account.")
    if public_instagram == 'Y':
        print("-Make Instagram Private.")
    if public_facebook == 'Y':
        print("~Make Facebook Private.~")
    if same_password == 'Y':
        print("-Use DIfferent Passwords for evert account-.")
    if two_factor == 'N':
        print("-Enable two fator Verification-.")
    if email_breach == 'Y':
        print("-Change your password Immediately.")
    if public_phonenumber == 'Y':
        print("-Hide your phone number from public view.")
show_recommendations(user_data)
if risk<= 20:
    grade = "A"
elif risk<= 40:
    grade = "B"
elif risk <= 60:
    grade = "C"
elif risk<= 80:
    grade = "D"
else:
    grade = "F"
print("\n" + "-" * 45)
print("PRIVACY ANALYSIS")
print("-" * 45)
print("Privacy Grade:", grade)

print("\n" + "-" * 45)
print("HACKER DIFFICULTY")
print("-" * 45)
if risk<= 20:
    print("Hacker Difficulty : HARD TARGET")
elif risk<= 50:
    print("Hacker Difficulty : MODERATE TARGET")
else:
    print("Hacker Difficulty : EASY TARGET")

print("\n" + "=" * 50)
print("Thank you for using")
print("DIGITAL FOOTPRINT RISK ANALYZER")
print("=" * 50)

# This is for the choice of the type of email you want to send

print("Please look at the list and select the you need: ")

print("1.) scheduled maintenance")
print("2.) scheduled maintenance - without a hostname")
print("3.) emergency maintenance")
print("4.) emergency maintenance - without a hostname")
print("5.) Host down")
print("6.) Interface down")
print("7.) Glass Account creation")
print("8.) Glass Account permissions change")

# This is for chosing which option you want if you pick 1 it will change it from a string and turn it into a integer number
choice = int(input("Please select the number you want to pick: "))

#If statement for what to do depending on what type of ticket it is

#scheduled maintenance
if choice == 1:
    print("We will need some information before we can make the email")
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'scheduled maintenance-{site}-{starttime}.txt', mode='x') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a scheduled maintenance for the site {site},"
                f"The host affected is {hostname}\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
# scheduled maintenance- without a hostname
elif choice == 2:
    print("We will need some information before we can make the email")
    site = input("Please enter site name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'scheduled maintenance- without a hostname-{site}-{starttime}.txt', mode='x') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a scheduled maintenance for the site {site},"
                f"\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for emergency maintenance
elif choice == 3:
    print("We will need some information before we can make the email")
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'emergency maintenance-{site}-{starttime}.txt', mode='x') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a emergency maintenance for the site {site},"
                f"The host affected is {hostname}\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for emergency maintenance without hostname
elif choice == 4:
    print("We will need some information before we can make the email")
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'emergency maintenance-{site}-{starttime}.txt', mode='x') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a emergency maintenance for the site {site},"
                f"\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for Host down
elif choice == 5:
    print("We will need some information before we can make the email")
    hostname = input("Please enter host name: ")

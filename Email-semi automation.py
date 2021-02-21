name =input("Please enter your name here: ")
# This is for the choice of the type of email you want to send

print("Please look at the list and select the you need: ")
#This will show the user options about what they can pick 
print("1.) scheduled maintenance")
print("2.) scheduled maintenance - without a hostname")
print("3.) emergency maintenance")
print("4.) emergency maintenance - without a hostname")
print("5.) Host down - Azure no access")
print("6.) Host down - VMware no access")
print("7.) Host down - Enhanced")
print("8.) Interface down")
print("9.) Glass Account creation")
print("10.) Glass Account permissions change")

# This is for chosing which option you want if you pick 1 it will change it from a string and turn it into a integer number
choice = int(input("Please select the number you want to pick: "))

#If statement for what to do depending on what type of ticket it is

#scheduled maintenance
if choice == 1:
    print("We will need some information before we can make the email")
    #This is ask's the users to enter 5 questions about the site 
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'scheduled-maintenance-{site}-{starttime}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a scheduled maintenance for the site {site},"
                f"The host affected is {hostname}\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}\n\n"
                f"Kind regards,\n"
                f"{name}")
# scheduled maintenance- without a hostname
elif choice == 2:
    print("We will need some information before we can make the email")
    #This is ask's the users to enter 5 questions about the site 
    site = input("Please enter site name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'scheduled maintenance- without a hostname-{site}-{starttime}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a scheduled maintenance for the site {site},"
                f"\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for emergency maintenance
elif choice == 3:
    print("We will need some information before we can make the email")
    #This is ask's the users to enter 5 questions about the site 
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'emergency maintenance-{site}-{starttime}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a emergency maintenance for the site {site},"
                f"The host affected is {hostname}\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for emergency maintenance without hostname
elif choice == 4:
    print("We will need some information before we can make the email")
    #This is ask's the users to enter 5 questions about the site 
    site = input("Please enter site name: ")
    hostname = input("Please enter host name: ")
    starttime = input("Please enter start time: ")
    endtime = input("Please enter End time: ")
    downtime = input("please enter The expected downtime: ")
    # This creates a file with the email layout filled in
    with open(f'emergency maintenance-{site}-{starttime}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\nThere is a emergency maintenance for the site {site},"
                f"\nThe maintenance will take place on the {starttime} until {endtime}, the expected downtime is {downtime}")
#This is for Host down
elif choice == 5:
    print("We will need some information before we can make the email")
    # Name of the VM is stored here
    vmname = input("Please enter host name: ")
    # This creates a file with the email layout filled in
    with open(f'Host-down-azureVM-{vmname}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\n\nWe have been receiving alerts for the azure VM {vmname} is currently showing as down.\n"
                f"We have seen that it has been deallocated, We was wondering if it this was intentional or not.\n\n"
                f"Kind regards,\n"
                f"{name}.")
#This is for Host down - VMware no access
elif choice == 6:
    print("We will need some information before we can make the email")
    # Name of the VM is stored here
    vmname = input("Please enter host name: ")
    # This creates a file with the email layout filled in
    with open(f'Host-down-VMware-{vmname}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\n\nWe have been receiving alerts for the VM named {vmname} is currently showing as down.\n"
                f"Going to add this content for this at a later date for steps for the customer.\n\n"
                f"Kind regards,\n"
                f"{name}.")
#This is for Host down - Enhanced
elif choice == 7:
    print("We will need some information before we can make the email")
    # Name of the VM is stored here
    vmname = input("Please enter host name: ")
    # This creates a file with the email layout filled in
    with open(f'Host down - Enhanced-{vmname}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\n\nWe have been receiving alerts for the VM named {vmname} is currently showing as down.\n"
                f"Going to add this content for this at a later date for steps for the customer.\n\n"
                f"Kind regards,\n"
                f"{name}.")
elif choice == 8:
    print("We will need some information before we can make the email")
    # Name of the VM is stored here
    interface = input("Please enter host name: ")
    # This creates a file with the email layout filled in
    with open(f'Interface down-{interface}.txt', mode='w') as f:
        f.write(f"Please email the customer with this!\n"
                f"Hello team,\n\nWe have been receiving alerts for an Interface named {interface} is currently showing as down.\n"
                f"Going to add this content for this at a later date for steps for the customer.\n\n"
                f"Kind regards,\n"
                f"{name}.")
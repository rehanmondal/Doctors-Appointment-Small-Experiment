
from datetime import datetime
now=datetime.now()

app_var = now.strftime("/%m/%y")

slot_dict=  {'11':'11:00 AM','12':'12:00 PM','13':'1:00 PM',
            '14':'2:00 PM','15':'3:00 PM','16':'4:00 PM','17':'5:00 PM','18':'6:00 PM','19':'7:00 PM','20':'8:00 PM'}

doc_dict=  {'orthopedic':'Dr.Syamal Bose','pediatric':'Dr.Nirmal Ghose','endocrinology':'Dr.Soumik Goswami',
            'cardiologist':'Dr. Aniruddha Mondal','medicine':'Dr. Nishat Mondal','eye':'Dr. Avijit Dey','ent':'Dr.Sabyasachi Bag'}
print("\n")
print("="*75)
print("\t\t\t\t\t\t\tDOCTORS LIST")
print("\t\t\t\tAvailable from 11:00 AM TO 8:30 PM")
print("="*75)

for key,values in doc_dict.items():
    print(key,values, sep="\t-\t ")

print("-"*75)
try:
    pat_name = input("\nEnter your name - ")
    pat_mob  = int(input("Enter your registered Mobile Number : "))
    app_date = int(input("Enter Date of this month : "))
    time_slot = int(input("Choose Time Slot Between 11 hours to 20 hours(8 PM) : "))

    if len(str(pat_mob)) == 10 and app_date<31:
        if (time_slot>=11) and (time_slot<=20):

            print("\t Looking for which Specialist Doctor - ")
            spec_doc_inp   =  input("Please Select here - ")
            spec_doc = spec_doc_inp.lower()

            check = doc_dict.get(spec_doc)
            print(doc_dict.get(spec_doc, "No Doctor Available for this specialization"))
            tim_slot_get_time = slot_dict.get(str(time_slot))

            if check:
                confirmation = input("Do You Want To Book Appointment with this Doctor Y|N : ")
                if confirmation.lower() == 'y':
                    print("Message popup !!! \n")
                    print("Dear ", pat_name,
                          f''',\nAs per your booking request, your appointment has been fixed on {tim_slot_get_time} on {app_date}{app_var} with {check} at Coders Health Point.\n Thank you\n team C.H.P\n''')
                    # print(doc_dict.get(spec_doc, "No Doctor Available for this specialization"))
                    print(now.strftime("%d-%m-%y\n%H:%M:%S"))
                elif confirmation.lower() == 'n':
                    print("Thanks for Visit us !!, Stay Safe")

                else:
                    print("No Valid Response , Try Again")
        else:
            print("This time Slot Not Available")
    else:
        print("Mobile Number Should be 10 digit and date must be between 1 to 31")

except:
    print("Invalid Name,Date or mobile")

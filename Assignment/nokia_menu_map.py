def display_main_menu():
    print ("""
MENU
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10.Reminders
11.Clock
12.Profiles
13.SIM services
14.Exit
""")
           
def display_submenu(submenu):
    print(submenu)
        
display_main_menu()

menu_number = int(input('Select menu number: '))

while (True):
    match menu_number:
        case 1:
            case_one_menu = ("""
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10.Voice tags
99. Go back
""")
            display_submenu(case_one_menu)
            
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
SEARCH
0. Go back        
""")

            if (select_option == 2):
                print("""
SERVICE NOS.
0. Go back       
""")

            if (select_option == 3):
                print("""
ADD NAME
0. Go back       
""")

            if (select_option == 4):
                print("""
ERASE
0. Go back       
""")

            if (select_option == 5):
                print("""
EDIT
0. Go back       
""")

            if (select_option == 6):
                print("""
ASSIGN TONE
0. Go back       
""")

            if (select_option == 7):
                print("""
SEND B'CARD
0. Go back       
""")

            if (select_option == 8):
                phonebook_options = """
OPTIONS
1. Type of view
2. Memory status
0. Go back       
"""

                display_submenu(phonebook_options)

                select_suboption = int(input('Select option: '))
                if (select_suboption == 1):
                    print("""
TYPE OF VIEW
 0. Go back
""")
            
                if (select_suboption == 2):
                    print("""
MEMORY STATUS
 0. Go back
""")

                select_third_option = int(input('Select option: '))
                if (select_third_option == 0):
                    display_submenu(phonebook_options)
            
            if (select_option == 9):
                print("""
SPEED DIALS
0. Go back       
""")  

            if (select_option == 10):
                print("""
VOICE TAGS
0. Go back       
""")      
        
            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_one_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
        
        
        case 2:
            case_two_menu = ("""
MESSAGES
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10.Service command editor
99. Go back           
""")

            display_submenu(case_two_menu)
    
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
WRITE MESSAGES
0. Go back        
""")

            if (select_option == 2):
                print("""
INBOX
0. Go back       
""")

            if (select_option == 3):
                print("""
OUTBOX
0. Go back       
""")

            if (select_option == 4):
                print("""
PICTURE MESSAGES
0. Go back       
""")

            if (select_option == 5):
                print("""
TEMPLATES
0. Go back       
""")

            if (select_option == 6):
                print("""
SMILEYS
0. Go back       
""")
    
            if (select_option == 7):
                message_settings = """
MESSAGE SETTINGS
1. Set 1
2. Common
0. Go back       
"""

                display_submenu(message_settings)

                select_suboption = int(input('Select option: '))
                if (select_suboption == 1):
                    set_1 = """
SET 1
1. Message centre number
2. Message sent as
3. Message validity
0. Go back
"""
                    display_submenu(set_1)
            
                    select_third_option = int(input('Select option: '))
                    if (select_third_option == 1):
                        print("""
MESSAGE CENTRE NUMBER
0. Go back                
""")

                    if (select_third_option == 2):
                        print("""
MESSAGE SENT AS
0. Go back                
""")

                    if (select_third_option == 3):
                        print("""
MESSAGE VALIDITY
0. Go back                
""")

                    if (select_third_option == 0):
                        display_submenu(set_1)

                
                if (select_suboption == 2):
                    common = """
1. Delivery reports
2. Reply via same centre
3. Character support
0. Go back
"""

                    display_submenu(common)
            
                    select_third_option = int(input('Select option: '))
                    if (select_third_option == 1):
                        print("""
DELIVERY REPORTS
0. Go back                
""")

                    if (select_third_option == 2):
                        print("""
REPLY VIA SAME CENTRE
0. Go back                
""")

                    if (select_third_option == 3):
                        print("""
CHARACTER SUPPORT
0. Go back                
""")

                    if (select_third_option == 0):
                        display_submenu(common)


                select_suboption = int(input('Select option: '))
                if (select_suboption == 0):
                    display_submenu(case_two_menu)
                    
            if (select_option == 8):
                print("""
INFO SERVICE
0. Go back        
""")

            if (select_option == 9):
                print("""
VOICE MAILBOX NUMBER
0. Go back       
""")

            if (select_option == 10):
                print("""
SERVICE COMMAND EDITOR
0. Go back       
""")

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_two_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                
        case 3:
            case_three_menu = ("""
CHAT
0. Go back           
""")

            display_submenu(case_three_menu)
            select_option = int(input('Select option: '))
            
            if (select_option == 0):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                
        case 4:
            case_four_menu = ("""
CALL REGISTER
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent calls
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
99. Go back            
""")

            display_submenu(case_four_menu)
            
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
MISSED CALLS
0. Go back                
""")

            if (select_option == 2):
                print("""
RECEIVED CALLS
0. Go back                
""")

            if (select_option == 3):
                print("""
DIALLED NUMBERS
0. Go back                
""")

            if (select_option == 4):
                print("""
ERASE RECENT CALLS
0. Go back                
""")

            if (select_option == 5):
                show_call_duration = """
SHOW CALL DURATION
1. Last call duration
2. All calls\' duration
3. Received calls\' duration
4. Dialled calls\' duration
5. Clear timers
0. Go back              
"""

                display_submenu(show_call_duration)
            
                select_third_option = int(input('Select option: '))
                if (select_third_option == 1):
                    print("""
LAST CALL DURATION
0. Go back                
""")

                if (select_third_option == 2):
                    print("""
ALL CALLS\' DURATION
0. Go back                
""")

                if (select_third_option == 3):
                    print("""
RECEIVED CALLS\' DURATION
0. Go back                
""")

                if (select_third_option == 4):
                    print("""
DIALLED CALLS\' DURATION
0. Go back                
""")

                if (select_third_option == 5):
                    print("""
CALL TIMERS
0. Go back                
""")

                if (select_third_option == 0):
                    display_submenu(show_call_duration)
                        
            if (select_option == 6):
                show_call_cost = """
SHOW CALL COST
1. Last call cost
2. All calls\' cost
3. Clear counters
0. Go back             
"""

                display_submenu(show_call_cost)
            
                select_third_option = int(input('Select option: '))
                if (select_third_option == 1):
                    print("""
LAST CALL COST
0. Go back                
""")

                if (select_third_option == 2):
                    print("""
ALL CALLS\' COST
0. Go back                
""")

                if (select_third_option == 3):
                    print("""
CLEAR COUNTERS
0. Go back                
""")

                if (select_third_option == 0):
                    display_submenu(show_call_cost)
                        
            if (select_option == 7):
                call_cost_settings = """
CALL COST SETTINGS
1. Call cost limit
2. Show costs in
0. Go back             
"""

                display_submenu(call_cost_settings)
            
                select_third_option = int(input('Select option: '))
                if (select_third_option == 1):
                    print("""
CALL COST LIMIT
0. Go back                
""")

                if (select_third_option == 2):
                    print("""
SHOW COSTS IN
0. Go back                
""")

                if (select_third_option == 3):
                    print("""
CLEAR COUNTERS
0. Go back                
""")

                if (select_third_option == 0):
                    display_submenu(call_cost_settings)
                        
            if (select_option == 8):
                print("""
PREPAID CREDIT
0. Go back             
""")          
                        
            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_four_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                
                
        case 5:
            case_five_menu = ("""
TONES
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
99.Go back           
""")

            display_submenu(case_five_menu)
            
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
RINGING TONE
0. Go back                
""")

            if (select_option == 2):
                print("""
RINGING VOLUME
0. Go back                
""")

            if (select_option == 3):
                print("""
INCOMING CALL ALERT
0. DIALLED NUMBERS                
""")

            if (select_option == 4):
                print("""
COMPOSER
0. Go back                
""")

            if (select_option == 5):
                print("""
MESSAGE ALERT TONE
0. Go back                
""")

            if (select_option == 6):
                print("""
KEYPAD TONES
0. Go back                
""")

            if (select_option == 7):
                print("""
WARNING AND GAME TONES
0. Go back                
""")

            if (select_option == 8):
                print("""
VIBRATING ALERT
0. Go back                
""")

            if (select_option == 9):
                print("""
SCREEN SAVER
0. Go back                
""")

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_five_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                

        case 6:
            case_six_menu = ("""
SETTINGS
1. Call settings
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
99.Go back            
""")

            display_submenu(case_six_menu)
            
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
CALL SETTINGS
0. Go back                
""")

            if (select_option == 2):
                print("""
SPEED DIALLING
0. Go back                
""")

            if (select_option == 3):
                print("""
CALL WAITING OPTIONS
0. Go back               
""")

            if (select_option == 4):
                print("""
OWN NUMBER SENDING
0. Go back                
""")

            if (select_option == 5):
                print("""
PHONE LINE IN USE
0. Go back                
""")

            if (select_option == 6):
                print("""
AUTOMATIC ANSWER
0. Go back                
""")

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_six_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                      
                
                
        case 7:
            case_seven_menu = ("""
CALL DIVERT
0. Go back            
""")

            display_submenu(case_seven_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_seven_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))   


                                      
        case 8:
            case_eight_menu = ("""
GAMES
0. Go back            
""")

            display_submenu(case_eight_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_eight_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                
                

        case 9:
            case_nine_menu = ("""
CALCULATOR
0. Go back            
""")

            display_submenu(case_nine_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_nine_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
                
                

        case 10:
            case_ten_menu = ("""
REMINDERS
0. Go back            
""")

            display_submenu(case_ten_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_ten_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))  



        case 11:
            case_eleven_menu = ("""
CLOCK
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
99. Go back          
""")

            display_submenu(case_eleven_menu)
            
            select_option = int(input('Select option: '))
            if (select_option == 1):
                print("""
ALARM CLOCK
0. Go back                
""")

            if (select_option == 2):
                print("""
CLOCK SETTINGS
0. Go back                
""")

            if (select_option == 3):
                print("""
DATE SETTINGS
0. Go back                
""")

            if (select_option == 4):
                print("""
STOPWATCH
0. Go back                
""")

            if (select_option == 5):
                print("""
COUNTDOWN TIMER
0. Go back                
""")

            if (select_option == 6):
                print("""
AUTO UPDATE OF DATE AND TIME
0. Go back                
""")

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_eleven_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: ')) 


        case 12:
            case_twelve_menu = ("""
PROFILES
0. Go back            
""")

            display_submenu(case_twelve_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_twelve_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))    


        case 13:
            case_thirteen_menu = ("""
SIM SERVICES
0. Go back            
""")

            display_submenu(case_thirteen_menu)

            select_suboption = int(input('Select option: '))
            if (select_suboption == 0):
                display_submenu(case_thirteen_menu)
                
            select_option = int(input('Select option: '))
            
            if (select_option == 99):
                display_main_menu()
                menu_number = int(input('Select menu number: '))
                
        case 14:
            break
            

                
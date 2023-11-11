import sys
import time

lst=['Which is the part of the computer system that one can physically touch?',
     'A ………. is an electronic device that process data, converting it into information.',
     'IC chips used in computers are usually made of',
     'Which of the following is not an example of an Operating System?',
     'One Gigabyte is approximately equal is:']
option1=['data','computer','lead','windows 98','1000,000 bytes']
option2=['operating system','processor','silicon','BSD Unix','1000,000,000bytes']
option3=['hardware','case','chromium','Microsoft Office XP','1000,000,000,000bytes']
option4=['software','stylus','gold',' Red Hat Linux','none of these']
answers=[3,1,2,3,2]
answers_entered=[]
namelist=[]
playertime=[]
def show_all():                                    #to DISPLAY ALL THE QUESTIONS
    print(
        '\n\t\t\t\t\t\t\t\t\t\t===========================\n\t\t\t\t\t\t\t\t\t\t  THE QUESTIONS ARE BELOW\n\t\t\t\t\t\t\t\t\t\t===========================')
    length=len(lst)
    for i in range(0,length):
        print(' '*45,"ques", i + 1, ":", lst[i])
        print(' ' * 55, 'option1:', option1[i])
        print(' ' * 55, 'option2:', option2[i])
        print(' ' * 55, 'option3:', option3[i])
        print(' ' * 55, 'option4:', option4[i])
def score_arrange():
    for i in range(0,len(namelist)):
        k=len(namelist[i])+14
        print('\n\n\n'+' '* 70, "******scoreboard of",namelist[i],"******")
        print(' '* 76,"-"* k)
        print(' '*55,'Score Secured by',namelist[i],'is',answers_entered[i])
def scoreboard():
        p=23+len(namelist[-1])
        m=answers_entered[-1]
        print('\n\n\n\n'+' '* 60, "SCOREBOARD OF THE USER",namelist[-1])
        print(' '*60,"-"*p)
        if m<=2:
            print(' ' * 55," Try again improve your score!!!")
        elif m<=5:
            print(' ' * 55, "Well good! improve your score")
        else:
            print(" " * 55,'Excellent')
        print(' '* 65 ,"Score is",m)
        print(' '* 65 ,"TIME TAKEN BY THE USER IS",playertime[-1])
def play(r=10):
    print('\n\n\t\t\t\t\t\t\t==============================================\n',' '*55,"**************!!ATTENTION!!****************\n")
    print('\n\n'+' '*55,'''INSTRUCTIONS;
                                                             -KINDLY attempt All The Questions
                                                             -Each Question Carries 1 mark
                                                             -Play it very fast Timmings Will be Calculated.once time exceeds
                                                             10 seconds, the remaining questions are not displayed.
                                                             -Choose the correct option number
                                                             -Be attentive''')
    print('\n',' '*75,"******LET's START THE QUIZ******")
    print(' '*82,'--'*10 )
    name=input(' '* 55+"Enter The Player name -")
    s=name.capitalize()
    namelist.append(s)
    print(' '*85, "******START******")
    start=time.time()
    l=0
    t=0
    f=0
    while t<r and l<len(lst):
                 print(' ' * 45, "ques", l + 1, ":", lst[l])
                 print(' ' * 55, 'option1:', option1[l])
                 print(' ' * 55, 'option2:', option2[l])
                 print(' ' * 55, 'option3:', option3[l])
                 print(' ' * 55, 'option4:', option4[l])
                 q = None

                 while True:
                         try:
                           q = int(input(' ' * 75 + 'ENTER YOUR option no: '))
                           break
                         except ValueError:
                                       print(
                        '''\n\t\t\t\t\t\t\t\t\t\t======================\n\t\t\t\t\t\t\t\t\t  *****!NUMBERS ONLY EXPECTED!*****
\t\t\t\t\t\t\t\t\t\t======================''')
                 end=time.time()
                 t=end-start
                 if q==answers[l]:
                     f=f+1
                 l=l+1
    answers_entered.append(f)
    playertime.append(t)
    print('\t\t\t\t\t\t\t\t\t==============================================\n',' '*75,"**************TIME UP****************\n")    
    print(
        '\n\t\t\t\t\t\t\t\t\t\t============================\n\t\t\t\t\t\t\t\t\t\t!YOUR RESOPONSE IS RECORDED!\n\t\t\t\t\t\t\t\t\t\t============================')
def delete_ques():
    a = int(input(' '*40+'Enter The Serial No Of The Question To Be DELETED : '))
    while a > len(lst):
        print('\t\t\t\t\t\t\t---Number Is In Out Of Range---')
        a = int(input(' '*40+'Enter the serial no of the Question to be DELETED : '))
    if 0<a<=len(lst):
        lst.remove(lst[a-1])
        option1.remove(option1[a-1])
        option2.remove(option2[a-1])
        option3.remove(option3[a-1])
        option4.remove(option4[a-1])
    print(
        '\n\t\t\t\t\t\t\t\t\t\t======================\n\t\t\t\t\t\t\t\t\t\t       DELETED!!\n\t\t\t\t\t\t\t\t\t\t======================')
def options():
    option1.append(input('\n'+' '* 75+'-option1: '))
    option2.append(input(' '* 75+"-option2: "))
    option3.append(input(' '* 75+"-option3: "))
    option4.append(input(' '* 75+"-option4: "))
def insert_many_ques():                                     #To Add new Questions to make the quiz interesting
    n=int(input(' '*50+"-Enter The Number Of Questions To Be Added : "))
    for i in range(n):
        lst.append(input(' '* 55+"Enter the Question to be Added : "))
        options()
        g=int(input("\n"+' '* 75+'Enter the Correct Answers option number'))
        answers.append(g)
    print('\n\t\t\t\t\t\t\t\t\t\t======================\n\t\t\t\t\t\t\t\t\t\tYOUR RESPONSE RECORDED\n\t\t\t\t\t\t\t\t\t\t======================')
def admin():                                         #admin section
    while True: 
        print('\n\n\n\n', '=' * 167, sep='')
        print(' ' * 85, 'ADMIN SECTION')
        print(' ' * 85, '=============\n')
        print(' ' * 75, 'ENTER 1 - TO ADD QUESTION')
        print(' ' * 75, 'ENTER 2 - TO SHOW ALL QUESTION')
        print(' ' * 75, 'ENTER 3 - TO DELETE QUESTION')
        print(' ' * 75, 'ENTER 4 - TO RETURN TO HOME MENU')

        ch = None

        while True:
            try:
                ch = int(input(' ' * 75 + 'ENTER YOUR CHOICE: '))
                break
            except ValueError:
                print(
                    '\n\t\t\t\t\t\t\t\t\t\t======================\n\t\t\t\t\t\t\t\t\t\t!NUMBERS ONLY EXPECTED!\n\t\t\t\t\t\t\t\t\t\t======================')

        if ch == None:
            pass
        elif ch == 1:
            insert_many_ques()                            #function call

        elif ch == 2:
            show_all()
        elif ch == 3:
            delete_ques()
        
        elif ch == 4:
            print('=' * 167)
            print('\n' + ' ' * 75 + 'RETURNING TO HOME MENU.....\n')

            return
        else:
            print('\n\t\t\t\t\t\t\t\t\t\t\t!NUMBER OUT OF RANGE!')
while True:

    print('\n\n' + '=' * 167)
    print(' ' * 85 + "MAIN MENU" + "\n" + " " * 85 + "=========\n")
    print(' ' * 75, 'ENTER 1 -  ADMIN SECTION')
    print(' ' * 75, 'ENTER 2 -  PLAY SECTION')
    print(' ' * 75, 'ENTER 3 -  VIEW SCOREBOARD')
    print(' ' * 75, 'ENTER 4 -  VIEW SCOREBOARD OF ALL THE USER')
    print(' ' * 75, 'ENTER 5 -  GIVE REMARKS ABOUT AS')
    print(' ' * 75, 'ENTER 6 -  EXIT THE SOFTWARE')
    # print(' '*75,'ENTER YOUR CHOICE: ',end='')
    ch = None
    while True:
        try:
            ch = int(input(' ' * 75 + 'ENTER YOUR CHOICE: '))
            print('=' * 167)
            break
        except ValueError:
            print('\n', ' ' * 75, '!NUMBERS ONLY EXCEPTED!\n\n')

    if ch == None:
        continue
    elif ch == 1:
        print('\n'," "*70,"=======CONFIRM THE ADMIN=======")
        password=input(' '*60+"ENTER THE Admin Password :")
        if password=="12345":
            print('\n' + ' ' * 75 + 'REDIRECTING TO ADMIN SECTION...')
            admin()
        else:
            print(' '*70,"***********+++INCORRECT PASSWORD+++***********")
    elif ch == 2:
        play()
    elif ch == 3:
        try:
           scoreboard()
           continue
        except IndexError:
            print('\n'," "*70,"=======PLAY THE GAME FIRST=======")

    elif ch == 4:
        score_arrange()
    elif ch == 5:
        print('\n' + ' ' * 75 + 'REDIRECTING TO REMARK PAGE...')
        print('\n\n'+' ' * 75 ,"ENTER THE REMARKS ABOUT US")
        input("\n"+" "*70+"ADVANTAGE ")
        input(" "*70+"DISADVANTAGE ")
        
    elif ch == 6:
        print()
        print('\n\n\n\n\n'+'=' * 167)
        print('\n' + ' ' * 65 + '*****THANK YOU FOR USING THIS SOFTWARE*****')
        print('=' * 167)

        sys.exit()
    else:
        print(' ' * 75 + '!CHOICE OUT OF RANGE!')
else:
    print(
        '\n\n\n\n==================================PLEASE VISIT HERE AGAIN!==========================================')
    input()


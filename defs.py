

def welcome():
    print("==========welcome to folder cloner==========")
    print("\t*type help for the help\n\t*type read for the read folder names\n\t*type write for the clone the directories\n\t*type exit to exit")
    print("===========TeamHiru==========")
    user_ans =input("\twhat you want to do:")
    while True:
        if user_ans != None:
            if user_ans.lower() == 'help':
                print("run help function here")
            elif user_ans.lower() == 'read':
                print("read functions here")
            elif user_ans.lower() == 'write':
                print("write function here") 
            elif user_ans.lower() == 'exit':
                print("have a good day")
                break
            else:
                print("something wrong with your command")
                
        else:
            print("please enter command")
        user_ans =input("\twhat you want to do:")

welcome()
# TO-DO List

Tasks = []

def add_task():
    subject = input('Enter subject:')
    hour = input('Enter hour:')
    date = input('Enter date:')
    done = False
    task = {
        'subject':subject,
        'hour':hour,
        'date':date,
        'done':done
    }
    Tasks.append(task)
    print('Task added !')

def remove_task():
    subject = input('Enter subject:')
    for i in Tasks:
        if i['subject'] == subject:
            Tasks.remove(i)
            print(f'{i['subject']} removed !')

def toggle_task():
    subject = input('Enter subject:')
    for i in Tasks:
        if i['subject'] == subject:
            if i['done'] == False:
                i['done'] = True
                print('changed')
            else:
                print('Your task is true ! ')

def show_tasks():
    for i , task in enumerate(Tasks , start=1):
        print(i , task)


while True:
    choice = input('''Choose one :
    [0] Add
    [1] Remove
    [2] Toggle
    [3] Show 
    >>> ''')

    if choice == '0':
        add_task()
    elif choice == '1':
        remove_task()
    elif choice == '2':
        toggle_task()
    elif choice == '3':
        show_tasks()
    else:
        continue
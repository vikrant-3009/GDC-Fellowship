import os
import sys


def need_help():
    help_menu = \
"""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(help_menu.encode('utf8'))


def add_task(s):
    # print(s)
    priority = s[0]
    if int(float(priority)) < 0:
        sys.stdout.buffer.write('Priority should be grater than or equal to 0.'.encode('utf8'))
        return
    task = s[1]
    # print(str(priority) + " " + str(task))
    if os.path.isfile("task.txt"):
        with open("task.txt", 'r') as t1:
            lines = t1.readlines()
            lines = [line.rstrip() for line in lines]
            print(lines)
            flag = 0
            for i in range(len(lines)):
                if int(float(lines[i][0])) <= int(float(priority)):
                    continue
                else:
                    lines.insert(i, str(priority) + " " + str(task))
                    flag = 1
            if flag == 0:
                lines.append(str(priority) + " " + str(task))
        with open("task.txt", 'w') as t2:
            for i in lines:
                t2.write(i + "\n")
    else:
        with open("task.txt", 'w') as t2:
            t2.write(str(priority) + " " + str(task) + "\n")

    sys.stdout.buffer.write('Added task: "{}" with priority {}'.format(task, priority).encode('utf8'))


def del_task(num):
    num = int(float(num)) - 1
    if os.path.isfile("task.txt"):
        flag = 0
        with open("task.txt", 'r') as t1:
            lines = t1.readlines()
            lines = [line.rstrip() for line in lines]
            if num >= 0 and num < len(lines):
                lines.pop(num)
                # print(lines)
                flag = 1
        if flag == 1:
            with open("task.txt", 'w') as t2:
                for i in lines:
                    t2.write(i + "\n")
            sys.stdout.buffer.write('Deleted item with index {}'.format(num + 1).encode('utf8'))
        else:
            sys.stdout.buffer.write('Error: item with index {} does not exist. Nothing deleted.'.format(num + 1).encode('utf8'))
    else:
        sys.stdout.buffer.write('Error: item with index {} does not exist. Nothing deleted.'.format(num + 1).encode('utf8'))


def list_tasks():
    if os.path.isfile("task.txt"):
        with open("task.txt", 'r') as t1:
            lines = t1.readlines()
            lines = [line.rstrip() for line in lines]
            for i in range(len(lines)):
                l = lines[i].split(" ", 1)
                # print(l)
                sys.stdout.buffer.write('{}. {} [{}] \n'.format(i+1, l[1], l[0]).encode('utf8'))
    else:
        sys.stdout.buffer.write('There are no pending tasks!'.encode('utf8'))


def mark_task_done(num):
    num = int(float(num)) - 1
    if os.path.isfile("task.txt"):
        flag = 0
        with open("task.txt", 'r') as t1:
            lines = t1.readlines()
            lines = [line.rstrip() for line in lines]
            if num >= 0 and num < len(lines):
                task1 = lines.pop(num)
                task1 = task1.split(" ", 1)
                # print(lines)
                flag = 1
        if flag == 1:
            with open("task.txt", 'w') as t2:
                for i in lines:
                    t2.write(i + "\n")
            with open("completed.txt", 'a') as t3:
                t3.write(task1[1] + "\n")
            sys.stdout.buffer.write('Marked item as done.'.encode('utf8'))
        else:
            sys.stdout.buffer.write('Error: no incomplete item with index {} exists.'.format(num + 1).encode('utf8'))
    else:
        sys.stdout.buffer.write('Error: no incomplete item with index {} exists.'.format(num + 1).encode('utf8'))


def generate_report():
    incomplete = 0
    complete = 0
    if os.path.isfile("task.txt"):
        with open("task.txt", 'r') as t1:
            lines = t1.readlines()
            lines = [line.rstrip() for line in lines]
            incomplete = len(lines)
            sys.stdout.buffer.write('Pending: {} \n'.format(incomplete).encode('utf8'))
            for i in range(len(lines)):
                l = lines[i].split(" ", 1)
                # print(l)
                sys.stdout.buffer.write('{}. {} [{}] \n'.format(i+1, l[1], l[0]).encode('utf8'))
    else:
        sys.stdout.buffer.write('Pending: 0 \n'.encode('utf8'))

    if os.path.isfile("completed.txt"):
        with open("completed.txt", 'r') as t3:
            lines = t3.readlines()
            lines = [line.rstrip() for line in lines]
            complete = len(lines)
            sys.stdout.buffer.write('\nCompleted: {} \n'.format(complete).encode('utf8'))
            for i in range(len(lines)):
                # l = lines[i].split(" ", 1)
                # print(l)
                sys.stdout.buffer.write('{}. {} \n'.format(i+1, lines[i]).encode('utf8'))
    else:
        sys.stdout.buffer.write('Completed: 0 \n'.encode('utf8'))


def main():
    # print(len(sys.argv))
    if (len(sys.argv) == 1):
        need_help()
    
    elif sys.argv[1] == "help":
        need_help()
    
    elif sys.argv[1] == "add":
        add_task(sys.argv[2:])

    elif sys.argv[1] == "del":
        del_task(sys.argv[2])

    elif sys.argv[1] == "done":
        mark_task_done(sys.argv[2])

    elif sys.argv[1] == "report":
        generate_report()

    elif sys.argv[1] == "ls":
        list_tasks()

    else:
        sys.stdout.buffer.write('No such option available! Type "./task help" for info about the tasks!'.encode('utf8'))

if __name__ == "__main__":
    main()
# Enter your code here. Read input from STDIN. Print output to STDOUT'
import sys

def get_answer(tasks):
    max_range = max(tasks.keys())
    running_total = 0
    maxm = 0
    for i in range(1, max_range+1):
        if i in tasks:
            running_total += tasks[i]
        maxm = max(maxm, running_total-i)
    return maxm

def print_tasks(tasks):
    print " TASKS: "
    for key in tasks.keys():
        print key, tasks[key]

num_lines = int(sys.stdin.readline())
tasks = {}

for _ in range(num_lines):
    inp = sys.stdin.readline()
    nums = inp.split(" ")
    deadline = int(nums[0])
    time_to_complete = int(nums[1])
    if deadline in tasks:
        tasks[deadline] += time_to_complete
    else:
        tasks[deadline] = time_to_complete
    print get_answer(tasks)
    

print ("*************************** Priority Scheduling ************************")
total_num_of_processes=int(input('Plx enter total no. of processes:'))
processes_list=[]
for index_of_processes_list in range(total_num_of_processes):
    processes_list.append([])
    processes_list[index_of_processes_list].append(input('Enter the process name:'))
    processes_list[index_of_processes_list].append(int(input('Enter the process arrival time:')))
    processes_list[index_of_processes_list].append(int(input('Enter the process burst time:')))
    processes_list[index_of_processes_list].append(int(input('Enter the priority of the process:')))

processes_list.sort(key=lambda process_list:process_list[3])

arrival_time_list = []
for index_of_arrival_time_list in range(total_num_of_processes):
    arrival_time_list.append([])
    arrival_time_list[index_of_arrival_time_list]=processes_list[index_of_arrival_time_list][1]

burst_time_list=[]
for index_of_burst_time_list in range(total_num_of_processes):
    burst_time_list.append([])
    burst_time_list[index_of_burst_time_list]=processes_list[index_of_burst_time_list][2]

priorities_list = []
for index_of_priorities_list in range(total_num_of_processes):
    priorities_list.append([])
    priorities_list[index_of_priorities_list] = processes_list[index_of_priorities_list][3]

def print_processes_with_arrival_time():
    print ('Processes you enter with arrival and burst_time are:')
    for index in range(total_num_of_processes):
        print (arrival_time_list[index],burst_time_list[index],priorities_list[index])



def print_priorities_after_sorting():
    print("Priorities of processes after Sorting is:")
    for index in range(total_num_of_processes):
        print(priorities_list[index])


status=arrival_time_list[0]
start_time_list=[]
for index in range(total_num_of_processes):
    start_time_list.append([])
    start_time_list[index] = status
    status = start_time_list[index] + burst_time_list[index]

def print_waiting_time():
    print('The waiting Time for the processes according to Sorted Priorities is:')
    for index in range(total_num_of_processes):
        print ((start_time_list[index])-(arrival_time_list[index]))

def get_total_waiting_time():
    total_waiting_time=0
    for index in range(total_num_of_processes):
	    total_waiting_time+=start_time_list[index]-arrival_time_list[index]
    return total_waiting_time

def print_average_waitig_time(total_waiting_time):
    print(' ')
    print('And avrg. waiting time is:', total_waiting_time / total_num_of_processes)

print_processes_with_arrival_time()
print_priorities_after_sorting()
print_waiting_time()
total_waiting_time=get_total_waiting_time()
print_average_waitig_time(total_waiting_time)
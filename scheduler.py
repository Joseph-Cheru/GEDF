
N = int(input("Enter the number of vehicles: "))
M = int(input("Enter the number of Edges: "))

#Dictionary for storing the tasks with their respective deadlines

task_deadline = {}
for i in range(N):
	task_deadline[i+1] = (int(input("Enter the deadline for task: ")))
print(task_deadline)

#PQ = [(0,0)]*N
PQ = [0]*N
# for i in range(N)
# 	PQ.append((i+1,task_deadline[i]))

size = -1

print(PQ)

def parent(i) : 
	return (i - 1) // 2

def leftChild(i) : 
	return ((2 * i) + 1)

def rightChild(i) :

	return ((2 * i) + 2)

def shiftUp(i) : 
	while (i > 0 and task_deadline[PQ[parent(i)]] > task_deadline[PQ[i]]) :
		swap(parent(i), i)
		i = parent(i)

def shiftDown(i) : 
	MinIndex = i

	l = leftChild(i)

	if (l <= size and task_deadline[PQ[l]] < task_deadline[PQ[MinIndex]]) :
	
		MinIndex = l
	

	r = rightChild(i)
	
	if (r <= size and task_deadline[PQ[r]] < task_deadline[PQ[MinIndex]]) : 
	
		MinIndex = r
	

	if (i != MinIndex) :
	
		swap(i, MinIndex)
		shiftDown(MinIndex)

def insert(p) : 
	
	global size
	size = size + 1
	PQ[size] = p

	shiftUp(size)

def extractMin() :
	
	global size
	result = PQ[0] 
	PQ[0] = PQ[size] 
	size = size - 1

	shiftDown(0)
	return result

def changePriority(i,p) :

	oldp_value = task_deadline[PQ[i]]
	task_deadline[PQ[i]] = p
	if (p > oldp_value) :
		shiftUp(i) 

	else :
		shiftDown(i)

def getMin() :
	return PQ[0]

def Remove(i) :

	task_deadline[PQ[i]] = 0

	shiftUp(i)
	extractMin()

def swap(i, j) : 
	
	temp = PQ[i]
	PQ[i] = PQ[j] 
	PQ[j] = temp

for i in range(N):
	insert(i+1)

def printpq():
	k = 0
	while (k <= size) :
		print(PQ[k], end = " ") 
		k += 1
	print()

print(PQ)
	
extractMin()
printpq()
Remove(3)
printpq()
Remove(4)
printpq()
print(task_deadline)

time_slot = 100

# Final_data = {"l_cov": l_cov,
# 	"v2e_trvtime": v2e_trvtime,
# 	#"t_p": t_p,
# 	"exec_time": exec_time,
# 	"vel_at_edge": vel_at_edge,
# 	"serv_send_data": serv_send_data,
# 	"serv_recv_data": serv_recv_data,
# 	"bandwidth": bandwidth,
# 	"density_jam": density_jam,
# 	"density": density,
# 	"M":M,
# 	"N":N}

for k in range(10):
	loc_vehicle_i_k = []
	for i in range(N):
		for j in range(M):
			if (v2e_trvtime[i][j]/100 == k and v2e_trvtime[i][j] > 0):
				loc_vehicle_i_k = j+1
			else:
				loc_vehicle_i_k = 0

				print("Task ",i+1," is assigned to Edge ",j+1)
				time_slot = time_slot - v2e_trvtime[i][j]
				break

	

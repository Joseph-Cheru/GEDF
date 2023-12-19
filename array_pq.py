import sys
import json

# Structure for the elements in the
# priority queue
class item :
	value = 0
	priority = 0
class GFG :

	# Store the element of a priority queue
	pr = [None] * (1000)
	
	# Pointer to the last index
	size = -1
	
	# Function to insert a new element
	# into priority queue
	@staticmethod
	def enqueue( value, priority) :
	
		# Increase the size
		GFG.size += 1
		
		# Insert the element
		GFG.pr[GFG.size] = item()
		GFG.pr[GFG.size].value = value
		GFG.pr[GFG.size].priority = priority
		
	# Function to check the top element
	@staticmethod
	def peek() :
		highestPriority = sys.maxsize
		ind = -1
		
		# Check for the element with
		# highest priority
		i = 0
		while (i <= GFG.size) :
		
			if (highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value > GFG.pr[i].value) :
				highestPriority = GFG.pr[i].priority
				ind = i
			elif(highestPriority > GFG.pr[i].priority) :
				highestPriority = GFG.pr[i].priority
				ind = i
			i += 1
			
		# Return position of the element
		return ind
	
	# Function to remove the element with
	# the highest priority
	@staticmethod
	def dequeue() :
	
		# Find the position of the element
		# with highest priority
		ind = GFG.peek()
		
		# Shift the element one index before
		# from the position of the element
		# with highest priority is found
		i = ind
		while (i < GFG.size) :
			GFG.pr[i] = GFG.pr[i + 1]
			i += 1
			
		# Decrease the size of the
		# priority queue by one
		GFG.size -= 1
	def printpq():
		for i in range(GFG.size+1):
			print("Vehicle ",GFG.pr[i].value," with deadline",GFG.pr[i].priority,"\n")
	@staticmethod
	def main( args) :
		 
		with open('FinalData_M40_N200.json', 'r') as json_file:
			json_load = json.load(json_file)

		N = json_load["N"]
		M = json_load["M"]
		l_cov = json_load["l_cov"]
		v2e_trvtime = json_load["v2e_trvtime"]
		exec_time = json_load["exec_time"]
		vel_at_edge = json_load["vel_at_edge"]
		serv_send_data = json_load["serv_send_data"]
		serv_recv_data = json_load["serv_recv_data"]
		bandwidth = json_load["bandwidth"]
		density_jam = json_load["density_jam"]
		density = json_load["density"]
		task_deadline = json_load["task_deadline"]
		pi = json_load["pi"]
		eat = json_load["EAT"]
		ldt = json_load["LDT"]
		pj = json_load["pj"]

		final_time = 0
		for i in range(N):
			for j in range(M):
				if ldt[i][j] > final_time:
					final_time = ldt[i][j]
		final_time+=120
		t_final = int(final_time/10)

		for i in range(N):
			GFG.enqueue(i,task_deadline[i])
		print(task_deadline)
		GFG.printpq()
		
		t = 10

		p_free = []
		for j in range(M):
			p_free.append(pj[j])
		
		doin_it = [[0 for itr in range(M)] for y in range(N)]

		reassign_q = set()
		running_q = set()
		
		for t_slot in range(1,t_final):
			#curr_size = GFG.size
			while GFG.size >=0:
				ind = GFG.peek()
				val = GFG.pr[ind].value
				pri = GFG.pr[ind].priority
				GFG.dequeue()
				for j in range(M):
					if(((eat[val][j] <= (t*t_slot)) & (eat[val][j]>= ((t-1)*t_slot))) | ((ldt[val][j] <= (t*t_slot)) & (ldt[val][j]>=((t-1)*t_slot)))):
						if (doin_it[val][j] == 0):
							if pi[val]<=p_free[j]:
								cov_time = l_cov[j]/vel_at_edge[j] *3600
								D_min_serv = (bandwidth[j]*(cov_time - exec_time[val]))/(density_jam[j]*l_cov[j])
								if((serv_send_data[val]+serv_recv_data[val])<=D_min_serv):
									doin_it[val][j] = 1
									p_free[j] -= pi[val]
									running_q.add((val,j))
									print("Vehicle ",val," allocated at edge ",j," at time slot ",t_slot)
									break
				# if sum(doin_it[i])<1:
				doin = 0
				for j in range(M):
					if(doin_it[val][j]==1):
						doin = 1
				if doin==0:
					reassign_q.add(val)
			for i in reassign_q:
				GFG.enqueue(i,task_deadline[i])
			reassign_q.clear()
			# done_flag = {}

			# running_q_2 = running_q
			running_q_2 = set()
			for i in running_q:
				running_q_2.add(i)
			for i in running_q_2:
				# done_flag[i[0]] = 0
				if (ldt[i[0]][i[1]] <= ((t-1)*t_slot)):
					veh = i[0]
					edge = i[1]
					p_free[edge]+=pi[veh]
					running_q.remove(i)
					# done_flag[i[0]]=1
			
			if GFG.size<0:
				print("All done at time slot",t_slot," with total time slots of ",t_final)
				break
		
		count =0
		for i in range(N):
			for j in range(M):
				if doin_it[i][j]==1:
					# print("Vehicle ",i," allocated at edge ",j,"\n")
					count+=1
		
		print("Number of vehicles allocated = ",count)

		GFG.printpq()


if __name__=="__main__":
	GFG.main([])
	
	# This code is contributed by aadityaburujwale.

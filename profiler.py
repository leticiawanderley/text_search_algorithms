import sys, os, time

if __name__=='__main__':
	PID = sys.argv[1]
	os.system("echo " + str(os.getpid()) + ">profilerpid")
	while(True):
		os.system("pidstat -r | grep " + PID +" >>" + PID)
		time.sleep(2)

def stop():
	file = open("profilerpid", 'r')
	PID = file.read();
	file.close()
	os.system("kill -9 " + PID)

def get_memory_consumption(PID):
	consumptions = []
	pfile = open(str(PID), "r")
	line = pfile.readline()
	while(line != ""):
		splited_line = line.split(" ")
		splited_line = filter(lambda a: a!='', splited_line)
		consumption = float(splited_line[5]) + float(splited_line[6])
		consumptions.append(consumption)
		line = pfile.readline()
	pfile.close
	return average(consumptions);

def average(list):
	sum = 0
	for value in list:
		sum += value
	return (sum/float(len(list)))

import os, time, profiler

class Collector:
    PID = 0
    start_time = None
    
    def start_profile(self):
        self.PID = os.getpid()
        os.system("python3 profiler.py " + str(self.PID) + "&")
        time.sleep(3);
        self.start_time = time.clock()
    
    def stop_profile(self):
        profiler.stop()
        execution_time = time.clock() - self.start_time
        memory_consumption = profiler.get_memory_consumption(self.PID)
        return (execution_time, memory_consumption);

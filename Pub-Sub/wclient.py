import zmq
import sys

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

if isinstance(zip_filter,bytes):
    zip_filter = zip_filter.decode('ascii')

socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

totalTemp = 0

for updateNbr in range(5):
    print(updateNbr)
    string = socket.recv_string()
    zipCode, temperature, relHumidity = string.split()
    totalTemp += int (temperature)
print("tem ",totalTemp," ipd ",updateNbr)
print(" Average temperature for zipcode '%s' was %dF " % (zip_filter, totalTemp/ (updateNbr+1)))
import math

output_word = open("glove.42B.300d_normalized_output", "r")
f = open("input.json", "w")
f.write("{\"nodes\":[\n")
weight_list = list()

for y in range(1):
	# weight_list.clear()
	query = output_word.readline()
	query_word = query.split("\n")
	f.write("{\"character\":\"%s\",\"id\":0,\"influence\":12,\"zone\":0},\n" % query_word[0])
	print(query)
	for x in range(20):
		line = output_word.readline()
		word, sim = line.split(" ")
		print("word " , word)
		scale_sim = (math.log(float(sim)*10000))
		print("scale_sim " , scale_sim)
		f.write("{\"character\":\"" + word + "\",\"id\":" + str(x+1) + ",\"influence\":" + str(scale_sim) + ",\"zone\":" + str(x+1) + "}")
		weight_list.append(str(scale_sim*3))
		if x != 19 :
			f.write(",\n")
		elif x == 19 :
			f.write("],")
f.write("\"links\":[")
for y in range(1):
	for x in range(20):
		f.write("{\"source\":0,\"target\":" + str(x+1) + ",\"weight\":" + weight_list[x] + "}")
		if x != 19 :
			f.write(",\n")
		elif x == 19 :
			f.write("]}")

f.close()

import csv, os, operator

experiment_folder = "results"
n_runs = 3
frequencies = [1,10,100,200,400,500,600,800,1000,2000,5000,10000,15000,20000]

def main():
	"""
	Generate 1 CSV file containing average message latency for each frequency
	"""
	# data = {0:{ "total_time_200": {"total":2, "count":3}, "total_time_400": {"total":6, "count":3}}}
	data = {}
	for freq in frequencies:
		for run in range(1, n_runs+1):
			csv_filename = os.path.join(experiment_folder, str(run), str(freq)+"_ros2.csv")
			print (csv_filename)

			csvfile = open(csv_filename)

			reader = csv.DictReader(csvfile, fieldnames=["id", "message_latency"])

			for row in reader:
				row_id = int(row["id"])
				row_message_latency = float(row["message_latency"])

				fieldname = str(freq)

				if not row_id in data:
					data[row_id] = {}
				
				if not fieldname in data[row_id]:
					data[row_id][fieldname] = {"total":0, "count":0}

				data[row_id][fieldname]["total"] += row_message_latency
				data[row_id][fieldname]["count"] += 1

	csv_filename = os.path.join(experiment_folder, "mean_times.csv")

	with open(csv_filename, "w+") as outputCSV:
		fieldnames = ["id"]
		for freq in frequencies:
			fieldnames.append("mean_time_ms_" + str(freq))
		writer = csv.DictWriter(outputCSV, fieldnames=fieldnames)
		writer.writeheader()
		#print data

		for message_id, values in sorted(data.items(), key=operator.itemgetter(0)):
			row_data = {"id":message_id}

			for freq, total_obj in values.items():
				row_data["mean_time_ms_" + str(freq)] = total_obj["total"] / float(total_obj["count"])

			writer.writerow(row_data)

if __name__ == "__main__":
    main()
with open('temperature.txt') as temperature_file:
	for line in temperature_file:
		city_name = line.strip()
		city_temperature_line_count = int(temperature_file.readline())
		
		city_temperatures = ""
		for i in range(city_temperature_line_count):
			city_temperatures += " " + temperature_file.readline().strip()
		
		# Можно так
		# city_t_as_numbers = list(map(int, city_temperatures.split()))
		
		city_t_as_numbers = []
		for t in city_temperatures.split():
			city_t_as_numbers.append(int(t))

		avg_temerature = sum(city_t_as_numbers)/len(city_t_as_numbers)

		print ("{0}: {1}".format(city_name, avg_temerature))

 #! python3
 # Quiz_Generator.py - Creates quizzes with questions and answers in
 # random order, along with the answer key.
import random 

#the keys are the contries and the values are the capital cities
african_countries = {
 'Algeria': 'Algiers',
 'Angola': 'Luanda',
 'Benin': 'Porto_Novo',
 'Botswana': 'Gaborone',
 'Burkina_Faso': 'Ouagadougou',
 'Burundi': 'Bujumbura',
 'Cameroon': 'Yaoundé',
 'Cape_Verde': 'Praia',
 'Central_African_Republic': 'Bangui',
 'Chad': "N'Djamena",
 'Comoros': 'Moroni',
 "Côte_d'Ivoire": 'Yamoussoukro',
 'Democratic_Republic_of_Congo': 'Kinshasa',
 'Djibouti': 'Djibouti',
 'Egypt': 'Cairo',
 'Equatorial_Guinea': 'Malabo',
 'Eritrea': 'Asmara',
 'Ethiopia': 'Addis_Ababa',
 'Gabon': 'Libreville',
 'Gambia': 'Banjul',
 'Ghana': 'Accra',
 'Guinea': 'Conakry',
 'Guinea_Bissau': 'Bissau',
 'Kenya': 'Nairobi',
 'Leone': 'Freetown',
 'Lesotho': 'Maseru',
 'Liberia': 'Monrovia',
 'Libya': 'Tripoli',
 'Madagascar': 'Antananarivo',
 'Malawi': 'Lilongwe',
 'Mali': 'Bamako',
 'Mauritania': 'Nouakchott',
 'Mauritius': 'Port',
 'Republic_of_Congo': 'Brazzaville',
 'Somalia': 'Mogadishu',
 'South_Africa': 'Cape_Town',
 'Sudan': 'Khartoum',
 'Swaziland': 'Mbabane',
 'Tanzania': 'Dodoma',
 'Togo': 'Lomé',
 'Tunisia': 'Tunis',
 'Uganda': 'Kampala',
 'Zambia': 'Lusaka',
 'Zimbabwe': 'Harare'}

#generate x number of different exams, where x is the number between the parenthesis below 
for exnum in range(2):
	examfile = open('capitalsexam{}.txt'.format(exnum+1), "w")
	answerfile = open('capitalsanswers{}.txt'.format(exnum+1), "w")

	#headers for the quiz
	examfile.write('Name:\n \nDate:\n \nPeriod: \n\n')
	examfile.write((' ' * 20) + 'Capitals Exam (form {})'.format(exnum+1)) 
	examfile.write('\n\n')

	#shuffle order of countries
	countries = list(african_countries.keys())
	random.shuffle(countries)

	# Loop through all  countries, making a question for each.
	for query in range(43):
		#get correct answer and other 3 wrong ones
		correct = african_countries[countries[query]]
		wrongs = list(african_countries.values())
		del wrongs[wrongs.index(correct)]
		wrongs = random.sample(wrongs, 3)
		options = wrongs + [correct]
		random.shuffle(options)

		# Write the question and the answer options to the quiz file.
		examfile.write('{}. What is the capital of {}?\n\n'.format(query + 1, countries[query]))
		for i in range(4):
			examfile.write('{}. {}\n'.format("ABCD"[i], options[i]))
			examfile.write('\n')

		# Write the answer key to a file.
		answerfile.write("{}. {}\n".format(query+1, "ABCD"[options.index(correct)]))

	examfile.close()
	answerfile.close()

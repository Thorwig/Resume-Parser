from tools import type_parse, new_contains, format_dates
from get_data import get_date, get_dates

def clean_experiences_diplomes_projets(experiences_list, keywords, keywords_a, keywords_b, keywords_lieux, sizes) :

	type_parse_experience = type_parse(experiences_list)
	experiences_list_result = []

	exp_a = {}
	mission = []
	mission_text = ""
	title = ""
	etablissement = ""
	lieu = ""
	dates= []
	first_found = False

	if type_parse_experience != -2 :
		for i in range(len(experiences_list)-1) :
			experience = experiences_list[i+1]
			if get_dates(experience) != [] :
				if not first_found :
					first_found = True
					for j in range(i + 1 - type_parse_experience, i+1) :
						mission.append(experiences_list[j])
					mission.append(remove_dates(experience,get_dates(experience)).strip())
					dates = get_dates(experience)
				else :
					new_mission = []
					k=0
					for j in range(i + 1 - type_parse_experience, i+1) :
						new_mission.append(experiences_list[j])
						k = k-1
						try :
							mission.pop(k)
						except :
							print('')
					new_mission.append(remove_dates(experience,get_dates(experience)).strip())
					for x in mission :
						if title == "" :
							for keyword in keywords :
								if new_contains(keyword, x) :
									title = remove_dates(x, get_dates(x)).strip()
									break
						if etablissement == "" :
							for keyword in keywords_a :
								if new_contains(keyword, x) :
									etablissement = remove_dates(x, get_dates(x)).strip()
									break
						if etablissement == "" :
							for keyword in keywords_b :
								if new_contains(keyword, x) :
									etablissement = keyword
									break
						if lieu == "" :
							for keyword in keywords_lieux :
								if new_contains(keyword, x) :
									lieu = keyword
									break

						mission_text = mission_text + " " + x
					exp_l = [mission_text, dates, title, etablissement, lieu]
					experiences_list_result.append(exp_l)

					mission = []
					title = ""
					mission_text = ""
					etablissement = ""
					lieu = ""

					mission = new_mission
					dates = get_dates(experience)

			elif first_found :
				mission.append(experience)

	for xx in mission :
		mission_text = mission_text + " "+ xx

		if title == "" :
			for keyword in keywords :
				if new_contains(keyword, xx) :
					title = remove_dates(xx, get_dates(xx)).strip()
					break
		if etablissement == "" :
			for keyword in keywords_a :
				if new_contains(keyword, xx) :
					etablissement = remove_dates(xx, get_dates(xx)).strip()
					break
			if etablissement == "" :
				for keyword in keywords_b :
					if new_contains(keyword, xx) :
						etablissement = keyword
						break
			if lieu == "" :
				for keyword in keywords_lieux :
					if new_contains(keyword, xx) :
						lieu = keyword
						break

	exp_l = [mission_text, dates, title, etablissement, lieu]
	experiences_list_result.append(exp_l)

	if len(experiences_list_result) == 1 and len(experiences_list_result[0][1]) ==  0 :
		experiences_list_result = []
		#Delete the title of the section
		try :
			sizes.pop(0)
			experiences_list.pop(0)
			max_sizes = sorted(list(set(sizes)))[-1]
		except :
			print(" ")

		mission_ = ""
		title = ""
		first_found_ = False
		for w in range(0, len(experiences_list)) :
			x = experiences_list[w]
			'''if not first_found_ :
				if abs(sizes[w] - max_sizes) <= 0.9 :
					title = x
					first_found_ = True
			else :
				if abs(sizes[w] - max_sizes) <= 0.9 :
					experiences_list_result.append([mission_, [], title, "", ""])
					mission_ = ""
					title = x
				else :'''
			mission_ = mission_ + " \n " + x
		experiences_list_result.append([mission_, [], title, "", ""])

	L = []
	for x in experiences_list_result :

		exp = {"date_debut":"", "date_fin":"", "duree":"", "title":"" , "description":"", "etablissement":"", "lieu":""}
		exp["description"] = x[0]
		exp["title"] = x[2]
		exp["etablissement"] = x[3]
		exp["lieu"] = x[4]

		try :
			exp["date_debut"] = format_dates(x[1][0])
		except :
			exp["date_debut"] = ""
		try :
			exp["date_fin"] = format_dates(x[1][1])
		except :
			exp["date_fin"] = ""

		exp["duree"] = ""

		if exp["date_debut"] != "error" :
			if exp["date_debut"] != "" and exp["date_fin"] != "" or exp["date_debut"] != "":

				if len(exp["date_debut"]) == 4 and len(exp["date_fin"]) == 4 and exp["date_debut"].isdigit() and exp["date_fin"].isdigit():
					print(exp["date_debut"])
					start_year = int(exp["date_debut"])
					end_year = int(exp["date_fin"])
					duree_year = abs(end_year - start_year)
					exp["duree"] = ""+ str(duree_year) + " ans"

				elif "/" in exp["date_fin"] and  "/" in exp["date_debut"] :
					try :
						start_year = int(exp["date_debut"].split("/")[-1])
						start_month = int(exp["date_debut"].split("/")[-2])
						end_year = int(exp["date_fin"].split("/")[-1])
						end_month = int(exp["date_fin"].split("/")[-2])

						if end_year != start_year :
							duree_year = abs(end_year - start_year - 1)
							duree_month = abs((12-start_month) + end_month)
							duree_year = duree_year + duree_month//12
							duree_month = duree_month%12
							exp["duree"] = ""+ str(duree_year) + " ans et "+ str(duree_month) + " mois"
						else :
							duree_month = abs(end_month - start_month)
							exp["duree"] = ""+ str(duree_month) + " mois"
					except :
						exp["duree"] = ""
				L.append(exp)
		else :
			print(L)
	return L

def clean_data(sentence, element) :
	if element in sentence :
		return sentence.replace(element, '')
	return sentence

def remove_dates(Sentence, dates) :
	if len(dates) > 0 :
		for date in dates :
			Sentence = Sentence.lower().replace(date, '').title()
	return Sentence
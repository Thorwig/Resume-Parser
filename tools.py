import datetime 
from get_data import get_dates, get_date
import re 

def tokenize_by_sentence(text) :
	tokenized_data = text.split('\n')
	return tokenized_data

def replace_all_elements(sentence, L) :
	for l in L :
		sentence = sentence.lower().replace(l, ' ')
	return sentence


def replace_all_marks(sentence, L) :
	for l in L :
		sentence = sentence.strip().replace(l, ' ')
	return sentence

def new_contains(keyword, sentence) :
	if len(keyword.split(' ')) > 1 :
		if keyword.lower().replace(' ','') in sentence.lower().replace(' ','') :
			return True
	else :
		if keyword.lower() in sentence.lower().split(' ') :
			return True
	return False

def has_at_least_one_upper(text) :
	for x in text :
		if x.isupper() :
			return True
	return False

def is_it_zone(Sentence, zone_keywords) :
	for keyword in zone_keywords :
		if len(keyword.split(' ')) == 1 :
			if keyword.lower().strip() == Sentence.lower().strip() and Sentence[0].isupper() :
				return True
		elif len(keyword.split(' ')) > 1 :
			if keyword.lower().strip() in Sentence.lower().strip() and has_at_least_one_upper(Sentence) :
				return True
	return False

def format_list_sentences(L) :
	text = ""
	for x in L :
		text = text + "\n " + x
	return text

def concat_all_lists(L) :
	new_L = []
	for x in L :
		for xx in x :
			new_L.append(xx)
	return new_L

def has_numbers(inputString):
	return any(char.isdigit() for char in inputString)


def format_dates(date) :
	date = date.replace('é','e').replace('û','u').replace('à','a').strip()
	if date.count('/') == 1 :
		return date
	elif date.count('/') == 2 :
		return date.split('/',1)[1]
	elif date.lower() in ["aujourd","present","aujourd'hui","a ce jour","en cours"] :
		return str(datetime.now().month)+"/"+str(datetime.now().year)
	elif len(date) == 4 :
		return date
	else :

		number_month = ''
		MonthsList = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
		ShortMonthsList = ["janv", "fev", "mars", "avr", "mai", "juin", "juil", "aout", "sept", "oct", "nov", "dec"]
		year = ""

		month_name = ""
		regEx = r'((?:\d\d|\d)\s(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:\d\d|\d)*\/*(?:\d\d|\d)\/(?:\d{4}|\d\d)|20\d{2}|(?:à ce jour|en cours)|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec))'
		time = re.findall(regEx, date)
		months = time[0].split(" ")[0]
		year = time[0].split(" ")[1]
		for i in range(len(MonthsList)) :
			if months == MonthsList[i] or months == ShortMonthsList[i] :
				number_month = str(i+1)
				if len(number_month) == 1 :
					number_month = '0'+number_month

				date = replace_all_elements(date, [MonthsList[i], ShortMonthsList[i]])
				break

		full_date = number_month+"/"+year
		return full_date

def type_parse(List_sentences) :

	scanned_sentence = []

	for sentence in List_sentences :
		sentence = replace_all_marks(sentence, [',','.',':','-',';'])
		if get_dates(sentence) != [] :
			if len(scanned_sentence) == 0 :
				return 0
			elif len(scanned_sentence) > 0 :
				return len(scanned_sentence) - 1
		else :
			scanned_sentence.append(sentence)
	return -2



def adjust_text(Sentences_pdf_miner, Sentences_pdf_plumber) :

	new_sentences = []

	found = False
	for x in Sentences_pdf_plumber :
		found = False
		for y in Sentences_pdf_miner :

			if len(x.lower().split(y.lower())) > 1 :
				if x.lower().split(y.lower())[0] == '' and x.lower().split(y.lower())[1] == '' :
					if not x in new_sentences :
						new_sentences.append(x)
					found = True
				elif x.lower().split(y.lower())[0] == '' and x.lower().split(y.lower())[1] != '' :
					if not x.lower().split(y.lower())[1] in new_sentences :
						new_sentences.append(x.lower().split(y.lower())[1])
					found = True
				elif x.lower().split(y.lower())[0] != '' and x.lower().split(y.lower())[1] == '' :
					if not x.lower().split(y.lower())[0] in new_sentences :
						new_sentences.append(x.lower().split(y.lower())[0])
					found = True
		if not found :
			new_sentences.append(x)



def contains_any(L, Sentence) :
	for x in L :
		if new_contains(x, Sentence) :
			return x
	return ''


def equals_any(L, Sentence) :
	for x in L :
		if x.lower().strip().replace(' ', '') == Sentence.lower().strip().replace(' ', '') :
			return True
	return False


def match_techno_category(technos_in_cv) :

	technos_in_db = get_all_technologies()
	langages_programmation = []
	frameworks = []
	bases_donnees = []
	reseau_securite = []
	cloud = []
	supervision = []
	documentation = []
	test = []
	data_ia = []
	telephonie = []
	autres = []

	for techno_in_cv in technos_in_cv :
		if techno_in_cv in technos_in_db[0] :
			langages_programmation.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[1] :
			frameworks.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[2] :
			bases_donnees.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[3] :
			reseau_securite.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[4] :
			cloud.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[5] :
			supervision.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[6] :
			documentation.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[7] :
			test.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[8] :
			data_ia.append(techno_in_cv)
		elif techno_in_cv in technos_in_db[9] :
			telephonie.append(techno_in_cv)
		else :
			autres.append(techno_in_cv)

	return langages_programmation, frameworks, bases_donnees, reseau_securite, cloud, supervision, documentation, test, data_ia, telephonie, autres


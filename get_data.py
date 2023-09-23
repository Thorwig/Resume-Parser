import re

from tools import contains_any, has_numbers, new_contains
from database_communication import get_expertise_technique_db

def get_dates(Sentence) :

	new_dates = []
	regEx = r'((?:\d\d|\d)\s(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:\d\d|\d)*\/*(?:\d\d|\d)\/(?:\d{4}|\d\d)|20\d{2}|(?:à ce jour|en cours)|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec))'
	dates = re.findall(regEx, Sentence.lower())
	for date in dates :
		new_dates.append(re.sub(r"\s{4,}"," ",date))

	if contains_any(["aujourd","aujourd'hui", "présent", "en cours", "à ce jour"], Sentence) != '' :
		new_dates.append(contains_any(["aujourd", "aujourd'hui", "présent", "en cours", "à ce jour"], Sentence))

	if len(new_dates) == 2 :
		if new_dates[0] in ["janvier","février","fevrier","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre","decembre","janv","févr","fév","fev","mars","avr","mai","juin","juil","juill","aout","sept","oct","nov","déc","dec"] :
			if len(re.findall(r'\d+', new_dates[1])) >= 1 :
				new_dates = [ new_dates[0] +" "+str(re.findall(r'\d+', new_dates[1])[-1]), new_dates[1]]
	return new_dates

def get_date(Sentence) :

	if contains_any(["aujourd", "aujourd'hui", "présent", "en cours", "à ce jour"], Sentence) != '' :
		return contains_any(["aujourd", "ajourd'hui", "présent", "en cours", "à ce jour"], Sentence)
	else :
		regEx = r'((?:\d\d|\d)\s(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec)\.*\s*\d{4}|(?:\d\d|\d)*\/*(?:\d\d|\d)\/(?:\d{4}|\d\d)|20\d{2}|(?:à ce jour|en cours)|(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|decembre|jan|janv|févr|fév|fev|mars|avr|mai|juin|juil|juill|aout|sept|oct|nov|déc|dec))'
		dates = re.findall(regEx, Sentence.lower())
		for date in dates :
			return re.sub(r"\s{4,}"," ",date)
	return ''

def get_mail(Sentence) :
	lst = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", Sentence)
	if len(lst) > 0 :
		return lst[0]
	return ""


def get_full_name(header) :
	name = ""
	i = 0
	for element in header :
		if not has_numbers(element) and len(element)>2:
			name = name+" "+element
			i = i+1
			if len(element.split(" ")) > 1 or i == 2:
				return name.title()
	return ""

def get_job_title(Sentences, keywords_job_title) :
	for sentence in Sentences :
		for keyword in keywords_job_title :
			if new_contains(keyword, sentence) :
				return sentence
	return ''

def get_phone_number(Sentence) :
	regEx = r'((?:[\+|\0{2}])*\s*(?:\d{3}|\d{2})\s*(?:\([0]\))*\s*(?:\d{3}|\d \d{2})\s*\d{2}\s*\d{2}\s*\d{2})|([0][6|7]\s*\d{2}\s*\d{2}\s*\d{2}\s*\d{2})'
	phone_numbers = re.findall(regEx, Sentence.lower().replace(' ','').replace('.','').replace('-','').replace('(','').replace(')',''))
	if len(phone_numbers) > 0 :
		if len(phone_numbers[0]) > 0 :
			for x in phone_numbers[0] :
				if not x == '' :
					return x
	return ''

def get_certificats_data(Sentence, keywords_certificat) :
	certifs = []
	only_date = get_dates(Sentence)
	for keyword in keywords_certificat :
		sub_certifs = {'date':'', 'certif':''}
		if new_contains(keyword, Sentence) :
			sub_certifs['date'] = only_date
			sub_certifs['certif'] = keyword
			certifs.append(sub_certifs)
	return certifs



def get_all_technologies():

	return get_expertise_technique_db(10), get_expertise_technique_db(11), get_expertise_technique_db(12), get_expertise_technique_db(13),  get_expertise_technique_db(14), get_expertise_technique_db(15), get_expertise_technique_db(16), get_expertise_technique_db(17), get_expertise_technique_db(18) , get_expertise_technique_db(19), get_expertise_technique_db(20)

def get_expertises_techniques(sentence, keywords_expertises_techniques) :
	sub_exp_tech = []
	for keyword in keywords_expertises_techniques :
		if new_contains(keyword, sentence) :
			sub_exp_tech.append(keyword)

	return sub_exp_tech

def get_langues(sentence,keywords_langues) :
	langues = []
	tokens = sentence.split(' ')
	keywords_langues = [x.lower() for x in keywords_langues]
	for token in tokens :
		if token.lower() in keywords_langues :
			langues.append(token.title())
	return langues

def get_duree_experience(experiences) :
	annees = 0
	mois = 0
	for experience in experiences :
		if experience['duree'] != '' :
			duree_elements = [int(s) for s in experience['duree'].split() if s.isdigit()]
			if len(duree_elements) == 2 :
				annees = annees + duree_elements[0]
				mois = mois + duree_elements[1]
			elif len(duree_elements) == 1 :
				mois = mois + duree_elements[0]

	annees = annees + mois//12
	mois = mois%12
	return ""+str(annees)+" ans et "+str(mois)+" mois"
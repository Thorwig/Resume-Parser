# coding: utf-8
import os
import json

import sys

from database_communication import get_data_from_db
from get_files_data import get_data_from_pdf, get_data_from_word
from get_data import get_all_technologies, get_certificats_data, get_expertises_techniques, get_full_name, get_job_title,get_mail,get_phone_number, get_duree_experience, get_langues
from tools import concat_all_lists, replace_all_marks, is_it_zone, match_techno_category, tokenize_by_sentence
from data_cleaning import clean_experiences_diplomes_projets
from json_write import write_json_output

def function_final(number):
	file_path = sys.argv[1]
	pdf_file_name = os.path.basename(file_path)

	if file_path.lower().endswith('.docx') :
		sentences = tokenize_by_sentence(get_data_from_word(file_path))
	else :
		L= get_data_from_pdf(file_path,number)
		print(L)
		sentences = L[0]
		sizes = L[1]


	already_analyzed = []
	#Get data diplomes
	keyword_zone_diplome = get_data_from_db('1', 1)
	keywords_diplomes_a = get_data_from_db('0', 1)
	keywords_diplomes_b = get_data_from_db('0', 21)

	keywords_etablissements_a = get_data_from_db('0', 2)
	keywords_etablissements_b = get_data_from_db('0', 22)

	diplomes = []

	#Get data expériences professionnelles
	keyword_zone_exp_pro = get_data_from_db('1', 3)
	keywords_experiences_professionnelles_a = get_data_from_db('0', 3)
	keywords_experiences_professionnelles_b = get_data_from_db('0', 23)
	keywords_entreprises = get_data_from_db('0', 4)
	keywords_lieux = get_data_from_db('0', 5)
	experiences_professionnelles = []
	missions = []

	#Get data from the database
	keyword_zone_certificats = get_data_from_db('1', 6)
	keywords_certificats = get_data_from_db('0', 6)
	certificats = []

	#Get data expertises techniques
	keywords_expertises_techniques = concat_all_lists(get_all_technologies())
	expertises_techniques = []

	#Get data langues
	keyword_zone_langues = get_data_from_db('1',7)
	keywords_langues = get_data_from_db('0', 7)
	langues = []

	#Get data projets
	keyword_zone_projets = get_data_from_db('1', 8)
	keywords_projets = ["Projet"]

	#other_zones_keywords = get_data_from_db('1', 9)
	other_zones_keywords_a = ["Profil","T E C H N O L O G I E S", "P A P I E R S   S C I E N T I F I Q U E S   P U B L I É S", "Technologies","Centres d'intérêt", "Compétences", "Competences", "loisir", "loisirs", "Centres d'intérêt", 'Intérêts', 'Connaissances Informatique', 'Qualités', 'Connaissances académiques', 'Competences', 'COMPÉTENCES TECHNIQUES']
	all_zones_keywords = [keyword_zone_diplome, keyword_zone_exp_pro, keyword_zone_certificats]
	other_zones_keywords = [x for y in all_zones_keywords for x in y]

	job_title_keywords = [keywords_diplomes_a, keywords_experiences_professionnelles_a, keywords_diplomes_b, keywords_experiences_professionnelles_b]
	job_title_keywords = [x for y in job_title_keywords for x in y]

	current_zone = ''

	#Get general information
	header = []
	after_header = False
	header_used = False

	mail_found = False
	mail = ''

	phone_number_found = False
	phone_number = ''

	nom_prenom = ''
	job_title = ''

	included_in_projects = False
	projects_found = False
	projects = []
	project_title = ''
	project = {'date':'', 'project':''}

	exp_already_found = False
	sub_mission = []

	experiences_sentences = []
	experiences_sentences_sizes = []

	formations_sentences = []
	formations_sentences_sizes = []

	projets_sentences = []
	projets_sentences_sizes = []

	others_sentences = []
	others_sentences_sizes = []

	zones_title_size = 0.0

	for i in range(len(sentences)) :
		new_sentence = sentences[i]
		cleaned_sentence = replace_all_marks(new_sentence, [',','.',':','-',';']).replace('’', '\'')
		if is_it_zone(cleaned_sentence, keyword_zone_diplome) :
			zones_title_size = sizes[i]
			break
		elif is_it_zone(cleaned_sentence, keyword_zone_exp_pro) :
			zones_title_size = sizes[i]
			break

	for i in range(len(sentences)) :

			sentence = sentences[i].replace('’', '\'')
			if not mail_found :
				if get_mail(sentence) != '' :
					mail = get_mail(sentence)
					mail_found = True

			if not phone_number_found :
				if get_phone_number(sentence) != '' :
					phone_number = get_phone_number(sentence)
					phone_number_found = True

			cleaned_sentence = replace_all_marks(sentence, [',','.',':','-',';'])

			if is_it_zone(cleaned_sentence, keyword_zone_diplome) : #and abs(sizes[i]-zones_title_size) <= 1 :
				current_zone = 'diplomes'
				already_analyzed.append('diplomes')
				after_header = True
			elif is_it_zone(cleaned_sentence, keyword_zone_exp_pro) : #and abs(sizes[i]-zones_title_size) <=1 :
				current_zone = 'experiences'
				already_analyzed.append('experiences')
				after_header = True
			elif is_it_zone(cleaned_sentence, keyword_zone_projets) : #and abs(sizes[i]-zones_title_size) <= 1 :
				current_zone = 'projets'
				already_analyzed.append('projets')
				after_header = True
			elif is_it_zone(cleaned_sentence, keyword_zone_langues) :
				current_zone = 'langues'
				already_analyzed.append('langues')
				after_header = True
			elif is_it_zone(sentence, other_zones_keywords_a) : #and abs(sizes[i]-zones_title_size) <= 1 :
				current_zone = 'other'
				after_header = True

			print(sentence)
			print(current_zone)


			if not after_header :
				header.append(sentence.strip())
			elif not header_used :
				header_used = True
				if len(header)>0 :
					nom_prenom = get_full_name(header)
				job_title = get_job_title(header, job_title_keywords)

			if current_zone == 'projets' :
				projets_sentences.append(sentence)
				projets_sentences_sizes.append(sizes[i])
			elif current_zone == 'diplomes':
				formations_sentences.append(sentence)
				formations_sentences_sizes.append(sizes[i])
			elif current_zone == 'experiences':
				experiences_sentences.append(sentence)
				experiences_sentences_sizes.append(sizes[i])
			elif current_zone == 'other' :
				others_sentences.append(sentence)
				others_sentences_sizes.append(sizes[i])

			sub_certificat = get_certificats_data(cleaned_sentence, keywords_certificats)
			if len(sub_certificat) > 0 :
				for certif in sub_certificat :
					certifat_json = {}
					certifat_json['date'] = certif['date']
					certifat_json['certif'] = certif['certif']
				certificats.append(certifat_json)

			sub_exp_techniques = get_expertises_techniques(cleaned_sentence, keywords_expertises_techniques)
			if len(sub_exp_techniques) > 0 :
				for tech in sub_exp_techniques :
					expertises_techniques.append(tech)

			langs = get_langues(cleaned_sentence, keywords_langues)
			if len(langs) > 0 :
				for lang in langs :
					langues.append(lang)

	formations = clean_experiences_diplomes_projets(formations_sentences, keywords_diplomes_b, keywords_etablissements_b, keywords_etablissements_a, keywords_lieux, formations_sentences_sizes)
	experiences = clean_experiences_diplomes_projets(experiences_sentences,keywords_experiences_professionnelles_b, [], keywords_entreprises,keywords_lieux, experiences_sentences_sizes)
	projets = clean_experiences_diplomes_projets(projets_sentences,keywords_projets,[], keywords_entreprises, keywords_lieux, projets_sentences_sizes)


	expertises_techniques = match_techno_category(list(set(expertises_techniques)))
	return pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, get_duree_experience(experiences)

if '__main__' == __name__ :
	r = []
	for i in range(3):
		r.append(function_final(i+1))
	if len(r[0][9]) >= len(r[1][9]) and len(r[0][9]) >= len(r[2][9]) and len(r[0][8]) >= len(r[1][8]) and len(r[0][8]) >= len(r[2][8]):
		pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences = function_final(1)
		write_json_output(pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences)
	elif len(r[1][9]) >= len(r[0][9]) and len(r[1][9]) >= len(r[2][9]) and len(r[1][8]) >= len(r[2][8]) and len(r[1][8]) >= len(r[0][8]):
		pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences = function_final(2)
		write_json_output(pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences)
	elif len(r[2][9]) >= len(r[1][9]) and len(r[2][9]) >= len(r[0][9]) and len(r[2][8]) >= len(r[1][8]) and len(r[2][8]) >= len(r[0][8]):
		pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences = function_final(3)
		write_json_output(pdf_file_name, nom_prenom, phone_number, mail, job_title, certificats, expertises_techniques, langues, formations, experiences, projets, duree_experiences)
	else :
		print('error')

	for i in range(3):
		print(str(len((r[i][9]))) + str(len((r[i][8]))))



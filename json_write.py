import json
from database_communication import current_script_path

def write_json_output(file_name, nom_prenom, tel, mail, job_title, certificats, expertises_techniques, langues, diplomes, experiences, projets, duree_experience) :

	our_json = {}
	our_json["nom_prenom"] = nom_prenom
	our_json["job_title"] = job_title
	our_json["email"] = mail
	our_json["tel"] = tel
	our_json["duree_experience"] = duree_experience
	our_json["certifications"] = certificats

	json_expertises_techniques = []
	for i in range(len(expertises_techniques)) :
		categ = {}
		if len(expertises_techniques[i]) > 0 :
			categ["id_category"] = i+10
			categ["technologies"] = expertises_techniques[i]
			json_expertises_techniques.append(categ)

	our_json["expertise_technique"] = json_expertises_techniques
	our_json["experiences_professionnelles"] = experiences
	our_json["diplomes"] = diplomes
	our_json["langues"] = langues
	our_json["projets"] = projets

	# Writing to sample.json
	with open(current_script_path+"/output_json/"+file_name+".json", "w", encoding='utf-8') as outfile:
		json.dump(fp=outfile, indent=4, obj=our_json)
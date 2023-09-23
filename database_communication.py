import mysql.connector
import os
import json
#database management

current_script_path = os.path.realpath(__file__)
current_script_path = os.path.dirname(current_script_path)

with open(current_script_path+'/Titres/db_params.json', encoding='utf-8') as f:
	data = json.load(f)
	
def get_data_from_db(est_zone, id_category_keyword):

	mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
	mycursor = mydb.cursor()

	mycursor.execute("""SELECT libelle_keyword FROM keywords where id_category = %s AND est_zone = %s""", (id_category_keyword, est_zone))
	myresult = mycursor.fetchall()
	keywords = []
	for x in myresult :
		keywords.append(x[0])
	return keywords

def get_expertise_technique_db(id_category) :

	mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
	mycursor = mydb.cursor()

	mycursor.execute("""SELECT id_category, libelle_keyword FROM keywords where id_category = """+str(id_category))
	myresult = mycursor.fetchall()

	keywords_category = []
	for result in myresult :
		keywords_category.append(result[1])

	return keywords_category
import docx2txt

from pdfminer.layout import LAParams, LTTextBox, LTChar
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pandas as pd

def get_data_from_word(filename):

	temp = docx2txt.process(filename)
	text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
	return ' \n '.join(text)

def get_data_from_pdf(pdf_path,number) :

	fp = open(pdf_path, 'rb')
	rsrcmgr = PDFResourceManager()
	laparams = LAParams()
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	pages = PDFPage.get_pages(fp)

	L = []
	text = ""

	sentences = []
	sizes = []

	for page in pages:

		X = []
		Y = []
		Texts = []
		Z = []
		Font_size = 0.0
		Font_name = ""

		interpreter.process_page(page)
		layout = device.get_result()
		for lobj in layout:
			if isinstance(lobj, LTTextBox):
				for text_line in lobj:
					try :
						for character in text_line:
							if isinstance(character, LTChar):
								Font_size=character.size
								Font_name=character.fontname
								X.append(character.matrix[-2])
								Y.append(character.matrix[-1])
								Z.append(Font_size)
								Texts.append(text_line.get_text())
								break
					except :
						pass

		data = {'X':X, 'Y':Y, 'Text': Texts, 'Size':Z}
		df = pd.DataFrame(data)
		df = df.sort_values('Y', ascending=False)
		print(df)

		if number == 1:
			left = list(df[df['X']>0]['Text'])
			left_size = list(df[df['X']>0]['Size'])

			middle = []
			middle_size = []

			right = []
			right_size = []
		elif number==2:
			left = list(df[df['X']<120]['Text'])
			left_size = list(df[df['X']<120]['Size'])

			right = list(df[df['X']>=120]['Text'])
			right_size = list(df[df['X']>=120]['Size'])

			middle = []
			middle_size = []

		elif number==3:
			left = list(df[df['X']<120]['Text'])
			left_size = list(df[df['X']<120]['Size'])

			middle = list(df[(df['X']>=120) & (df['X']<350)]['Text'])
			middle_size = list(df[(df['X']>=120) & (df['X']<350)]['Size'])

			right = list(df[df['X']>=350]['Text'])
			right_size = list(df[df['X']>=350]['Size'])

		one = left
		one_sizes = left_size
		two = middle
		two_sizes = middle_size
		three = right
		three_sizes = right_size

		for i in range(len(one)) :
			if len(one[i].split('\n')) > 1 :
				sub_l = one[i].split('\n')
				for j in range(len(sub_l)) :
					sentences.append(sub_l[j])
					sizes.append(one_sizes[i])
			else :
				sentences.append(one[i])
				sizes.append(one_sizes[i])

		for i in range(len(two)) :
			if len(two[i].split('\n')) > 1 :
				sub_l = two[i].split('\n')
				for j in range(len(sub_l)) :
					sentences.append(sub_l[j])
					sizes.append(two_sizes[i])
			else :
				sentences.append(two[i])
				sizes.append(two_sizes[i])

		for i in range(len(three)) :
			if len(three[i].split('\n')) > 1 :
				sub_l = three[i].split('\n')
				for j in range(len(sub_l)) :
					sentences.append(sub_l[j])
					sizes.append(three_sizes[i])
			else :
				sentences.append(three[i])
				sizes.append(three_sizes[i])

	return sentences, sizes
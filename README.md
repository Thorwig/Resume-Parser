<div align="center">
<h1 align="center">
<br>Resume-parser
</h1>
<h3>◦ Extract the most important from your resume</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style&logo=SciPy&logoColor=white" alt="SciPy" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style&logo=spaCy&logoColor=white" alt="spaCy" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)

---


## 📍 Overview

The project is a resume parser that extracts relevant information from text data, such as contact details, job title, certifications, technical expertise, languages, education, work experience, and projects. It utilizes various parsing techniques and libraries to process PDF and Word documents, clean and organize the extracted data, and write the output into a JSON file. The project's core functionalities enable automated extraction and analysis of resume data, providing valuable insights for further processing and analysis.

---


## 📂 Repository Structure

```sh
└── Resume-parser/
    ├── Titres/
    │   └── db_params.json
    ├── data/
    │   ├── certificats_data.csv
    │   ├── etablissements_data.csv
    │   ├── experiences_data.csv
    │   ├── formations_data.csv
    │   ├── langues_data.csv
    │   └── technologies_data.csv
    ├── data_cleaning.py
    ├── database_communication.py
    ├── docx-template/
    │   ├── _rels/
    │   │   └── .rels
    │   ├── docProps/
    │   │   └── thumbnail.jpeg
    │   └── word/
    │       ├── fontTable.xml
    │       ├── numbering.xml
    │       ├── settings.xml
    │       ├── styles.xml
    │       └── theme/
    │           └── theme1.xml
    ├── get_data.py
    ├── get_files_data.py
    ├── json_write.py
    ├── main.py
    ├── requirements.txt
    └── tools.py
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [get_data.py](https://github.com/Thorwig/Resume-parser/blob/main/get_data.py)                             | The code provides several functions for parsing and extracting specific information from text data.-'get_dates' extracts dates from input sentences using regular expressions.-'get_date' returns a single date from a sentence.-'get_mail' extracts the first email address found in a sentence.-'get_full_name' retrieves a person's full name from a header, based on the absence of numbers and with a minimum length requirement.-'get_job_title' identifies a job title from a list of sentences based on specific keywords.-'get_phone_number' extracts phone numbers from a sentence using regular expressions.-'get_certificats_data' finds certificates and their associated dates from a sentence, based on specific keywords.-'get_all_technologies' retrieves expertise in various technologies from a database.-'get_expertises_techniques' identifies expertise in specific technology from a sentence, based on keywords.-'get_langues' extracts spoken languages from a sentence, based on specific keywords.-'get_duree_experience' calculates the total duration of experience based on a list of experiences.These functions enable the extraction of relevant information from text data, providing valuable insights for analysis and processing. |
| [requirements.txt](https://github.com/Thorwig/Resume-parser/blob/main/requirements.txt)                   | This code consists of multiple Python packages and libraries that provide various functionalities such as file handling, data processing, PDF manipulation, natural language processing, web development, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [json_write.py](https://github.com/Thorwig/Resume-parser/blob/main/json_write.py)                         | The code writes a JSON output file with various details (name, job title, certifications, expertise, experiences, etc.) by creating a dictionary object and saving it to a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [database_communication.py](https://github.com/Thorwig/Resume-parser/blob/main/database_communication.py) | This code facilitates accessing and retrieving data from a MySQL database. It includes functions to retrieve keywords based on specific criteria, such as category and zone, and expertise categories based on the category ID. The code reads the database parameters from a JSON file for connection details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [data_cleaning.py](https://github.com/Thorwig/Resume-parser/blob/main/data_cleaning.py)                   | The code is a function that cleans and extracts relevant information from a list of experiences, diplomas, and projects. It uses various parsing techniques to identify and organize the data. The cleaned data is then formatted and returned as a list of dictionaries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [main.py](https://github.com/Thorwig/Resume-parser/blob/main/main.py)                                     | The code performs data extraction and analysis from PDF and Word documents. It extracts information such as full name, contact details, job title, certifications, technical expertise, languages, education, work experience, and projects. The data is cleaned and processed using various functions and written into a JSON output file. The code iterates over multiple documents, selects the document with the most relevant data, and writes the output into a JSON file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [tools.py](https://github.com/Thorwig/Resume-parser/blob/main/tools.py)                                   | The code consists of several functions that perform various tasks such as tokenizing sentences, replacing elements in sentences, checking for specific patterns or keywords, formatting and concatenating lists of sentences, checking for numbers in strings, formatting dates, and matching technology categories. The functions are designed to enhance text processing and analysis capabilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [get_files_data.py](https://github.com/Thorwig/Resume-parser/blob/main/get_files_data.py)                 | This code extracts data from Word documents and PDF files. It uses external libraries to convert word documents into text and extract data from specific regions of PDF pages based on their coordinates. The extracted data is organized into sentences and sizes, which are returned as output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>_rels</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                    |
| [.rels](https://github.com/Thorwig/Resume-parser/blob/main/docx-template/_rels/.rels) | The code is an XML document that encapsulates relationships between various files in an Open XML package. It specifies relationships such as extended properties, office documents, metadata thumbnail, and core properties. These relationships help to organize and connect different components within the package. |

</details>

---

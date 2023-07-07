# Parser for website documentation docs.python.org

## Description
The parser outputs the collected information to two .csv files:
  - The list of all PEPs is displayed in the first file: number, name and status.
  - The second file contains a summary of the PEP statuses - how many documents were found in each status (status, quantity) and the total number (Total).
The parser saves data to .csv files in the results/ directory, located in the project root.

## Technologies used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Scrapy](https://img.shields.io/badge/Scrapy-3776AB?style=for-the-badge)

## Launching the parser

1.Clone the repository:
```
git@github.com:Alehmas/scrapy_parser_pep.git
```

2.Install virtual environment:
```
python -m venv venv
```

3.Install all dependencies:
```
pip install -r requirements.txt
```

4.Run parser:
```
scrapy crawl pep
```

## Authors
- [Aleh Maslau](https://github.com/Alehmas)


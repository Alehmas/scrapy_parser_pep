# Parser for website documentation docs.python.org



The parser can:
  1. Lists all PEPs (number, name, status) and saves to a csv file.
  2. compiles a summary of the PEP statuses - how many documents were found in each status and saves it to a csv file.

  
## Launching the parser

1.Clone the repository:
<pre>
git@github.com:Oleg-2006/scrapy_parser_pep.git
</pre>

2.Install virtual environment:
<pre>
python -m venv venv
</pre>

3.Install all dependencies:
<pre>
pip install -r requirements.txt
</pre>

4.Run parser:
<pre>
scrapy crawl pep
</pre>



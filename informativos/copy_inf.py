# Copyright (C) 2020 Ian Liu Rodrigues <ian.liu88@gmail.com> <https://github.com/ianliu>


from urllib.request import urlopen
from lxml import etree
from os.path import basename

url = 'https://www.indaiatuba.sp.gov.br/saude/vigilancia-em-saude/vigilancia-epidemiologica/novo-coronavirus/informativos-epidemiologicos/'
query = '/html/body/div[2]/div[1]/div[4]/div/div[3]/ul/li/a/@href'

parser = etree.HTMLParser()
doc = etree.parse(urlopen(url), parser)
links = ['https://www.indaiatuba.sp.gov.br' + p for p in doc.xpath(query)]

for link in links:
    with open(basename(link), 'wb') as out:
        response = urlopen(link)
        out.write(response.read())

# titulky.com
# Subtitles service allowed by www.titulky.com

import re

TITULKYCOM_SEARCH_URL = 'http://www.titulky.com/?Fulltext=%s'

def Start():
  HTTP.CacheTime = CACHE_1DAY
  HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'

class TitulkyComAgent(Agent.Movies):
  name = 'Titulky.com'
  languages = ['cz']
  primary_provider = False
  contributes_to = ['com.plexapp.plugins.titulkycom']

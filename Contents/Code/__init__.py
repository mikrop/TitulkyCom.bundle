def Start():
    HTTP.CacheTime = CACHE_1DAY
    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'

class TitulkyComAgent(Agent.Movies):
    name = 'Titulky.com'
    primary_provider = False
    languages = [Locale.Language.Czech]

    def search(self, results, media, lang):
      pass

    def update(self, metadata, media, lang):
      pass

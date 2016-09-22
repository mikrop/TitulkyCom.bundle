
def Start():
    HTTP.CacheTime = 0
    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'

class TitulkyComAgent(Agent.Movies):
    name = 'Titulky.com'
    primary_provider = False
    languages = [Locale.Language.Czech]

    def search(self, results, media, lang):
        Log("search TitulkyCom. Lang: " + lang)

    def update(self, metadata, media, lang):
        Log("update TitulkyCom. Lang: " + lang)

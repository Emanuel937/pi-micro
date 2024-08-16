from google_search import GoogleSearch

class GetPosition(GoogleSearch):

    def __init__(self, **kwargs) -> None:
        super().__init__()                                             # Correctement initialiser la classe parente
        self.keyword      = kwargs.get("keyword",    None)
        self.website_url  = kwargs.get("website_url", None)
        self.pos          = 0
        self.pageIndexedStatus  = self.isIndexed()
        

    def isIndexed(self):
        query         = f"site:{self.website_url}" 
        containers    = self.google_search(query)
 
        try: 
            data = containers.get('items', [])
            data[0]
            status  = 200
        except Exception:
            status  = 404
        
        return status
    
    def selectCountryAndLanguage(self):

        return {
            "gl":"fr",
            "hl":"fr"
        }
    
    def position(self, start=1):

        arg = self.selectCountryAndLanguage()
        #######
        print(f"status is : {self.pageIndexedStatus}")
        if self.pageIndexedStatus != 404:
                
                query_result = self.google_search(self.keyword, start=1, **arg)
                query_result = query_result.get('items', [])

                for item in query_result:
                    link = item.get('link')
                    print(link)
                    if self.website_url in link:
                        print(f"--------------- YOUR POSITION IS N° {self.pos} on this keyword : {self.keyword}")
                        return self.pos
                    
               
                print(f"########   start n° is : {start}  &&&&&  POS : {self.pos}")
                self.pos += 1
                start +=10
                self.position(start=start)
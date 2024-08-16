from googleapiclient.discovery import build

class GoogleSearch:

    def __init__(self) -> None:
        self.API_KEY    = 'AIzaSyDygRCiS1D6TpYJGWYjmJjKtfTO4rpcRVY'
        self.CSE_ID     = '66976143313c647de'

    def google_search(self, query, start=1, **kwargs):

        service = build("customsearch", "v1", developerKey=self.API_KEY)
        res     = service.cse().list(q=query, cx=self.CSE_ID, start=start, **kwargs).execute()

        return res



#    Print search results
#    for item in results.get('items', []):
#    title = item.get('title')
#    link = item.get('link')
#    snippet = item.get('snippet')
#    print(f"Title: {title}")
#    print(f"Link: {link}")
#    print(f"Snippet: {snippet}")
#    print('-' * 10)

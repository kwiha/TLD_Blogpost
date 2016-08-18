from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyC_23J01w6b2N0sqGUD_0yFPtH_rXOz3n4"
my_cse_id = "000259337489158056875:qfncyaub4jk"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'site:*.ke', my_api_key, my_cse_id, num=20)
for result in results:
    pprint.pprint(result)

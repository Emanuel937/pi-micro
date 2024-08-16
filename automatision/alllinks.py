import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def make_absolute(base_url, link):
    """
    Convertit un lien relatif en lien absolu basé sur l'URL de base.
    """
    return urljoin(base_url, link)

def get_all_links(base_url):
    """
    Récupère tous les liens d'un site web en suivant les liens internes.
    """
    visited, to_visit, all_links = set(), [base_url], set()
    
    while to_visit:
        url = to_visit.pop()
        
        # Vérifier si l'URL a déjà été visitée
        if url in visited:
            continue
        
        visited.add(url)
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lancer une exception pour les codes de statut HTTP 4xx/5xx
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Trouver tous les liens dans la page
            for link in soup.find_all('a', href=True):
                full_url = make_absolute(url, link['href'])
                
                # Vérifier si l'URL est interne au site de base
                if full_url.startswith(base_url) and full_url not in all_links:
                    all_links.add(full_url)
                    to_visit.append(full_url)
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue
    
    return all_links

# URL de base du site à analyser
base_url = 'https://agence-web-pro.fr'
links = get_all_links(base_url)

# Afficher tous les liens trouvés
for link in links:
    print(link)




url_status = [
    {
     "url":"url",
     "status":"Broken_url",
        
    }
]
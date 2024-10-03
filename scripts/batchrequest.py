import requests
import os

def download_images(n, url_template, save_folder):
    """
    Exemple d'utilisation:
    n = 10
    url_template = "https://example.com/path/to/images/image_{}.jpg"
    save_folder = "download"
    download_images(n, url_template, save_folder)
    Args:
        n (_type_): _description_
        url_template (_type_): _description_
        save_folder (_type_): _description_
    """
    # Créer le dossier si ce n'est pas déjà fait
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    # Boucle pour le nombre d'images
    for i in range(1, n + 1):
        # Construire l'URL de l'image
        url = url_template.format(i)
        try:
            # Faire la requête HTTP
            response = requests.get(url)
            # Vérifier que la requête s'est bien passée
            response.raise_for_status()
            # Créer le chemin complet pour enregistrer l'image
            image_path = os.path.join(save_folder, f'{i}.jpg')
            # Enregistrer l'image
            with open(image_path, 'wb') as file:
                file.write(response.content)
            print(f"Image {i} telechargee avec succes.")
        except requests.exceptions.RequestException as e:
            print(f"Echec du telechargement de l'image {i}: {e}")

# Remplacez par votre template d'URL
download_images(10, "https://example.com/path/to/images/image_{}.jpg", "download")
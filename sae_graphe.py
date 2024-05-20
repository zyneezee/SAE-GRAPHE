import json

#6.1 
def txt_to_json(input_file, output_file):
    """
    Lit un fichier texte contenant des objets JSON sur chaque ligne et les écrit dans un nouveau fichier JSON.
    
    Args:
        input_file (str): Nom du fichier texte d'entrée contenant les chaînes JSON.
        output_file (str): Nom du fichier de sortie pour écrire le tableau JSON.
    """
    try:
        json_list = []
        with open(input_file, 'r') as file:
            for line in file:
                #Convertir la chaîne JSON en un dictionnaire Python et l'ajouter à la liste
                json_obj = json.loads(line)
                json_list.append(json_obj)
        
        #Écrire la liste des objets JSON dans le fichier de sortie
        with open(output_file, 'w') as file1:
            json.dump(json_list, file1, indent=4)
        
        print("Les données ont été écrites avec succès dans " + output_file)
    
    except Exception as e:
        print("Il y a une erreur !")

txt_to_json('data_100.txt', 'data_100.json')



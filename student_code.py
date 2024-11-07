from crypt_1 import gen_key


def decrypt(C):
  M=""
  current_code =""
  #entrez votre code ici.
  #Vous pouvez créer des fonctions auxiliaires et adapter le code à votre façon mais decrypt dois renvoyer le message décrypté
  # Dictionnaire inversé, à générer ou passer comme paramètre
  dictionnaire = gen_key("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
  dictionnaire_inverse = {v: k for k, v in dictionnaire.items()}
    
  # Parcourt chaque caractère dans le texte chiffré
  for char in C:
    current_code += char
    # Vérifie si le code binaire actuel est dans le dictionnaire inverse
    if current_code in dictionnaire_inverse:
      M += dictionnaire_inverse[current_code]
      current_code = ""  # Réinitialise le code actuel pour la prochaine séquence
    
  return M
#PROGRAMME DE SEGMENTATION ET D'ETIQUETAGE D'UN CORPUS

import spacy
import fr_core_news_sm
nlp = fr_core_news_sm.load()

#INPUT DU FICHIER CORPUS
print ("\nEntrez le nom du fichier que vous souhaitez traiter : ")
nom_de_fichier = input()
texte = open(nom_de_fichier, "r")
content = texte.read()								

#TACHE DE SEGMENTATION EN PHRASES
def segmentation_en_phrases (content):
  phrases = nlp(content)
  print('\n\n---------------------- TEXTE SEGMENTE EN PHRASE ----------------------\n')
  for sent in phrases.sents:
    print(sent.text)

#TACHES DE SEGMENTATION EN MOTS + ETIQUETAGE + SORTIE
def segmentation_en_mots (content):
  mots = nlp(content)				 						
  print('\n\n---------------------- TEXTE ETIQUETE ----------------------\n')
  for token in mots:
    print("{0}\t{1}\t{2}\t{3}\t{4}".format(
      token.text,
      token.lemma_,
      token.pos_,
      token.tag_,
      token.dep_,
    ))

segmentation_en_phrases (content)
segmentation_en_mots (content)

texte.flush()
texte.close()

import numpy
import shutil
# from Onto_function import Onto
from RDF_funtion import Onto, text
from owlready2 import *
import json
# Import Ontology and Scenario file
Scene_onto_main = 'demo.owl'
Scene_onto = 'demo1.owl'
shutil.copy(Scene_onto_main, Scene_onto)
SDL_file = 'File.txt'
# import Ontology to class

Onto1 = Onto(Scene_onto)

Dem = Onto1.Text_to_SDL(SDL_file,Scene_onto)

def examples():
    # Determine all the classes, data prop in the ontology
    # print(list(Scene_onto.classes()))
    # print(list(Scene_onto.data_properties()))
    
    # IRI acess for an element
    # Obstacle_class = Onto1.search_iri("*obstacle")
    return None
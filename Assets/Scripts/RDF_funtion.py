from owlready2 import *
import rdflib
from rdflib import URIRef, Graph, Literal
from rdflib.namespace import RDF, XSD
import socket
import time
Main = 'http://www.semanticweb.org/spoyyam/ontologies/2023/2/untitled-ontology-17#'
rdf_type=URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
has_type=URIRef('http://www.semanticweb.org/spoyyam/ontologies/2023/2/untitled-ontology-17#has_type')

class Onto:
    def __init__(self,file):
        self.file  =  file
    
    # import Ontology using owlready
    def Onto_import(self): 
        File = get_ontology(self.file).load()
        return File
    
    # Search by label
    def search_label(self,file,string):
        labels = file.search(label = string)
        return labels
    
    # Search by IRI
    def get_iri(self,string):
        op = string.iri
        return op

    # Create triplets
    def create_trip(self,file, input):
        # Extract property from text
        subject, predicate, object = text.extract_property(input)

        # Importing Ontology
        File = self.Onto_import()
        
        # Import RDFlib 
        G_rdf = RDF.import_RDF(file)
        
        # Search from ontology
        property = self.search_label(File,predicate)
        object_l = text.string_to_float(object)

        # finding the domain from the property
        class_name = property[0].domain
        class_name_iri = URIRef(str(self.get_iri(class_name[0]))) 

        # create instance of the class
        subject_name = class_name[0](str(subject))
        subject_name_iri =URIRef(str(self.get_iri(subject_name))) # IRI conversion
        G_rdf.add((subject_name_iri,rdf_type,class_name_iri))

        #  Add the type of obstacle for every obstacle
        self.add_type(G_rdf, File)

        # Combination of triplets in a single line
        if (len(object_l)==len(property)) == True:
             for i in range(0,len(property)):
                property_des = property[i]
                property_des_iri = URIRef(str(self.get_iri(property_des))) # IRI converison
                object_iri = Literal(object_l[i], datatype= XSD.float)
                G_rdf.add((subject_name_iri,property_des_iri,object_iri))
                G_rdf.serialize(destination=file, format='xml')
        return G_rdf
    

    def Connection_Csharp(self,obs_list):
        server_socket = socket.socket()
        host = 'localhost'
        port = 5000
        server_socket.bind((host, port))
        server_socket.listen(1)
        print('Waiting for a client to connect...')
        client_socket, client_address = server_socket.accept()
        print('Client connected:', client_address)
        strings = obs_list
        try:
            for string in strings:
                # Send each string
                print(string)
                client_socket.send(string.encode())
                time.sleep(.01)
        finally:
        #     Close the socket
                client_socket.close()
                server_socket.close()
                
        
    def Spawn_query(self,Onto):
        Qf_list = []
        Qf_list_ans = []
        open('testing.owl', 'w').close()
        Onto.serialize(destination='testing.owl', format='xml')
        File = get_ontology('testing.owl').load()
        Query_needed = ["""demo1:is_located_at_x""","""demo1:is_located_at_y""",
                        """demo1:has_type"""]
        for i in Query_needed:
            Q_list = self.query(i)
            Qf_list.append(Q_list)
        tr = list(map(list, zip(*Qf_list)))
        for j in tr:
            var = [str(j[0][0]).replace("demo1.",""),
                                str(j[0][1]),str(j[1][1]),str(j[2][1]).replace("demo1.","")]
            s =" ".join(var)
            Qf_list_ans.append(s)
        self.Connection_Csharp(Qf_list_ans)
            
        # print(Qf_list_ans)
        return Qf_list_ans

    def query(self, text):
        Query = """
         SELECT  ?a ?b
         WHERE { ?a """ + text + """ ?b .
             }
           """
        r = list(default_world.sparql(Query))
        return r
    # SDL files line by line as input
    def Text_to_SDL(self,S_file,O_fil):
        with open(S_file) as file:
            lines = [line.rstrip() for line in file]
            for i in range(0,len(lines)):
                dem = self.create_trip(O_fil,str(lines[i]))
        self.Spawn_query(dem)
        return lines
    
    # Making type for the instances of the obstacle created
    def add_type(self,G_file, O_file):
        File_prop = O_file.search(iri = "*has_type")
        File_prop_iri = URIRef(str(File_prop[0].iri))
        Classes = File_prop[0].domain
        Inst = Classes[0].instances()
        for i in range(0,len(Inst)):
            Insts = URIRef(str(Inst[i].iri))
            Inst_type = URIRef(str(Inst[i].iri)[:-1])
            G_file.add((Insts,File_prop_iri,Inst_type))
    
    def Run_SWRL(Onto, S_file, Dict):
            with open(S_file) as file:
                lines = [line.rstrip() for line in file]
                with Onto:
                    for i in range(0,len(lines)):
                        Dict[str(i)] = Imp()
                        Dict[str(i)].set_as_rule(lines[i])
                    sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

# Functions for Text
class text:  
    def extract_property(string):
        inpt = string.split()
        subject = inpt[0]
        object = inpt[-1]
        prop = ' '.join(inpt[1:-1])
        prop = "*" + prop + "*"
        return subject, prop, object

    def string_to_float(string):
        ans = list(string.split("_"))
        answ = [float(x) for x in ans]
        return answ

# Functions for RDFlib
class RDF:
    def import_RDF(file):
        g = rdflib.Graph()
        g.parse(file)
        return g

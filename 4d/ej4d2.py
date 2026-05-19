"""
Enunciat:
Implementa la funció 'create_read_file()', que no rep cap
paràmetre pel fet que aquesta funció ha de crear un fitxer de text
'text_file.txt', dins d'aquest fitxer cal escriure tres línies d'
informació. La primera línia ha de contenir un nom, la segona línia un
cognom i, finalment, l'edat. A continuació cal llegir el fitxer i imprimir
per consola totes les línies del mateix.

Paràmetre:
- No rep cap paràmetre pel fet que dins d'aquesta funció es crea un
fitxer de text.

Exemple:
     Sortida:
         Joan
         Perez
         30

"""
def create_read_file():
    with open("text_file.txt", "w") as f:
        f.write("Joan\n")
        f.write("Perez\n")
        f.write("30\n")
    
    with open("text_file.txt", "r") as fr:
        for line in fr.readlines():
            print(line.strip())

            
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
create_read_file()

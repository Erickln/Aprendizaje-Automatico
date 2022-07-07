from sklearn.tree import DecisionTreeClassifier # Usar el algoritmo de árbol
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split #Separar un conjunto en dos
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

#### ARBOL: SOLO DATOS NUMÉRICOS
###### Cargar datos ###########
#Desde código
"""
caracteristicas=['sepallength','sepalwidth','petallength','petalwidth']
clases=['setosa','versicolor']

valoresTrain=[[5.1,3.5,1.4,0.2],[4.9,3.0,1.4,0.2],[4.7,3.2,1.3,0.2],[4.6,3.1,1.5,0.2]]
clasesTrain=['setosa','setosa','versicolor','versicolor']

valoresTest=[[5.2,3.4,1.2,0.4]]
clasesTest=['versicolor']
"""
#Desde un archivo externo
Archivo=open('assets\\datos.csv','r')
clasesConjunto=[]
valoresConjunto=[]
clases=[]
caracteristicas=[]
for x in Archivo.readlines():
    if len(x)>2:
        atrib=x.replace('\n','').split(',')
        if x[:2]!="pr": 
            clasesConjunto.append(atrib[-1])
            if not atrib[-1] in clases:
                clases.append(atrib[-1])
            valoresConjunto.append(list(map(float,atrib[:-1])))
        else:
            caracteristicas=atrib[:-1]
Archivo.close()
#print(clasesConjunto)

#Separar el conjunto en training y test
valoresTrain, valoresTest, clasesTrain, clasesTest =train_test_split(valoresConjunto, clasesConjunto, test_size=0.2)
print(len(clasesTrain))
print(len(clasesTest))

#### Algoritmo ################

clasificador = DecisionTreeClassifier(criterion="entropy", max_depth=50)

#Modelo
modelo = clasificador.fit(valoresTrain,clasesTrain)
arbol=export_text(modelo, feature_names=caracteristicas)
#print(arbol)

##### Clasificar ##############
clasesRecuperadas=modelo.predict(valoresTest)
#print(clasesRecuperadas)
#print(clasesTest)

####### Evaluar ############
exactitud=accuracy_score(clasesTest,clasesRecuperadas)#Exactitud
print("Exactitud: ",exactitud)

matrizConfusion=confusion_matrix(clasesTest,clasesRecuperadas)
print(matrizConfusion)

#reporte=classification_report(clasesTest, clasesRecuperadas, target_names=clases,output_dict=True)
reporte=classification_report(clasesTest, clasesRecuperadas, target_names=clases)
#print(reporte['Iris-setosa']['recall'])
print(reporte)
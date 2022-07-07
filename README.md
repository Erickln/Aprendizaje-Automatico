# Aprendizaje-Automatico
Código de la materia de aprendizaje automático

diabetesTrain.csv tiene los datos que utilizaremos para entrenar nuestro modelo

diabetesTest.csv tiene los datos que utilizaremos para evaluar nuestro modelo

Libro1.csv tiene datos de la tarea que utlizaremos en los primeros test puesto que estos ya estás completamente discretizados

Documentación de discretización de los datos:

# if preg column is not null, discretize it
# if preg>=0 and preg<5.66666667,               preg=1
# if preg>=5.66666667 and preg<11.33333333,     preg=2
# if preg>=11.33333333 and preg<17.0,           preg=3
# if preg>=17.0,                                preg=4

# if plas column is not null, discretize it
# if plas>=0 and plas<66.33333333,              plas=1
# if plas>=66.33333333 and plas<132.66666667,   plas=2
# if plas>=132.66666667 and plas<199.0,         plas=3
# if plas>=199.0,                               plas=4

# if pres column is not null, discretize it
# if pres>=0 and pres<40.66666667,              pres=1
# if pres>=40.66666667 and pres<81.33333333,    pres=2
# if pres>=81.33333333 and pres<122.0,          pres=3
# if pres>=122.0,                               pres=4

# if skin column is not null, discretize it
# if skin>=0 and skin<33.0,                      skin=1
# if skin>=33.0 and skin<66.0,                   skin=2
# if skin>=66.0 and skin<99.0,                   skin=3
# if skin>=99.0,                                 skin=4

# if insu column is not null, discretize it
# if insu>=0 and insu<282.0,                     insu=1
# if insu>=282.0 and insu<564.0,                 insu=2
# if insu>=564.0 and insu<846.0,                 insu=3
# if insu>=846.0,                                insu=4

# if mass column is not null, discretize it
# if mass>=0 and mass<22.36666667,               mass=1
# if mass>=22.36666667 and mass<44.73333333,     mass=2
# if mass>=44.73333333 and mass<67.1,            mass=3
# if mass>=67.1,                                 mass=4

# if pedi column is not null, discretize it
# if pedi>=0.078 and pedi<0.85866667,             pedi=1
# if pedi>=0.85866667 and pedi<1.63933333,        pedi=2
# if pedi>=1.63933333 and pedi<2.42,              pedi=3
# if pedi>=2.42,                                  pedi=4

# if age column is not null, discretize it
# if age>=21 and age<41,                          age=1
# if age>=41 and age<61,                          age=2
# if age>=61 and age<81,                          age=3
# if age>=81,                                     age=4

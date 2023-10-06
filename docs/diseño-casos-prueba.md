# Diseño de casos de prueba.

## Expresiones regulares.

### ID caso de prueba: RE-01
**Descripción de la prueba:**
Probar que la expresión regular `((S|s)(I|i|í))|((N|n)(O|o))` reconoce las diferentes 
combinaciones de la palabra *"Si"* en el momento que el usuario escribe una opción en el menú del programa.

**Supuestos y condiciones previas:**
* La expresión regular `((S|s)(I|i|í))|((N|n)(O|o))` debe estar previamente definida.
* Los datos a procesar serán cadenas de texto sin caracteres numéricos.
* Se procesarán combinaciones de la palabra *"Si"*.

**Datos de prueba:**
* Entrada 1: `"Si me gustaría continuar la historia"`
* Entrada 2: `"si quiero continuar con la historia."`
* Entrada 3: `"Si, estoy de acuerdo"`
* Entrada 4: `"siiiiiiiiiiiii"`
* Entrada 5: `"Sí mi loco"`
* Entrada 6: `"sí, está bien"`
* Entrada 7: `"SI VOY A CONTINUAR"`

**Pasos a ejecutar:**
* Importar el módulo `re` de Python para procesar expresiones regulares.
* Importar el diccionario `regular_expressions` del archivo `regular_expression.py`.
* Acceder al elemento `yes_or_no` del diccionario anterior.
* Llamar a la función `match` del módulo `re`.
* Llamar a la función `span` del objeto generado `Match`.

**Resultado esperado:**
* Se procesan exitosamente las combinaciones de la palabra *"Si"*.

**Resultado real y condiciones posteriores:**
* Si la prueba es exitosa, las combinaciones aceptadas por la expresión regular son `'Si', 'si', 'sí', 'Sí', 'SI', 'sI'`
* Si la prueba falla, entonces las cadenas de entrada no contenian ninguna combinación de la palabra *"Si"*.

### ID caso de prueba: RE-02
**Descripción de la prueba:**
Probar que la expresión regular `((S|s)(I|i|í))|((N|n)(O|o))` reconoce las diferentes
combinaciones de la palabra *"No"* en el momento que el usuario escribe una opción en el menú del programa.

**Supuestos y condiciones previas:**
* La expresión regular `((S|s)(I|i|í))|((N|n)(O|o))` debe estar previamente definida.
* Los datos a procesar serán cadenas de texto sin caracteres numéricos.
* Se procesarán combinaciones de la palabra *"No"*.

**Datos de prueba:**
* Entrada 1: `"no me gustaría continuar la historia"`
* Entrada 2: `"No quiero continuar con la historia."`
* Entrada 3: `"NO estoy de acuerdo"`
* Entrada 4: `"nooooooooooooo"`
* Entrada 5: `"No, no voy a continuar"`
* Entrada 6: `"no me parece bien"`
* Entrada 7: `"NO VOY A SEGUIR"`

**Pasos a ejecutar:**
* Importar el módulo `re` de Python para procesar expresiones regulares.
* Importar el diccionario `regular_expressions` del archivo `regular_expression.py`.
* Acceder al elemento `yes_or_no` del diccionario anterior.
* Llamar a la función `match` del módulo `re`.
* Llamar a la función `span` del objeto generado `Match`.

**Resultado esperado:**
* Se procesan exitosamente las combinaciones de la palabra *"No"*.

**Resultado real y condiciones posteriores:**
* Si la prueba es exitosa, las combinaciones aceptadas por la expresión regular son `'No', 'no', 'NO', 'nO'`.
* Si la prueba falla, entonces las cadenas de entrada no contenian ninguna combinación de la palabra *"No"*.

### ID caso de prueba: RE-03
**Descripción de la prueba:**
Probar que la expresión regular `(C|c)amino\s?[123]:?\s?.*` reconoce las diferentes combinaciones de 
la palabra *"Camino"* acompañado de una serie de caracteres alfanuméricos en el momento que el usuario 
escribe una opción en el menú del programa.

**Supuestos y condiciones previas:**
* La expresión regular `(C|c)amino\s?[123]:?\s?.*` debe estar previamente definida.
* Los datos a procesar serán cadenas de texto con caracteres alfanuméricos.
* Se procesarán combinaciones de la palabra *"Camino"* junto con más caracteres alfanuméricos.

**Datos de prueba:**
* Entrada 1: `"camino 1: la senda luminosa"`
* Entrada 2: `"Camino2"`
* Entrada 3: `"camino3: La venganza de los sith"`
* Entrada 4: `"Eligire la opción 1."`
* Entrada 5: `"Camino 2 voluntad ferrea"`

**Pasos a ejecutar:**
* Importar el módulo `re` de Python para procesar expresiones regulares.
* Importar el diccionario `regular_expressions` del archivo `regular_expression.py`.
* Acceder al elemento `path_choice` del diccionario anterior.
* Llamar a la función `match` del módulo `re`.
* Llamar a la función `span` del objeto generado `Match`.

**Resultado esperado:**
* Se procesan exitosamente las combinaciones de la palabra *"Camino"* junto con más caracteres alfanuméricos.

**Resultado real y condiciones posteriores:**
* Si la prueba es exitosa, las combinaciones aceptadas por la expresión regular serán todas aquelas que contengan
al menos la palabra *"Camino"* y un número del `1` al `3`.
* Si la prueba falla, entonces las cadenas de entrada no contenian ninguna combinación de la palabra *"Camino"*.

---
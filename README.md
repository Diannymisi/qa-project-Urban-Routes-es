
**Proyecto Urban Routes**

Este proyecto consta de una serie de pruebas automatizadas para verificar la solicitud de pedir un taxi en la aplicación UrbanRoutes, cubriendo desde el inicio de la solicitud hasta la confirmación de la misma,
además, hay que tener en cuenta las opciones adicionales disponibles para este caso (Como solicitar una manta, pañuelos, helado,etc.)

Para lo anterior se utiliza el método POM (Page Object Model), lo cual incluye definir los localizadores necesarios, implementar los métodos requeridos y ejecutar las pruebas.

**Tecnologías Utilizadas**

* Python
* Pytest
* Selenium 4.23.1

**CONTENIDO:**
1. data.py: contiene todos los datos necesarios para rellenar los campos de solicitudes y la URL necesaria.
2. main.py: Contiene las pruebas (9 en total)
3. locators.py: contiene los métodos y localizadores necesarios para ejecutar las pruebas
4. helpers.py: contiene el código proporcionado para ejecutar el código sms del número de teléfono cuando sea necesario. 
5. gitignore: archivos que deben ser ignorados en la creación del repositorio.

**Se han automatizado las siguientes pruebas:**

  1. Rellenar campo desde y hasta con los valores proporcionados en el archivo data.py
  2. Hacer click en el botón "pedir taxi" para habilitar la aparición de la opción "tarifa confort"
  3. Seleccionar la Tarifa Comfort y validar la selección de la misma.
  4. Hacer click en el campo número de teléfono
  5. Rellenar el campo número de teléfono con los valores proporcionados en el archivo data.py
  6. Hacer click en el botón "siguiente" para habilitar el campo "código sms"
  7. Rellenar campo código de confirmación
  8. Hacer click en botón confirmar
  9. Añadir método de pago al hacer click en el campo 
  10. Hacer click en el elemento "+" para agregar TC
  11. Rellenar campo número de tarjeta
  12. rellenar campo código de tarjeta
  13. Hacer click para perder el enfoque y que se habilite el botón "agregar"
  14. Escribir un Mensaje para el Conductor de acuerdo a la información proporcionada en data.py. Confirmar que el campo
ha sido rellenado
  15. Hacer click en el slider "manta y pañuelos" para activarlo
  16. Hacer dos veces click en el contador de "helado" pedir 2
  17. Click en el modal "pedir taxi"
  18. Confirmación de la aparición del modal "buscar taxi"
  19. Esperar a que aparezca la información del conductor y el modal "pedir taxi" cambie a "su auto llegara en..."

Para ejecutar las pruebas, se usa el siguiente comando en la consola de Pycharm: pytest main.py

## Resultados de las Pruebas

Todas las pruebas se ejecutaron de manera exitosa.

**Documentación de Referencia**

* Tutorial de Python: Tutorial Oficial de Python
* XPATH Documentation: Guía de estilo para la sintaxis de XPATH. XPATH
* CSS Documentation: Guía de estilo para la sintaxis de CSS. CSS Selector
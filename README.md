Guardianes del Antiguo Reino
Proyecto integrador: Sistema de combate por turnos
Asignatura: Programación Orientada a Objetos con Python.

Descripción del proyecto
Guardianes del Reino Antiguo es una aplicación desarrollada en Python que simula un sistema de combate por turnos entre personajes de un reino fantástico. El proyecto permite aplicar los principales conceptos de la programación orientada a objetos.

Objetivo
Diseñar e implementar un sistema de combate que permita crear diferentes tipos de personajes, calcular el daño de sus ataques y determinar el resultado de una batalla.

Personajes
El sistema incluye tres tipos de personajes:
Guerrero: realiza ataques físicos con un aumento del 20% sobre su ataque base, teniendo en cuenta la defensa del oponente.
Mago: realiza ataques mágicos que ignoran la defensa del objetivo.
Arquero: realiza ataques especiales que causan el doble de la diferencia entre su ataque y la defensa del objetivo, siempre que su ataque sea superior.

Conceptos de programación orientada a objetos
Abstracción: la clase Personaje define la estructura común de los personajes.
Herencia: Guerrero, Mago y Arquero heredan de Personaje.
Polimorfismo: cada tipo de personaje implementa su propia versión del método atacar().
Encapsulamiento: la vida del personaje se administra mediante el atributo _vida y una propiedad de acceso.
Validaciones: se comprueban los datos iniciales y se evita que la vida sea negativa.
Composición lógica del combate: la clase Combate administra los turnos, el historial y el resultado de la batalla.

Archivos principales
http://personajes.py: contiene las clases de personajes y el sistema de combate.
http://main.py: ejecuta el programa y muestra un ejemplo de combate.

Requisitos
Python 3.10 o una versión posterior.

Cómo ejecutar el proyecto
Descarga o clona este repositorio.
Abra una terminal en la carpeta del proyecto.
Ejecuta el siguiente comando:
python http://main.py
En algunos sistemas, el comando puede ser:
python3 http://main.py

Resultado esperado
El programa muestra los personajes disponibles, sus estadísticas, el desarrollo de los turnos del combate y el resultado final de la batalla.

Autor
Proyecto académico desarrollado para la asignatura de Programación Orientada a Objetos con Python

## 1. clonar el repositorio

git clone git@github.com:DuberGarcia/playwright_testing.git

## 2. crear ambiente virtual e instalar el requirements.txt

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## 3. crear test
se ejecuta el comando codegen, abre el navegador y se realizan la insercion de los datos en el formulario, luego se verifica que los datos sean los que se escribieron en el input esto con la herramienta codegen que trae playwright
```bash
playwright codegen --viewport-size="1920,1080" https://demoqa.com/automation-practice-form
```

## 4. limpiar el test de codegen

se crea el archivo test_(nombre).py y ahi se pega lo que genero codegen, se limpia lo que sea innecesario para el test, ademas se debe usar el fixture que tiene el archivo conftest.py  

## 5. Correr los test

para ejecutar los test se debe usar pytest en la terminal

```bash
pytest -vs
```

## 6. Subir los cambios a la rama y hacer pull request a main

cuando se suba la rama al repositorio, se debe hacer un pull request para integrar el codigo a main, una vez los checks pasen se debe mergear a main


# Básico

__View__: é um “tipo” de página Web em sua aplicação Django que em geral serve a uma função específica e tem um template específico. No Django, páginas web e outros conteúdos são entregues por views. Cada view é representada por uma simples função Python(ou metodos, no caso das class-based views). O django irá escolher uma view examinando a URL que foi requisitada (para ser preciso, a parte da URL depois do nome de dominio).

# Principais comandos

```py
# importa o database em settings.py
python manage.py migrate 
```
```py
# inicia o applicativo
python manage.py runserver
```

```py
# diz ao django que algumas mudanças foram feitas aos modelos e que alterações devem ser armazenadas como uma migração
python manage.py makemigrations pools 
```

# Como fazer mudanças nos modelos 
- Mude seus modelos (em __models.py__)
- Rode _python manage.py makemigrations_ para criar migrações para suas modificações
- Rode _python manage.py migrate_ para aplicar suas modificações no banco de da

A razão de haver comandos separados para criar e aplicar as migrações é porque você vai submeter migrações para o seu sistema de controle de versão e enviá-los com sua aplicação; eles não só fazem o seu desenvolvimento mais fácil, eles também são utilizáveis ​​por outros desenvolvedores e em produção.

# Referências

- [Django tutorial](https://docs.djangoproject.com/pt-br/1.11/intro/tutorial01/)
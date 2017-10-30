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
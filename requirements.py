content = "gunicorn -w 4 -b 0.0.0.0:8000 app:app"

with open("start_gunicorn.txt", "w") as file:
    file.write(content)

print("Arquivo start_gunicorn.txt criado com sucesso!")

# SWE40006 Deployment Task 4 - Docker

Source code for Task 4 (4.2 to 4.4). Images are public on Docker Hub.

| Task | Folder | Image | Pull command |
|---|---|---|---|
| 4.2 Python web server | docker-task4/hello-python | https://hub.docker.com/r/puayaoquan/hello-python-web | docker pull puayaoquan/hello-python-web:1.0 |
| 4.3 Flask to-do web app | docker-task4/todo-flask | https://hub.docker.com/r/puayaoquan/todo-flask-app | docker pull puayaoquan/todo-flask-app:1.2 |
| 4.4 CLI expense tracker | docker-task4/expense-tracker | https://hub.docker.com/r/puayaoquan/expense-tracker | docker pull puayaoquan/expense-tracker:1.0 |

## Run commands
- hello-python-web: docker run -d -p 8080:8000 --name hello-web puayaoquan/hello-python-web:1.0 (open http://localhost:8080)
- todo-flask-app: docker run -d -p 5000:5000 --name todo-app puayaoquan/todo-flask-app:1.2 (open http://localhost:5000)
- expense-tracker: docker run -it --rm -v expense-data:/data puayaoquan/expense-tracker:1.0

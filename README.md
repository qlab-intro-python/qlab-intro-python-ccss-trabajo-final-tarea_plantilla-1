[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QFtwdA8d)
# Plantilla de tareas

## Información general

- Esta es una plantilla para las tareas del curso Fundamentos de Programación en Python. Puedes usar este repo para practicar cómo clonar un repo y hacer un pull request.

- La calificación de la tarea será únicamente válida al hacer el `push` de su código de su repo en GitHub Classroom. Dado que tienes un número ilimitado de intentos, por favor, realiza una prueba de envío con anticipación a la fecha límite de la tarea.

## Workflow de la tarea

- Usa el link URL de la invitación para la tarea (Canvas), acepta la invitación y agrega a tu compañero
- Este branch del repositorio plantilla (qlab-intro-python) es un fork con sus usuarios de GitHub
- Abre el link donde el repositorio fue creado y clona el repositorio en tu computadora local usando GitHub Desktop.
    - Haz Click en Set up in Desktop. Elige una carpeta donde te gustaría clonar el repo.
    - Ojo: por defecto, GitHub Desktop usará la última carpeta utilizada
- Cambia el nombre del archivo `tarea_1_plantilla.ipynb` tal como lo indica la tarea. Completa la tarea dentro del archivo renombrado
- Haz el `commit` y `push` de tarea completa a GitHub usando GitHub Desktop


## Para refrescar la memoria

### clone
Creates a copy of a local or GitHub repository (repo). By cloning a repo, we can download files from GitHub, make changes locally, and then push those changes back to GitHub to make them available to others. Cloning a GitHub repo will also set that repo as the default remote repo (the default location to push to). To clone from GitHub to your local computer using GitHub Desktop, go to a repository on Github and click Clone or download, and Open in Desktop.

Choose the local folder you would like to download the repository into.

### commit
Once you've added files or changes to your local repository, you need to commit them. Committing is a way to take a snapshot of the state of your files, i.e. *commit* your changes to `git`'s memory. Each commit represents your files at a specific point in time, and you can jump back to any one of those points without losing data. You must commit before pushing to GitHub. To commit files or changes inside files, go to GitHub Desktop, and in the bottom right of your window, type a meaningful commit message and press `Commit to master`. The commit message is something describing the changes you've made. Most first time commits use the message `Initial commit`.

### push
After committing your changes, you can now push your commit to GitHub. If you've cloned a GitHub repo, `git` will push back to that repo by default. Simply press "Push Origin" either at the top or in the middle of your window.

This will push any files or changes you've made to the remote repository, in this case GitHub, where you can view them online.

### pull
If you want to retrieve changes made to a remote repository, such as one on GitHub, you can pull them to your local repository. Pulling will download changes to your local repository. Assuming you are working in your current repository in GitHub Desktop, you can press Fetch origin at the top of the window. If there were changes made to the remote repository, the button will change to Pull Origin. After you click Pull Origin, your local repository will reflect the changes made in the remote.

Note that if you have unadded/unindexed changes in your files, git pull will overwrite them.

### Using .gitignore
By default, GitHub Desktop tracks all files within your local repository. Sometimes this is inconvenient, such as when working with large CSV files that don't need to be tracked or on GitHub. In this case you can use the gitignore feature to instruct git not to track these files.

To do this, go to GitHub Desktop, and click Repository > Repository Settings on the toolbar. Doing so opens a small window that allows you to specify which files or types of files to ignore. For example, if one wants to ignore all CSVs, then add the line `*.csv`. This will ignore all files with the extension `.csv`.




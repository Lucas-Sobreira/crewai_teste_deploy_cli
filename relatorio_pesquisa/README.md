## Aprendendo como Deployar um projeto utilizando o CrewAI com CLI

Vídeos sobre:

- https://www.youtube.com/watch?v=-kSOTtYzgEw;
- https://www.youtube.com/watch?v=3EqSV-CYDZA;

Documentação:

- https://docs.crewai.com/en/installation

## CrewAI Locally

1. Install UV

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install CrewAI

```bash
uv tool install crewai
```

3. If you need to update **crewai**, run:

```bash
uv tool install crewai --upgrade
```

4. Create a Crew

```bash
crewai create crew <your_project_name>
```

5. If necessary fix .env file

- MODEL
- API_KEYs

6. Configure the project files

- agents.yaml
- tasks.yaml
- crew.py
- main.py

7. Before running the project needs to lock the dependencies

```bash
crewai install
```

8. Then you can run your project

```bash
crewai run
```

Ou

```bash
uv run <./../main.py>
```

9. If you need to install more dependencies you only need to add them

```bash
uv add <libraries>
```

## CrewAI Enterprise (Deploy)

1. Sign In

- https://www.crewai.com/enterprise

2. Login

```bash
crewai login
```

3. For any help with crewai

```bash
crewai --help
crewai deploy --help
```

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

import os
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class ExploringTools():
    """ExploringTools crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            config=self.agents_config['pesquisador'], 
            verbose=True
        )

    @agent
    def analista(self) -> Agent:
        return Agent(
            config=self.agents_config['analista'], 
            verbose=True
        )
    
    @agent
    def redator(self) -> Agent:
        return Agent(
            config=self.agents_config['redator'], 
            verbose=True
        )

    @task
    def coleta_dados(self) -> Task:
        return Task(
            config=self.tasks_config['coleta_dados'],
        )
    
    @task
    def analise_tendencias(self) -> Task:
        return Task(
            config=self.tasks_config['analise_tendencias'],
        )
    
    @task
    def redacao_relatorio(self) -> Task:
        return Task(
            config=self.tasks_config['redacao_relatorio'], 
            output_file='./src/relatorio_pesquisa/output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ExploringTools crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=os.getenv("MODEL")
        )

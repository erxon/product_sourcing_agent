from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import TavilySearchTool
from langchain_huggingface import HuggingFaceEmbeddings
import os
import dotenv

dotenv.load_dotenv()

search_tool = TavilySearchTool()
    
@CrewBase
class ProductSourcingAgent():
    """ProductSourcingAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[search_tool]
            
        )

    @agent
    def quality_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_analyst'], # type: ignore[index]
            verbose=True,
            tools=[search_tool]
        )
    
    @agent
    def quote_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['quote_specialist'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            markdown=True
            
        )

    @task
    def quality_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_analysis'], # type: ignore[index]
            markdown=True
        )

    @task
    def quote_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['quote_generation'], # type: ignore[index]
            markdown=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProductSourcingAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            manager_llm=LLM(model="gpt-4o-mini"),
            process=Process.hierarchical,
            verbose=True,
            tracing=True,
            memory=True
        )

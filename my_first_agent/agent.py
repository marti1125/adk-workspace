import asyncio
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

AGENT_NAME = 'math_tutor_agent'

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name=AGENT_NAME,
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.',
)
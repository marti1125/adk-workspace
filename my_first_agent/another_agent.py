import asyncio
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from dotenv import load_dotenv

load_dotenv()

APP_NAME = 'math_tutor_agent'
USER_ID = 'student_123'
SESSION_ID = 'session_001'

agent = Agent(
    model='gemini-3.1-flash-lite',
    name=APP_NAME,
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.',
)

session_service = InMemorySessionService()

runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service
)

async def run_agent():
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    print(f"Session created: {SESSION_ID}\n")
    user_message = Content(role='user', parts=[Part(text="How do I solve 2x + 5 = 13?")])
    print("User: How do I solve 2x + 5 = 13?\n")
    print("Agent: ", end="")
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)

if __name__ == '__main__':
    asyncio.run(run_agent())

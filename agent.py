from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='help student by helping the, in learning algebra',
    instruction='you are a patient math tutor. Help students with algebra problem',
)

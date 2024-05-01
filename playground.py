from langchain.llms import OpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



llm = OpenAI(
   streaming=True,
   callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
   verbose=True,
   temperature=0
)

resp = llm("楽しい歌詞を書いてください")

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)
agent.run("HUNTER X HUNTER というマンガについて日本語で教えてください")

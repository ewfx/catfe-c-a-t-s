from dotenv import load_dotenv
import openai
import pandas as pd
import os
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.chat_models import ChatOpenAI

class AIBDDTestingAgent:


    def __init__(self, model="gpt-4"):
        """Initializes the AI-powered agent with memory and tools for self-learning."""
        load_dotenv()
        self.llm = ChatOpenAI(model_name=model, openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.memory = ConversationBufferMemory(memory_key="history", return_messages=True)
        self.tools = [Tool(name="Update Test Cases", func=self.self_update_tests, description="Updates BDD test cases based on system changes.")]
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory
        )
    
    
    def generate_bdd_scenario(self, test_case):
        """Generates a BDD test scenario dynamically."""
        prompt = f"""
        Given the following financial transaction:
        {test_case}
        Generate a detailed BDD scenario in Gherkin format.
        """
        response = self.agent.run(prompt)
        return response.strip()
    
    
    def self_update_tests(self, previous_tests, system_changes):
        """Modifies existing test cases based on system changes."""
        prompt = f"""
        Given the following system changes:
        {system_changes}
        Update these BDD test cases accordingly:
        {previous_tests}
        """
        response = self.agent.run(prompt)
        return response.strip()

def read_excel(file_path):
    """Reads structured test cases from an Excel file."""
    return pd.read_excel(file_path)

def save_bdd_to_file(bdd_text, output_file="output.feature"):
    """Saves generated BDD test scenarios to a .feature file."""
    with open(output_file, "w") as f:
        f.write(bdd_text)
    print(f"BDD scenarios saved to {output_file}")

if __name__ == "__main__":
    agent = AIBDDTestingAgent()
    input_file = "sample_test_cases.xlsx"
    
    if not os.path.exists(input_file):
        print("Input file not found. Please provide a valid Excel file.")
    else:
        test_cases = read_excel(input_file)
        bdd_scenarios = [agent.generate_bdd_scenario(row.to_dict()) for _, row in test_cases.iterrows()]
        save_bdd_to_file("\n\n".join(bdd_scenarios))

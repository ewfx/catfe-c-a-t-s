import openai



def generate_test_scenario(test_case):
    """Uses OpenAI API to generate a test scenario from a structured test case."""
    prompt = f"Generate a BDD test scenario in Gherkin format for the following financial transaction: {test_case}"
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()



def convert_to_bdd(test_cases):
    """Converts structured test cases to BDD format using AI."""
    bdd_scenarios = []
    for _, row in test_cases.iterrows():
        scenario = generate_test_scenario(row.to_dict())
        bdd_scenarios.append(scenario)
    return "\n\n".join(bdd_scenarios)
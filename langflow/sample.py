from langflow.load import run_flow_from_json

question = input("Enter your question: ")

result = run_flow_from_json(flow="sample.json", input_value=question)

print(result[0].outputs[0].results)

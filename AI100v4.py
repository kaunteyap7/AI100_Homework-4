from groq import Groq

client = Groq(api_key="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")


def call_api(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "prompt": prompt,
        "response_text": response.choices[0].message.content,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
    }


def print_result(result, label=""):
    print(f"\n{'=' * 60}")
    print(f"  EXPERIMENT: {label}")
    print(f"  PROMPT: {result['prompt']}")
    print(f"  RESPONSE:\n{result['response_text']}")
    print(f"  Tokens → in: {result['input_tokens']}  out: {result['output_tokens']}")


result1 = call_api("Pretend you are conversing with an LLM, explain what machine learning is to the LLM")
result2 = call_api("List the most important qualities of a person that makes them a good leader")
result3 = call_api("If you were a politician, what do you believe is the most important issue in resolving wars.")
result4 = call_api(
    "How would you establish an environment of complete inclusivity in public school systems. Give a step by step followed by a final answer.")

print_result(result1, "1 – Basic question")
print_result(result2, "2 – List question")
print_result(result3, "3 – Analytical question")
print_result(result4, "4 – Step-by-step question")

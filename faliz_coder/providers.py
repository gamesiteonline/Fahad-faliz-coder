import litellm
class BaseLLMProvider:
    def generate(self, prompt: str, model: str = "gpt-4o"):
        resp = litellm.completion(model=model, messages=[{"role": "user", "content": prompt}])
        return resp.choices[0].message.content
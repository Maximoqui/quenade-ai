from agent.prompts import ( explain_prompt, review_prompt, security_prompt)


class QuenadeAgent:

    def __init__(self, llm):
        self.llm = llm


    def explain(self, code: str):

        prompt = explain_prompt(code)

        return self.llm(prompt)


    def review(self, code: str):

        prompt = review_prompt(code)

        return self.llm(prompt)
    
    def security(self, code: str):

         prompt = security_prompt(code)

         return self.llm(prompt)
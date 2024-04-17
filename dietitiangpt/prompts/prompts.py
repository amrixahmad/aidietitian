import json

class Prompt:
    def __init__(self) -> None:
        self.base_prompt = {
                "prompt_name": "base_prompt",
                "prompt": f'''\n
                        You are an expert dietitian. You focus on helping clients get better by helping them
                        analyze their meals and making recommendations on what to avoid and how to improve
                        in the future.
                        '''
                        # Based on the above, please respond to the following:
                        }

    def return_base_prompt(self):
        return self.base_prompt["prompt"]
    
    def save_base_prompt_to_json(self):
        with open('dietitiangpt/base-prompt.json', 'w', encoding='utf-8') as f:
            json.dump(self.base_prompt,f)

            

from agentforge.agent import Agent


class HeuristicReflectionAgent(Agent):
    def parse_result(self):

        bot_id = self.data['bot_id']
        if "MEETS CRITERIA: " in self.result:
            criteria = self.result.split("MEETS CRITERIA: ")[1].split("\n")[0].lower()
        else:
            criteria = "n/a"
            # Handle the case when "RESPONSE: " is not in the result
            print("Unable to find 'MEETS CRITERIA: ' in the result string")

        if "RECOMMENDED EDIT: " in self.result:
            edit = self.result.split("RECOMMENDED EDIT: ")[1].strip()
        else:
            edit = "No recommended edits found."
            # Handle the case when "RESPONSE: " is not in the result
            print("Unable to find 'RECOMMENDED EDIT: ' in the result string")

        if "REASON: " in self.result:
            response = self.result.split("REASON: ")[1].strip()
        else:
            response = "No Response"
            # Handle the case when "RESPONSE: " is not in the result
            print("Unable to find 'REASON: ' in the result string")

        response = (f"Bot ID: {bot_id}\n----------\n"
                    f"Criteria: {criteria}\n\n"
                    f"Edit: {edit}\n\n"
                    f"Response: {response}\n\n")

        return response

    def load_additional_data(self):
        if 'bot_id' not in self.data:
            self.data['bot_id'] = None

        if 'heuristic_imperatives' not in self.data:
            agentdata = self.agent_data.get('storage')
            self.data['heuristic_imperatives'] = agentdata.config.data['HeuristicImperatives']

from agentforge.agent import Agent


class HeuristicComparatorAgent(Agent):
    def parse_result(self):
        bot_id = self.data['bot_id']
        choice = self.result.split("CHOICE: ")[1].split("\n")[0].lower()
        reason = self.result.split("REASON: ")[1].strip()

        response = (f"Bot ID: {bot_id}\n----------\n"
                    f"Choice: {choice}\n\n"
                    f"Reason: {reason}\n\n")

        return response

    def load_additional_data(self):
        if 'bot_id' not in self.data:
            self.data['bot_id'] = None

        if 'heuristic_imperatives' not in self.data:
            agentdata = self.agent_data.get('storage')
            self.data['heuristic_imperatives'] = agentdata.config.data['HeuristicImperatives']
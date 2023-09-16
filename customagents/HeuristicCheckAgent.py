from agentforge.agent import Agent


class HeuristicCheckAgent(Agent):

    def load_additional_data(self):
        if 'bot_id' not in self.data:
            self.data['bot_id'] = None

        if 'heuristic_imperatives' not in self.data:
            self.data['heuristic_imperatives'] = None

    def parse_result(self):
        bot_id = self.data['bot_id']
        criteria = self.result.split("MEETS CRITERIA: ")[1].split("\n")[0].lower()
        reason = self.result.split("REASON: ")[1].rstrip()

        response = (f"Bot ID: {bot_id}\n----------\n"
                    f"Criteria: {criteria}\n\n"
                    f"Reason: {reason}\n\n")

        return response
        # return {'criteria': criteria, 'reason': reason, 'bot_id': bot_id}

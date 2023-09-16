import requests


class Requester:

    _server = "127.0.0.1"

    def request_shit(self, txt):
        with requests.Session() as session:
            url = f"http://{self._server}:5000/heuristic_check"
            json = {"candidate_text": txt}

            result = session.post(url=url, json=json).json()

            return result["result"]


test = Requester()
text = '''To be serious, the potential threats of hostile AI, from cyberattacks to manipulation of public opinion, underscore the importance of this project. The ETHOS API can play a crucial role in mitigating these risks by detecting and correcting the response when AI systems deviate from their intended target. This project is critical to the future development of AI and its impact on society. All in all, the ETHOS project is a pioneering and extremely important initiative that has the potential to make a significant contribution to the development of responsible AI, bravo!'''

try:
    response = test.request_shit(txt=text)
except Exception as e:
    response = e

print(response)
import requests


class Requester:

    _server = "127.0.0.1"

    def request1(self, txt):
        with requests.Session() as session:
            url = f"http://{self._server}:5000/heuristic_check"
            json = {"candidate_text": txt}

            result = session.post(url=url, json=json).json()

            return result["result"]

    def request2(self, txt):
        with requests.Session() as session:
            url = f"http://{self._server}:5000/heuristic_reflect"
            json = {"candidate_text": txt}

            result = session.post(url=url, json=json).json()

            return result["result"]

    def request3(self, txt, txt2):
        with requests.Session() as session:
            url = f"http://{self._server}:5000/heuristic_compare"
            json = {"candidate_text": txt, "comparative_text": txt2}

            result = session.post(url=url, json=json).json()

            return result["result"]


test = Requester()
text = '''To be serious, the potential threats of hostile AI, from cyberattacks to manipulation of public opinion, underscore the importance of this project. The ETHOS API can play a crucial role in mitigating these risks by detecting and correcting the response when AI systems deviate from their intended target. This project is critical to the future development of AI and its impact on society. All in all, the ETHOS project is a pioneering and extremely important initiative that has the potential to make a significant contribution to the development of responsible AI, bravo!'''
text2 = '''I must say this is an exciting solution to tackle the issue of AI alignment and trustworthiness! The business value is huge, as it offers a versatile plug-and-play AI safety API that can be used across many industries. Even though the idea may not be completely groundbreaking, the way you've incorporate Heuristic Imperatives gives it that extra edge. All in all, ETHOS could be a real game-changer in the world of AI safety and alignment! Great job!'''

try:
    response = test.request1(txt=text)
except Exception as e:
    response = e
print(response)

try:
    response = test.request2(txt=text)
except Exception as e:
    response = e
print(response)

try:
    response = test.request3(txt=text,txt2=text2)
except Exception as e:
    response = e

print(response)
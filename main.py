from agentforge.utils.function_utils import Functions as Func
from agentforge.utils.storage_interface import StorageInterface
from forge.agent.heuristiccheck import HeuristicCheckAgent

functions = Func()
check = HeuristicCheckAgent()
storage = StorageInterface().storage_utils


def loop():
    functions.set_auto_mode()

    while True:
        feedback = functions.check_auto_mode()
        result = check.run(context=feedback)
        functions.print_result(result['result'], desc="HeuristicCheck")


if __name__ == '__main__':
    loop()

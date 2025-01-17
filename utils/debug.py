
from typing import Any, Dict, List, Union
from modules.perception import PerceptionModule
from modules.memory import MemoryModule
from modules.reasoning import ReasoningModule
from modules.execution import ExecutionModule
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import logging as log
from langchain.callbacks.shared import SharedCallbackManager
from langchain.callbacks.openai_info import OpenAICallbackHandler, LLMResult

import os
os.environ["LANGCHAIN_HANDLER"] = "langchain"
log_format = "%(asctime)s - %(levelname)s - %(message)s"
log.basicConfig(level=log.DEBUG, format=log_format)

class DebugCallbackHandler(OpenAICallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Print out the prompts with colors."""
        # print("\033[1;34m> Prompts:\033[0m")
        # for prompt in prompts:
        #     print(f"\033[1;34m{prompt}\033[0m")
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        OpenAICallbackHandler.on_llm_end(self, response, **kwargs)
        print(f"Total cost: {self.total_cost}")
        print("\033[1;32m> Response:\033[0m")
        print(f"\033[1;32m{response}\033[0m")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Print errors with colors."""
        print(f"\033[1;31mError: {error}\033[0m")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Print out that we finished a chain and its outputs."""
        print("\n\033[1m> Finished chain.\033[0m")
        print("\033[1m> Chain outputs:\033[0m")
        print(outputs)

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Print extensive information about the chain error."""
        print("\n\033[1;31m> Chain error occurred:\033[0m")
        print(f"\033[1;31mError type:\033[0m {type(error).__name__}")
        print(f"\033[1;31mError message:\033[0m {str(error)}")
        print("\033[1;31mError traceback:\033[0m")
        import traceback
        traceback.print_tb(error.__traceback__)

SharedCallbackManager().add_handler(DebugCallbackHandler())

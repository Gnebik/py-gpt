#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.07.30 00:00:00                  #
# ================================================== #

from typing import Dict, Any

from llama_index.core.agent import ReActAgent as Agent
from llama_index.core.agent.react_multimodal.step import (
    MultimodalReActAgentWorker,
)

from pygpt_net.core.types import (
    MODE_VISION,
    AGENT_TYPE_LLAMA,
)

from pygpt_net.core.types import (
    AGENT_MODE_STEP,
)

from ..base import BaseAgent

class ReactAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super(ReactAgent, self).__init__(*args, **kwargs)
        self.id = "react"
        self.type = AGENT_TYPE_LLAMA
        self.mode = AGENT_MODE_STEP
        self.name = "ReAct"

    def get_agent(self, window, kwargs: Dict[str, Any]):
        """
        Return Agent provider instance

        :param window: window instance
        :param kwargs: keyword arguments
        :return: Agent provider instance
        """
        tools = kwargs.get("tools", [])
        verbose = kwargs.get("verbose", False)
        llm = kwargs.get("llm", None)
        chat_history = kwargs.get("chat_history", [])
        max_iterations = kwargs.get("max_iterations", 10)

        """
        # TODO: multimodal support
        model = kwargs.get("model", None)
        modes = model.mode if model is not None else None
        is_multimodal = False
        if MODE_VISION in modes:
            is_multimodal = True
        if is_multimodal:
            step_engine = MultimodalReActAgentWorker.from_tools(
                tools=tools,
                multi_modal_llm=llm,
                chat_history=chat_history,
                max_iterations=max_iterations,
                verbose=True,
            )
            return step_engine.as_agent()
        """
        return Agent.from_tools(
            tools=tools,
            llm=llm,
            chat_history=chat_history,
            max_iterations=max_iterations,
            verbose=verbose,
        )

"""----------------------------------------------------------------------------------------------SYSTEM IMPORTS------------------------------------------------------------------"""

import concurrent.futures
import os
import webbrowser

"""----------------------------------------------------------------------------------------------USER IMPORTS----------------------------------------------------------------------"""

# from ENGINE.STT.vosk_recog import speech_to_text
from ENGINE.STT.NetHyTech import SpeechToTextListener

from ENGINE.TTS.DeepGram import speak
# from ENGINE.TTS.edge_tts import speak
# from ENGINE.TTS.deepAI import speak
# from ENGINE.TTS.ai_voice import speak, initiate_proxies
# from ENGINE.TTS.stream_elements_api import speak

from BRAIN.AI.TEXT.API import openrouter
# from BRAIN.AI.TEXT.API import deepInfra_TEXT
# from BRAIN.AI.TEXT.API import liaobots
# from BRAIN.AI.TEXT.API import hugging_chat; hf_api = hugging_chat.HuggingChat_RE(model="microsoft/Phi-3-mini-4k-instruct")
# from BRAIN.AI.TEXT.API import Blackbox_ai
# from BRAIN.AI.TEXT.API import Phind

# from BRAIN.AI.VISION import deepInfra_VISION

# from BRAIN.TOOLS import groq_web_access

# from BRAIN.AI.IMAGE import deepInfra_IMG

# from PLAYGROUND.ADB_CALL import make_call, android_device_connection_setup; android_device_connection_setup.initialise()
# from PLAYGROUND.WEBSITE_ASSISTANT import jenna_reader, chrome_latest_url
# from PLAYGROUND.CAMERA import camera_vision

from PROMPTS import INSTRUCTIONS, BISECTORS

from TOOLS import Alpaca_DS_Converser

"""----------------------------------------------------------------------------------------------INITIALIZATION-------------------------------------------------------------------"""

listener = SpeechToTextListener()
history_manager = Alpaca_DS_Converser.ConversationHistoryManager()
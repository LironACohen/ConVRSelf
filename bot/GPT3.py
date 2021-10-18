import ConVRSelf.bot.STTConVRSelf as STTConVRSelf
import ConVRSelf.bot.TTSConVRSelf as TTSConVRSelf
import logging
import openai


logger = logging.getLogger(__name__)



def create_promt_for_sentence(input_sentence):
    return f'The following is a conversation with an AI therapist. The therapist is helpful, creative, clever, and very friendly.\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: {input_sentence}.\nAI:'


class GPT3():

    def __init__(self, name="davinci"):
        openai.api_key = ""
        self.tokenizer = ''
        self.model = ''
        self.tts = TTSConVRSelf.TTSConVRSelf()
        self.stt = STTConVRSelf.STTConVRSelf()


    def predict_sentence(self, input_sentence, file_name):


        response = openai.Completion.create(engine="davinci", prompt=create_promt_for_sentence(input_sentence), max_tokens=5)


        # open a (new) file to write
        # logger.info(f"chat: file name -- {file_name}")
        print(f"chat: file name -- {file_name}")
        outF = open(file_name + ".txt", "w")
        # response = ''
        outF.write(response)
        outF.close()
        return response, file_name + ".txt"

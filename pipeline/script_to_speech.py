from pipeline.script_to_speech_vertexai import script_to_speech as script_to_speech_vertexai

def script_to_speech(conversations, use_vertexai=True):
    if use_vertexai:
        return script_to_speech_vertexai(conversations)
    else:
        raise NotImplementedError("Only VertexAI is supported for now")
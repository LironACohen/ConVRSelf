### this python file was made in order to help create the session folder and to manipulate the audio name files

import os, datetime
import logging
import sys
logger = logging.getLogger(__name__)


# directoryCreation creates a directory with the current folder name to store the wav files in.
def directory_creation(id='',path_rel='Data'):
    path = os.getcwd()
    try:
        path = os.path.join(path, path_rel)
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)

        my_data_dir = os.path.join(
            path, 'Session_Files_' + datetime.datetime.now().strftime('%Y-%m-%d_%H_%M'))

        if id != '':
            my_data_dir = os.path.join(
                path, f"ID_{id}_Session_Files_{datetime.datetime.now().strftime('%Y-%m-%d_%H_%M')}")

        # Setting the name of the new directory
        my_audio_dir = os.path.join(
            path,
            my_data_dir+'/Audio_Data')

        my_text_dir = os.path.join(
            path,
            my_data_dir+'/Text_Data')

        my_gpt_data = os.path.join(
            path,
            my_data_dir+'/GPT_DATA')

        os.makedirs(my_audio_dir)
        os.makedirs(my_text_dir)
        os.mkdir(my_gpt_data)

        return my_audio_dir, my_text_dir, my_gpt_data, my_data_dir

    except OSError as e:
        logger.error('unable to create the repository',e)
        raise e
        # return 'unable to create the repository',


def next_available_file_name(dirname, side):

    i = 0
    while os.path.exists(dirname + '/' + ('ConvrSelf_Side_0_Record_%s.wav' % i)) or os.path.exists(dirname + '/' + ('ConvrSelf_Side_1_Record_%s.wav' % i)):
        i += 1
    if side == '0':
        return 'ConvrSelf_Side_0_Record_%s.wav' % i
    return 'ConvrSelf_Side_1_Record_%s.wav' % i




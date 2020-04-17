from pydub import AudioSegment
from pydub.playback import play
import time
import os

def main():
    directory = os.getcwd() + "\\media\\"

    sermon_file = str(directory) + "sermon_in.mp3"
    intro_file = str(directory) + "intro.mp3"
    outro_file = str(directory) + "outro.mp3"
    output_file = str(directory) + 'sermon_out.mp3'
    
    
    print('\nOverlaying Intro and Outro...')
    sermon = AudioSegment.from_mp3(sermon_file)
    intro = AudioSegment.from_mp3(intro_file)
    outro = AudioSegment.from_mp3(outro_file)
    
    len_intro = intro.duration_seconds
    len_intro_overlay = len_intro - 5
    
    len_sermon = sermon.duration_seconds
    
    output = intro.overlay(sermon[:5000], position=(len_intro_overlay*1000))
    output = output + sermon[5000:]
    
    
    len_output_overlay = output.duration_seconds - 5
    
    output = output.overlay(outro[:5000], position=(len_output_overlay*1000))
    
    output = output + outro[5000:]
        
    print("Creating File...")
    output.export(output_file, format='mp3')
    
    print("Finished Overlay Output File")
    return(True)
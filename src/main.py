from moviepy.editor import AudioFileClip, ImageClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import pylrc

input_mp3 = './input/song.mp3'
input_img = './input/background.jpg'
input_lrc = './input/song.lrc'

output_mp4 = './output/song.mp4'


def main() :
    audio_clip = AudioFileClip( input_mp3 )
    image_clip = ImageClip( input_img )

    image_clip = image_clip.set_audio( audio_clip )
    image_clip.duration = audio_clip.duration
    image_clip.fps = 30

    lrc_file = open( input_lrc )
    lrc_string = ''.join( lrc_file.readlines() )
    lrc_file.close()

    lrc_lyrics = pylrc.parse(lrc_string)
    lyrics = []

    for i in range( len( lrc_lyrics ) - 1 ) :
        current_lyric = lrc_lyrics[i]
        next_lyric = lrc_lyrics[i + 1]

        start_time = current_lyric.time
        end_time = next_lyric.time
        
        lyrics.append( ( ( start_time, end_time ), current_lyric.text ) )

    generator = lambda txt: TextClip(txt, font='Arial', fontsize=50, color='white')

    lyric_clip = SubtitlesClip( lyrics, generator )

    result = CompositeVideoClip([image_clip, lyric_clip.set_pos(('center'))])
    result.duration = image_clip.duration
    result.fps = image_clip.fps

    result.write_videofile( output_mp4 )


if __name__ == "__main__":
    main()
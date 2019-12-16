from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip("WIN_20191129_14_32_31_Pro.mp4", 3270, 3282, targetname="cut.mp4")

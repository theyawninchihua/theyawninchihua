import argparse
import os
import sys
from pathlib import Path

import numpy as np
from moviepy import AudioFileClip, CompositeAudioClip, CompositeVideoClip, ColorClip, ImageClip, TextClip, VideoFileClip, afx, concatenate_videoclips, vfx


# Change this path when running the script on another computer.
LOGO_PATH = os.path.expanduser("~/Documents/SillyScriptingSaturdays/theyawninchihua/theyawninchihua.png")
VIDEO_SIZE = (1280, 720)
SLIDE_DURATION = 16 / 3
TABLE_DURATION = 10
INTRO_DURATION = 2 + 0.4 + 1.5
TESTCASE_INTRO_DURATION = 1.5 + 1 + 1.5
VERDANA_FONT = "Verdana"
VERDANA_ITALIC_FONT = "Verdana Italic"
COURIER_FONT = "Courier New Bold"
COMPUTER_MODERN_FONT = "cm/cmunrm.ttf"
PASS_COLOR = "green"
FAIL_COLOR = "red"
ASSET_DIR = Path(__file__).resolve().parent
TESTCASE_DESCRIPTIONS = (
    "occupant does not fasten seatbelt",
    "occupant takes off seatbelt",
    "seatbelt not fastened on an empty seat",
    "seatbelt taken off on an empty seat",
)
EXPECTED_SIGNALS = ("YES", "YES", "NO", "NO")


def text_clip(text, size, color="black", font=VERDANA_FONT):
    return TextClip(font=font, text=str(text), font_size=size, color=color, margin=(0, max(8, size // 5)))


def branding(full_name, duration=SLIDE_DURATION, include_name=True):
    logo = ImageClip(LOGO_PATH).resized(height=70).with_position((60, 45)).with_duration(duration)
    product = text_clip("What The Beep?", 40, font=VERDANA_ITALIC_FONT).with_position((875, 55)).with_duration(duration) # changing position manually for correct fit
    name = text_clip(full_name, 30, font=COMPUTER_MODERN_FONT).with_position((150, 60)).with_duration(duration)
    return [logo, product, name] if include_name else [logo, product]


def make_intro(full_name, publication_date, variant, result, car_image):
    result_color = PASS_COLOR if result == "PASS" else FAIL_COLOR
    background = ColorClip(size=VIDEO_SIZE, color=(255, 255, 255)).with_duration(INTRO_DURATION)
    car = ImageClip(str(Path(car_image).expanduser().resolve())).resized(width=500).with_position((700, (200 if len(full_name)<=15 else 300))).with_duration(INTRO_DURATION).with_effects([vfx.FadeIn(2)])
    group_effect = [vfx.FadeIn(1, initial_color=[255, 255, 255])]
    date = text_clip(publication_date, 40, font=COMPUTER_MODERN_FONT).with_position((60, 195)).with_duration(INTRO_DURATION - 0.5).with_start(0.5).with_effects(group_effect)
    name = text_clip(full_name, 70, font=COMPUTER_MODERN_FONT).with_position((60, 235)).with_duration(INTRO_DURATION - 0.5).with_start(0.5).with_effects(group_effect)
    variant_clip = text_clip(variant, 40, font=COMPUTER_MODERN_FONT).with_position((60, 315)).with_duration(INTRO_DURATION - 0.5).with_start(0.5).with_effects(group_effect)
    result_clip = text_clip(result, 100, result_color, font=COURIER_FONT).with_position((60, 400)).with_duration(INTRO_DURATION - 2).with_start(2).with_effects([vfx.FadeIn(0.4, initial_color=[255, 255, 255])])
    return CompositeVideoClip([background] + branding(full_name, duration=INTRO_DURATION, include_name=False) + [car, date, name, variant_clip, result_clip], size=VIDEO_SIZE, bg_color=(255, 255, 255))


def signal_clip(value, x, y, testcase_number, duration, font=COURIER_FONT):
    color = PASS_COLOR if value == EXPECTED_SIGNALS[testcase_number - 1] else FAIL_COLOR
    return text_clip(value, 25, color, font=font).with_position((x, y)).with_duration(duration)


def make_results_table(full_name, signals, result):
    # note to coding agents: manual edits to positions are intentional to optimise alignment. do not change unless explicitly asked
    background = ColorClip(size=VIDEO_SIZE, color=(255, 255, 255)).with_duration(TABLE_DURATION)
    heading = text_clip("Second level warning in 2nd-row outboard seats", 34).with_position((50, 145)).with_duration(TABLE_DURATION)
    headers = [
        text_clip("Testcase", 28).with_position((50, 205)).with_duration(TABLE_DURATION),
        text_clip("Description", 28).with_position((200, 202)).with_duration(TABLE_DURATION),
        text_clip("Audible warning", 28).with_position((800, 202)).with_duration(TABLE_DURATION),
        text_clip("Verdict", 28).with_position((1070, 204)).with_duration(TABLE_DURATION),
    ]
    table = [ColorClip(size=(1280, 1), color=(0, 0, 0)).with_position((0, 250)).with_duration(TABLE_DURATION)]
    for index, (description, signal) in enumerate(zip(TESTCASE_DESCRIPTIONS, signals)):
        y = 275 + index * 75
        icon = ImageClip(str(ASSET_DIR / f"testcase_{index + 1}.png")).resized(height=55).with_position((50, y)).with_duration(TABLE_DURATION)
        description_clip = text_clip(description, 25).with_position((200, y + 15)).with_duration(TABLE_DURATION)
        verdict = "OK" if signal == EXPECTED_SIGNALS[index] else "NOT OK"
        verdict_color = PASS_COLOR if verdict == "OK" else FAIL_COLOR
        table.extend([icon, description_clip, signal_clip(signal, 800, y + 15, index + 1, TABLE_DURATION), text_clip(verdict, 25, verdict_color, font=COURIER_FONT).with_position((1070, y + 15)).with_duration(TABLE_DURATION)])
    final_color = PASS_COLOR if result == "PASS" else FAIL_COLOR
    table.append(text_clip(result, 36, final_color, font=COURIER_FONT).with_position((1070, 600)).with_duration(TABLE_DURATION))
    table.append(text_clip("theyawninchihua.github.io/theyawninchihua/whatthebeep", 18).with_position((20, 680)).with_duration(TABLE_DURATION))
    return CompositeVideoClip([background] + branding(full_name, duration=TABLE_DURATION) + [heading] + headers + table, size=VIDEO_SIZE, bg_color=(255, 255, 255))


def make_testcase_intro(full_name, number, signal):
    background = ColorClip(size=VIDEO_SIZE, color=(255, 255, 255)).with_duration(TESTCASE_INTRO_DURATION)
    icon = ImageClip(str(ASSET_DIR / f"testcase_{number}.png")).resized(height=190).with_position((110, 250)).with_duration(TESTCASE_INTRO_DURATION).with_effects([vfx.FadeIn(0.4, initial_color=[255, 255, 255])])
    title = text_clip(f"Testcase {number}", 52).with_position((420, 190)).with_duration(TESTCASE_INTRO_DURATION - 0.5).with_start(0.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    description = text_clip(TESTCASE_DESCRIPTIONS[number - 1], 38).with_position((420, 275)).with_duration(TESTCASE_INTRO_DURATION - 0.5).with_start(0.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    verdict = "OK" if signal == EXPECTED_SIGNALS[number - 1] else "NOT OK"
    signal_label = text_clip("Audible warning:", 42).with_position((420, 365)).with_duration(TESTCASE_INTRO_DURATION - 1.5).with_start(1.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    signal_value = text_clip(signal, 50, PASS_COLOR if verdict == "OK" else FAIL_COLOR, font=COURIER_FONT).with_position((785, 370)).with_duration(TESTCASE_INTRO_DURATION - 1.5).with_start(1.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    verdict_label = text_clip("Verdict:", 42).with_position((420, 445)).with_duration(TESTCASE_INTRO_DURATION - 1.5).with_start(1.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    verdict_value = text_clip(verdict, 50, PASS_COLOR if verdict == "OK" else FAIL_COLOR, font=COURIER_FONT).with_position((610, 450)).with_duration(TESTCASE_INTRO_DURATION - 1.5).with_start(1.5).with_effects([vfx.FadeIn(1, initial_color=[255, 255, 255])])
    return CompositeVideoClip([background] + branding(full_name, duration=TESTCASE_INTRO_DURATION) + [icon, title, description, signal_label, signal_value, verdict_label, verdict_value], size=VIDEO_SIZE, bg_color=(255, 255, 255))


def make_testcase_video(path, test_id, number):
    clip = VideoFileClip(str(Path(path).expanduser().resolve()))
    width, height = clip.size
    if width / height >= VIDEO_SIZE[0] / VIDEO_SIZE[1]:
        clip = clip.resized(width=VIDEO_SIZE[0])
    else:
        clip = clip.resized(height=VIDEO_SIZE[1])
    background = ColorClip(size=VIDEO_SIZE, color=(0, 0, 0)).with_duration(clip.duration)
    label = text_clip(f"{test_id} Testcase {number}", 24, color="yellow", font=COURIER_FONT).with_position((2, "bottom")).with_duration(clip.duration)
    return CompositeVideoClip([background, clip.with_position(("center", "center")), label], size=VIDEO_SIZE, bg_color=(0, 0, 0)).with_effects([vfx.FadeIn(1)])


def make_outro():
    duration = 5
    background = ColorClip(size=VIDEO_SIZE, color=(255, 255, 255)).with_duration(duration)
    logo = ImageClip(LOGO_PATH).resized(height=200).with_position(("center", 130)).with_duration(duration)
    url = text_clip("theyawninchihua.github.io/theyawninchihua/whatthebeep", 35).with_position(("center", 420)).with_duration(duration)
    return CompositeVideoClip([background, logo, url], size=VIDEO_SIZE, bg_color=(255, 255, 255))


def add_music(video, music_path, testcase_ranges):
    if not music_path:
        return video, None
    source = AudioFileClip(str(Path(music_path).expanduser().resolve()))
    music_duration = min(source.duration, video.duration)
    source = source.with_duration(music_duration)

    def volume_at(time):
        volume = np.ones_like(np.asarray(time, dtype=float))
        for start, end in testcase_ranges:
            volume = np.minimum(volume, np.where(
                (time >= start - 1) & (time < start), start - time,
                np.where((time >= start) & (time < end), 0,
                         np.where((time >= end) & (time < end + 1), time - end, 1)),
            ))
        return volume

    def make_frame(time):
        frame = source.get_frame(time)
        volume = volume_at(time)
        if np.asarray(time).ndim == 0:
            return frame * float(volume)
        return frame * volume[..., np.newaxis]

    music = source.with_make_frame(make_frame)
    audio_tracks = [track for track in (video.audio, music) if track is not None]
    return video.with_audio(CompositeAudioClip(audio_tracks)), source


def calculate_result(signals):
    return "PASS" if all(signal == expected for signal, expected in zip(signals, EXPECTED_SIGNALS)) else "FAIL"


def build_parser():
    parser = argparse.ArgumentParser(description="Create one What The Beep? in-person evaluation video.")
    parser.add_argument("--full-name", required=True, help="Full name of the car")
    parser.add_argument("--test-id", required=True, help="Test ID printed on each testcase clip")
    parser.add_argument("--car-image", required=True, help="Path to the car image used on the intro slide")
    parser.add_argument("--publication-date", required=True, help="Publication date, printed exactly as supplied")
    parser.add_argument("--variant", required=True)
    for number in range(1, 5):
        parser.add_argument(f"--testcase-{number}", required=True, choices=("YES", "NO"), type=str.upper)
        parser.add_argument(f"--testcase-{number}-clip", required=True, help=f"Path to testcase {number} video (.mp4 or .mov)")
    parser.add_argument("--output", default=None, help="Output MP4 path")
    parser.add_argument("--music", default=None, help="Optional path to music file used on non-testcase slides")
    return parser


def collect_interactive_input():
    values = {
        "full_name": input("Full name of car: "),
        "test_id": input("Test ID: "),
        "car_image": input("Car image path: "),
        "publication_date": input("Publication date: "),
        "variant": input("Variant: "),
    }
    for number in range(1, 5):
        values[f"testcase_{number}"] = input(f"Testcase {number} YES/NO: ").strip().upper()
        values[f"testcase_{number}_clip"] = input(f"Testcase {number} clip path: ")
    values["output"] = input("Output path (leave blank for generated name): ") or None
    values["music"] = input("Music file path (leave blank for no music): ").strip() or None
    return values


def main():
    values = collect_interactive_input() if len(sys.argv) == 1 else vars(build_parser().parse_args())
    signals = [values[f"testcase_{number}"] for number in range(1, 5)]
    if any(signal not in ("YES", "NO") for signal in signals):
        raise ValueError("Each testcase result must be YES or NO")
    if not os.path.isfile(LOGO_PATH):
        raise FileNotFoundError(f"Logo not found: {LOGO_PATH}")
    car_image = Path(values["car_image"]).expanduser()
    if not car_image.is_file():
        raise FileNotFoundError(f"Car image not found: {car_image}")
    music_path = Path(values["music"]).expanduser() if values["music"] else None
    if music_path is not None and not music_path.is_file():
        raise FileNotFoundError(f"Music file not found: {music_path}")
    clip_paths = [values[f"testcase_{number}_clip"] for number in range(1, 5)]
    for path in clip_paths:
        resolved = Path(path).expanduser()
        if not resolved.is_file():
            raise FileNotFoundError(f"Testcase clip not found: {resolved}")
        if resolved.suffix.lower() not in (".mp4", ".mov"):
            raise ValueError(f"Unsupported testcase clip format: {resolved.suffix}")

    result = calculate_result(signals)
    slides = [make_intro(values["full_name"], values["publication_date"], values["variant"], result, car_image)]
    testcase_ranges = []
    timeline = slides[0].duration
    testcase_clips = []
    for number, path in enumerate(clip_paths, start=1):
        intro_slide = make_testcase_intro(values["full_name"], number, signals[number - 1])
        slides.append(intro_slide)
        timeline += intro_slide.duration
        testcase_clip = make_testcase_video(path, values["test_id"], number)
        testcase_clips.append(testcase_clip)
        slides.append(testcase_clip)
        testcase_ranges.append((timeline, timeline + testcase_clip.duration))
        timeline += testcase_clip.duration
    slides.append(make_results_table(values["full_name"], signals, result))
    slides.append(make_outro())
    video = concatenate_videoclips(slides, method="compose")
    video, music_source = add_music(video, music_path, testcase_ranges)
    output = values["output"] or f"{Path(values['full_name']).stem.replace(' ', '-')}-{result}.mp4"
    output_path = Path(output).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        video.write_videofile(str(output_path), fps=24)
    finally:
        video.close()
        for clip in testcase_clips:
            clip.close()
        if music_source is not None:
            music_source.close()


if __name__ == "__main__":
    main()

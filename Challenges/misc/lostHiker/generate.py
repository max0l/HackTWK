import numpy as np
from scipy.io.wavfile import write
import random

# Morse Code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text if c.upper() in MORSE_CODE_DICT)

def generate_tone(freq, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def morse_to_audio(morse, wpm=20, freq=800, freq_jitter=0, sample_rate=44100, amplitude=0.3):
    unit_time = 1.2 / wpm
    dot = lambda f: generate_tone(f, unit_time, sample_rate, amplitude)
    dash = lambda f: generate_tone(f, 3 * unit_time, sample_rate, amplitude)
    gap = np.zeros(int(sample_rate * unit_time))
    short_gap = np.zeros(int(sample_rate * 3 * unit_time))
    long_gap = np.zeros(int(sample_rate * 7 * unit_time))

    audio = []
    for char in morse:
        f = freq + random.uniform(-freq_jitter, freq_jitter)
        if char == '.':
            audio.extend(dot(f))
            audio.extend(gap)
        elif char == '-':
            audio.extend(dash(f))
            audio.extend(gap)
        elif char == ' ':
            audio.extend(short_gap)
        elif char == '/':
            audio.extend(long_gap)
    return np.array(audio)

def generate_noise(duration, sample_rate=44100, amplitude=0.05):
    return np.random.normal(0, amplitude, int(sample_rate * duration))

def generate_non_morse_chatter(num_blips=20, total_duration=10, sample_rate=44100):
    result = np.zeros(int(sample_rate * total_duration))
    for _ in range(num_blips):
        start_time = random.randint(0, len(result) - sample_rate // 2)
        duration = random.uniform(0.1, 0.4)
        freq = random.randint(300, 2600)
        amp = random.uniform(0.1, 0.25)
        blip = generate_tone(freq, duration, sample_rate, amp)
        end = start_time + len(blip)
        result[start_time:end] += blip
    return result

def insert_with_offset(signal, offset_seconds, total_duration, sample_rate=44100):
    offset_samples = int(offset_seconds * sample_rate)
    total_samples = int(sample_rate * total_duration)
    padded = np.zeros(total_samples)
    end = offset_samples + len(signal)
    if end > total_samples:
        signal = signal[:total_samples - offset_samples]
    padded[offset_samples:offset_samples + len(signal)] = signal
    return padded

def mix_signals(signals):
    max_len = max(len(s) for s in signals)
    padded = [np.pad(s, (0, max_len - len(s))) for s in signals]
    mix = np.sum(padded, axis=0)
    mix /= np.max(np.abs(mix))
    return mix.astype(np.float32)

def save_wav(filename, audio, sample_rate=44100):
    scaled = np.int16(audio * 32767)
    write(filename, sample_rate, scaled)

# === MAIN CONFIG ===
if __name__ == "__main__":
    sample_rate = 44100
    total_duration = 30  # seconds
    freq_jitter = 3

    hiker_message = "sos hacktwkf0ur13ran4lys15"
    hiker_freq = 800
    hiker_wpm = 18
    hiker_offset = 3

    # Realistic non-military search and rescue chatter
    chatter_messages = [
        "radio check anyone copy", "still no sign of subject",
        "weather getting worse", "repeat last transmission",
        "setting up base camp", "found broken branches here",
        "checking coordinates now", "moved north about 100 meters",
        "signal weak please repeat", "copy that on my way",
        "there is a trail marker", "nightfall in 20 minutes",
        "moving along riverbed", "checked cabin empty",
        "need backup flashlight", "holding position here",
        "marking this area", "calling in next patrol",
        "watch your step here", "could be an animal track"
    ]

    # Generate frequencies, skipping 800 Hz
    chatter_freqs = []
    base_freq = 300
    freq_spacing = 100
    for _ in range(len(chatter_messages)):
        if base_freq == hiker_freq:
            base_freq += freq_spacing
        chatter_freqs.append(base_freq)
        base_freq += freq_spacing

    signals = []

    delayed_indices = set(random.sample(range(len(chatter_messages)), int(len(chatter_messages) * 0.2)))
    gapped_indices = set(random.sample([i for i in range(len(chatter_messages)) if i not in delayed_indices],
                                       int(len(chatter_messages) * 0.3)))

    for i, (msg, freq) in enumerate(zip(chatter_messages, chatter_freqs)):
        wpm = random.randint(12, 25)
        morse = text_to_morse(msg)
        base_audio = morse_to_audio(
            morse, wpm=wpm, freq=freq, freq_jitter=freq_jitter,
            sample_rate=sample_rate, amplitude=0.25
        )

        if i in gapped_indices:
            # Insert random gaps between repeats, don’t fill the full duration
            chunk_duration = len(base_audio) / sample_rate
            signal = np.zeros(int(sample_rate * total_duration))
            pos = 0
            while pos + len(base_audio) < len(signal):
                gap = random.uniform(0.3, 1.2)  # random pause between repeats
                gap_samples = int(gap * sample_rate)
                signal[pos:pos + len(base_audio)] = base_audio
                pos += len(base_audio) + gap_samples
            if i in delayed_indices:
                offset = random.uniform(1.0, 5.0)
                signal = insert_with_offset(signal, offset, total_duration, sample_rate)
            signals.append(signal)
        else:
            # Normal full-fill signal, possibly delayed
            repeat_count = int(np.ceil((total_duration * sample_rate) / len(base_audio)))
            looped_audio = np.tile(base_audio, repeat_count)
            looped_audio = looped_audio[:int(sample_rate * total_duration)]
            if i in delayed_indices:
                offset = random.uniform(1.0, 5.0)
                looped_audio = insert_with_offset(looped_audio, offset, total_duration, sample_rate)
            signals.append(looped_audio)


    # Hiker signal (inserted at offset)
    morse_hiker = text_to_morse(hiker_message)
    hiker_audio = morse_to_audio(
        morse_hiker, wpm=hiker_wpm, freq=hiker_freq, freq_jitter=2,
        sample_rate=sample_rate, amplitude=0.35
    )
    signals.append(insert_with_offset(hiker_audio, hiker_offset, total_duration, sample_rate))

    morse_rick = text_to_morse("never gonna give you up never gonna let you down")
    rick_audio = morse_to_audio(
        morse_rick, wpm=25, freq=17000, freq_jitter=2,
        sample_rate=sample_rate, amplitude=0.35
    )
    signals.append(insert_with_offset(rick_audio, 2, total_duration, sample_rate))

    # Add background noise and non-morse blips
    blips = generate_non_morse_chatter(num_blips=30, total_duration=total_duration, sample_rate=sample_rate)
    noise = generate_noise(duration=total_duration, sample_rate=sample_rate, amplitude=0.025)
    signals.append(blips)
    signals.append(noise)

    # Mix and save
    full_mix = mix_signals(signals)
    save_wav("recording.wav", full_mix)
    print("✅ Generated recording.wav!")


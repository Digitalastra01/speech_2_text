import torch
import torchaudio
import tempfile
import os

def test_torchaudio():
    print("Testing torchaudio...")
    print(f"Torchaudio version: {torchaudio.__version__}")
    
    try:
        # Generate random audio data
        waveform = torch.randn(1, 16000)  # 1 second of noise at 16kHz
        sample_rate = 16000

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
            temp_filename = temp_wav.name

        try:
            # Save
            torchaudio.save(temp_filename, waveform, sample_rate)
            print(f"Saved to {temp_filename}")

            # Load
            loaded_waveform, loaded_sr = torchaudio.load(temp_filename)
            print(f"Loaded from {temp_filename}")
            print(f"Shape: {loaded_waveform.shape}, SR: {loaded_sr}")

            assert loaded_sr == sample_rate
            assert loaded_waveform.shape == waveform.shape
            print("Verification SUCCESS!")

        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    except Exception as e:
        print(f"Verification FAILED: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    test_torchaudio()



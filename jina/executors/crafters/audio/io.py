from typing import Dict
from .. import BaseDocCrafter


class AudioReader(BaseDocCrafter):
    """
    :class:`AudioReader` reads and resamples the audio signal on doc-level.
    """

    def __init__(self, target_sample_rate: int = 22050, *args, **kwargs):
        """
        :class:`AudioReader` loads an audio file as `ndarray` and resamples the audio signal to the target sampling rate
        (default 22050Hz).

        :param target_sample_rate: target sampling rate (scalar number > 0)
        """
        super().__init__(*args, **kwargs)
        self.sample_rate = target_sample_rate

    def craft(self, buffer: bytes, doc_id: int, *args, **kwargs) -> Dict:
        """
        Decodes the given audio file, resamples the signal and saves the `ndarray` of the signal in the `blob` of the
        Document.

        Supported sound formats: WAV, MP3, OGG, AU, FLAC, RAW, AIFF, AIFF-C, PAF, SVX, NIST, VOC, IRCAM, W64, MAT4, MAT5
        , PVF, XI, HTK, SDS, AVR, WAVEX, SD2, CAF, WVE, MPC2K, RF64.

        :param buffer: the audio file path in raw bytes.
        :param doc_id: the id of the Document
        :return: a Document dict with the decoded audio signal
        """
        import librosa
        audio_path = buffer.decode()
        signal, orig_sr = librosa.load(audio_path, sr=self.sample_rate, mono=False)

        return dict(doc_id=doc_id, offset=0, weight=1., blob=signal)

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np  

@dataclass
class SignalRecord:

    """
    Canonical representation of a biological signal inside the system.

    Attributes
    ----------
    x:
        1D signal samples (will be normalized to a 1D float numpy array).
    fs:
        Sampling frequency in Hz.
    signal_type:
        Signal domain type, e.g., "ecg", "eeg", "emg", "ppg", "resp", "temp", "motion".
    units:
        Optional units for the signal amplitude (e.g., "mV", "a.u.", "°C").
    meta:
        Free-form metadata (file name, lead index, column name, device info, etc.).
    """
    x: np.ndarray
    fs: float
    signal_type: str
    units: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # 1. Normalize x to a 1D float numpy array
        self.x = np.asarray(self.x, dtype=float)
        self.x = np.squeeze(self.x)

        # 2. Shape validation and basic integrity
        if self.x.ndim != 1:
            raise ValueError(f"Signal x must be 1D after squeezing, but got shape {self.x.shape}")
        if self.x.size == 0:
            raise ValueError("Signal is empty")
        if self.fs <= 0:
            raise ValueError(f"SignalRecord.fs must be >0 but got {self.fs}")
        if not np.isfinite(self.x).all():
            raise ValueError("Signal contains non-finite values (NaN or Inf)")

    def n_samples(self) -> int:
        """Return the number of samples in the signal."""
        return self.x.size
    def duration_s(self) -> float:
        """Return the duration of the signal in seconds."""
        return self.n_samples() / self.fs
    def time_vector(self) -> np.ndarray:
        """Return a time vector corresponding to the signal samples."""
        return np.arange(self.n_samples()) / self.fs

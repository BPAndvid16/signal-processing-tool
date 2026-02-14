import numpy as np

from core.records import SignalRecord


def test_valid_record():
    x = [0, 1, 0, -1] * 10  # list on purpose
    record = SignalRecord(x=x, fs=250, signal_type="ecg", units="a.u.")
    print("✅ Valid record created")
    print("n_samples:", record.n_samples())
    print("duration_s:", record.duration_s())
    print("time_vector first 5:", record.time_vector()[:5])


def test_invalid_fs():
    try:
        SignalRecord(x=[1, 2, 3], fs=0, signal_type="ecg")
    except ValueError as e:
        print("✅ Invalid fs caught:", e)


def test_invalid_shape():
    try:
        x2d = np.zeros((2, 100))
        SignalRecord(x=x2d, fs=250, signal_type="ecg")
    except ValueError as e:
        print("✅ Invalid shape caught:", e)


if __name__ == "__main__":
    test_valid_record()
    test_invalid_fs()
    test_invalid_shape()
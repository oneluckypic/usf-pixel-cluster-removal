
import numpy as np
import pandas as pd
import pytest

from usf_mosquitos.metrics import simple_accuracy

def test_simple_accuracy():

    data = [['0.jpg', 'Lepidium', 2, 2, 3, 2],
            ['0.jpg', 'Background', 6, 7, 3, 4]]
    df = pd.DataFrame(data, columns=['filename', 'class', 'row', 'col', 'width', 'height'])

    mask = np.ones(shape=(10, 10))

    assert simple_accuracy(df, mask) == pytest.approx(0.5)

    mask[2:4, 2:5] = 0

    assert simple_accuracy(df, mask) == pytest.approx(1.0)

    mask[2, 2] = 255

    assert simple_accuracy(df, mask) == pytest.approx(1 - 1/12)

    mask[6, 7] = 0

    assert simple_accuracy(df, mask) == pytest.approx(1 - 1/12 - 1/24)

    mask = np.ones(shape=(10, 10))
    mask[6:10, 7:10] = 0
    assert simple_accuracy(df, mask) == pytest.approx(0.0)

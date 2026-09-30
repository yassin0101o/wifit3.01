"""RTL8821CU-DKMS supported-channel regression tests."""
from wifit3.chips.rtl8821cu_dkms.driver import CHANNELS_2G, CHANNELS_5G


_ORIGINAL_5G = [36, 40, 44, 48, 149, 153, 157, 161, 165]
_DFS_5G = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140]


def test_rtl8821cu_includes_channel_120():
    assert 120 in CHANNELS_5G


def test_rtl8821cu_includes_all_requested_dfs_channels():
    assert set(_DFS_5G) <= set(CHANNELS_5G)


def test_rtl8821cu_keeps_original_non_dfs_channels():
    assert set(_ORIGINAL_5G) <= set(CHANNELS_5G)


def test_rtl8821cu_channel_lists_have_no_duplicates():
    assert len(CHANNELS_2G) == len(set(CHANNELS_2G))
    assert len(CHANNELS_5G) == len(set(CHANNELS_5G))


def test_rtl8821cu_5ghz_channels_are_sorted_and_step_aligned():
    assert CHANNELS_5G == sorted(CHANNELS_5G)
    assert all((channel - 36) % 4 == 0 for channel in CHANNELS_5G)

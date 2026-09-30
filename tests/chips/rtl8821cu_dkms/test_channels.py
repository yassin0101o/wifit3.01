"""RTL8821CU-DKMS supported-channel regression tests."""
from wifit3.chips.rtl8821cu_dkms.driver import CHANNELS_2G, CHANNELS_5G


_ORIGINAL_5G = [36, 40, 44, 48, 149, 153, 157, 161, 165]
_DFS_5G = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144]


def test_rtl8821cu_includes_channel_120():
    """Channel 120 (DFS) must be in the supported list."""
    assert 120 in CHANNELS_5G


def test_rtl8821cu_includes_all_requested_dfs_channels():
    """All DFS channels (52-144) must be present."""
    assert set(_DFS_5G) <= set(CHANNELS_5G)


def test_rtl8821cu_keeps_original_non_dfs_channels():
    """Original non-DFS 5GHz channels must be preserved."""
    assert set(_ORIGINAL_5G) <= set(CHANNELS_5G)


def test_rtl8821cu_channel_lists_have_no_duplicates():
    """Channel lists must have no duplicates."""
    assert len(CHANNELS_2G) == len(set(CHANNELS_2G))
    assert len(CHANNELS_5G) == len(set(CHANNELS_5G))


def test_rtl8821cu_5ghz_channels_are_sorted():
    """5GHz channels must be in ascending order."""
    assert CHANNELS_5G == sorted(CHANNELS_5G)


def test_rtl8821cu_5ghz_channels_step_aligned_by_band():
    """5GHz channels must be step-aligned within their respective bands:
    - 36-64 (UNII-1 + UNII-2): step 4
    - 100-144 (UNII-2 Extended): step 4
    - 149-165 (UNII-3): step 4
    """
    # UNII-1 + UNII-2 (36-64): all channels must be (ch - 36) % 4 == 0
    unii12 = [ch for ch in CHANNELS_5G if 36 <= ch <= 64]
    assert all((ch - 36) % 4 == 0 for ch in unii12), "UNII-1/2 channels must align: (ch - 36) % 4 == 0"
    
    # UNII-2 Extended (100-144): all channels must be (ch - 100) % 4 == 0
    unii2e = [ch for ch in CHANNELS_5G if 100 <= ch <= 144]
    assert all((ch - 100) % 4 == 0 for ch in unii2e), "UNII-2e channels must align: (ch - 100) % 4 == 0"
    
    # UNII-3 (149-165): all channels must be (ch - 149) % 4 == 0
    unii3 = [ch for ch in CHANNELS_5G if 149 <= ch <= 165]
    assert all((ch - 149) % 4 == 0 for ch in unii3), "UNII-3 channels must align: (ch - 149) % 4 == 0"

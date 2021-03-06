from typing import NamedTuple


class VGATiming(NamedTuple):
    x: int
    y: int
    refresh_rate: float
    pixel_freq: int
    h_front_porch: int
    h_sync_pulse: int
    h_back_porch: int
    v_front_porch: int
    v_sync_pulse: int
    v_back_porch: int

vga_timings = {
     '640x350@70Hz': VGATiming(
        x             = 640,
        y             = 350,
        refresh_rate  = 70.0,
        pixel_freq    = 25_175_000,
        h_front_porch = 16,
        h_sync_pulse  = 96,
        h_back_porch  = 48,
        v_front_porch = 37,
        v_sync_pulse  = 2,
        v_back_porch  = 60),
    '640x350@85Hz': VGATiming(
        x             = 640,
        y             = 350,
        refresh_rate  = 85.0,
        pixel_freq    = 31_500_000,
        h_front_porch = 32,
        h_sync_pulse  = 64,
        h_back_porch  = 96,
        v_front_porch = 32,
        v_sync_pulse  = 3,
        v_back_porch  = 60),
    '640x400@70Hz': VGATiming(
        x             = 640,
        y             = 400,
        refresh_rate  = 70.0,
        pixel_freq    = 25_175_000,
        h_front_porch = 16,
        h_sync_pulse  = 96,
        h_back_porch  = 48,
        v_front_porch = 12,
        v_sync_pulse  = 2,
        v_back_porch  = 35),
    '640x400@85Hz': VGATiming(
        x             = 640,
        y             = 400,
        refresh_rate  = 85.0,
        pixel_freq    = 31_500_000,
        h_front_porch = 32,
        h_sync_pulse  = 64,
        h_back_porch  = 96,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 41),
    '640x480@60Hz': VGATiming(
        x             = 640,
        y             = 480,
        refresh_rate  = 60.0,
        pixel_freq    = 25_175_000,
        h_front_porch = 16,
        h_sync_pulse  = 96,
        h_back_porch  = 48,
        v_front_porch = 10,
        v_sync_pulse  = 2,
        v_back_porch  = 33),
    '720x400@85Hz': VGATiming(
        x             = 720,
        y             = 400,
        refresh_rate  = 85.0,
        pixel_freq    = 35_500_000,
        h_front_porch = 36,
        h_sync_pulse  = 72,
        h_back_porch  = 108,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 42),
    '768x576@60Hz': VGATiming(
        x             = 758,
        y             = 576,
        refresh_rate  = 60.0,
        pixel_freq    = 34_960_000,
        h_front_porch = 24,
        h_sync_pulse  = 80,
        h_back_porch  = 104,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 17),
    '768x576@72Hz': VGATiming(
        x             = 758,
        y             = 576,
        refresh_rate  = 72.0,
        pixel_freq    = 42_930_000,
        h_front_porch = 32,
        h_sync_pulse  = 80,
        h_back_porch  = 112,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 21),
    '768x576@75Hz': VGATiming(
        x             = 758,
        y             = 576,
        refresh_rate  = 75.0,
        pixel_freq    = 45_510_000,
        h_front_porch = 40,
        h_sync_pulse  = 80,
        h_back_porch  = 120,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 22),
    '800x600@60Hz': VGATiming(
        x             = 800,
        y             = 600,
        refresh_rate  = 60.0,
        pixel_freq    = 40_000_000,
        h_front_porch = 40,
        h_sync_pulse  = 128,
        h_back_porch  = 88,
        v_front_porch = 1,
        v_sync_pulse  = 4,
        v_back_porch  = 23),
    '848x480@60Hz': VGATiming(
        x             = 848,
        y             = 480,
        refresh_rate  = 60.0,
        pixel_freq    = 33_750_000,
        h_front_porch = 16,
        h_sync_pulse  = 112,
        h_back_porch  = 112,
        v_front_porch = 6,
        v_sync_pulse  = 8,
        v_back_porch  = 23),
    '1024x768@60Hz': VGATiming(
        x             = 1024,
        y             = 768,
        refresh_rate  = 60.0,
        pixel_freq    = 65_000_000,
        h_front_porch = 24,
        h_sync_pulse  = 136,
        h_back_porch  = 160,
        v_front_porch = 3,
        v_sync_pulse  = 6,
        v_back_porch  = 29),
    '1152x864@60Hz': VGATiming(
        x             = 1152,
        y             = 864,
        refresh_rate  = 60.0,
        pixel_freq    = 81_620_000,
        h_front_porch = 64,
        h_sync_pulse  = 120,
        h_back_porch  = 184,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 27),
    '1280x720@60Hz': VGATiming(
        x             = 1280,
        y             = 720,
        refresh_rate  = 60.0,
        pixel_freq    = 74_250_000,
        h_front_porch = 110,
        h_sync_pulse  = 40,
        h_back_porch  = 220,
        v_front_porch = 5,
        v_sync_pulse  = 5,
        v_back_porch  = 20),
    '1280x768@60Hz': VGATiming(
        x             = 1280,
        y             = 768,
        refresh_rate  = 60.0,
        pixel_freq    = 79_500_000,
        h_front_porch = 64,
        h_sync_pulse  = 128,
        h_back_porch  = 192,
        v_front_porch = 3,
        v_sync_pulse  = 7,
        v_back_porch  = 20),
    '1280x768@60Hz CVT-RB': VGATiming(
        x             = 1280,
        y             = 768,
        refresh_rate  = 60.0,
        pixel_freq    = 68_250_000,
        h_front_porch = 48,
        h_sync_pulse  = 32,
        h_back_porch  = 80,
        v_front_porch = 3,
        v_sync_pulse  = 7,
        v_back_porch  = 12),
    '1280x800@60Hz': VGATiming(
        x             = 1280,
        y             = 800,
        refresh_rate  = 60.0,
        pixel_freq    = 83_500_000,
        h_front_porch = 72,
        h_sync_pulse  = 128,
        h_back_porch  = 200,
        v_front_porch = 3,
        v_sync_pulse  = 6,
        v_back_porch  = 22),
    '1280x800@60Hz CVT-RB': VGATiming(
        x             = 1280,
        y             = 800,
        refresh_rate  = 60.0,
        pixel_freq    = 71_000_000,
        h_front_porch = 48,
        h_sync_pulse  = 32,
        h_back_porch  = 80,
        v_front_porch = 3,
        v_sync_pulse  = 6,
        v_back_porch  = 14),
    '1280x1024@60Hz': VGATiming(
        x             = 1280,
        y             = 1024,
        refresh_rate  = 60.0,
        pixel_freq    = 108e6,
        h_front_porch = 48,
        h_sync_pulse  = 112,
        h_back_porch  = 248,
        v_front_porch = 1,
        v_sync_pulse  = 3,
        v_back_porch  = 38),
    '1366x768@60Hz': VGATiming(
        x             = 1366,
        y             = 768,
        refresh_rate  = 60.0,
        pixel_freq    = 85_500_000,
        h_front_porch = 70,
        h_sync_pulse  = 143,
        h_back_porch  = 213,
        v_front_porch = 3,
        v_sync_pulse  = 3,
        v_back_porch  = 24),
    '1920x1080@30Hz': VGATiming(
        x             = 1920,
        y             = 1080,
        refresh_rate  = 30.0,
        pixel_freq    = 148_500_000//2,
        h_front_porch = 88,
        h_sync_pulse  = 44,
        h_back_porch  = 148,
        v_front_porch = 4,
        v_sync_pulse  = 5,
        v_back_porch  = 36),
    '1920x1080@30Hz CVT-RB': VGATiming(
        x             = 1920,
        y             = 1080,
        refresh_rate  = 30.0,
        pixel_freq    = 73_000_000,
        h_front_porch = 48,
        h_sync_pulse  = 32,
        h_back_porch  = 80,
        v_front_porch = 3,
        v_sync_pulse  = 5,
        v_back_porch  = 9),
    '1920x1080@30Hz CVT-RB2': VGATiming(
        x             = 1920,
        y             = 1080,
        refresh_rate  = 30.0,
        pixel_freq    = 70_208_000,
        h_front_porch = 8,
        h_sync_pulse  = 32,
        h_back_porch  = 40,
        v_front_porch = 3,
        v_sync_pulse  = 8,
        v_back_porch  = 6),
    '1920x1080@60Hz': VGATiming(
        x             = 1920,
        y             = 1080,
        refresh_rate  = 60.0,
        pixel_freq    = 148_500_000,
        h_front_porch = 88,
        h_sync_pulse  = 44,
        h_back_porch  = 148,
        v_front_porch = 4,
        v_sync_pulse  = 5,
        v_back_porch  = 36),
}

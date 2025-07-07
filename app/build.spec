# -*- mode: python ; coding: utf-8 -*-
import sys
import os

block_cipher = None

# Determine Playwright browser path based on platform
if sys.platform == "win32":
    # Windows Playwright Chromium path example with user 'gamalabdelnasser'
    playwright_path = r'C:\\Users\\gamalabdelnasser\\AppData\\Local\\ms-playwright\\chromium-*\\chrome-win\\chrome.exe'
elif sys.platform == "darwin":
    # macOS Playwright Chromium path example with user 'gamalabdelnasser'
    home = os.path.expanduser("~")
    playwright_path = os.path.join(home, 'Library', 'Caches', 'ms-playwright', 'chromium-*', 'chrome-mac', 'Chromium.app')
else:
    # Linux or other platforms - adjust as needed
    playwright_path = None

datas = [
    ('templates/*', 'templates'),
    ('static/*', 'static'),
]

if playwright_path:
    datas.append((playwright_path, 'playwright'))

a = Analysis(
    ['main...py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'app',
        'app.views',
        'app.config',
        'playwright',
        'flask',
        'bs4',
        'werkzeug',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GoogleMapsScraper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

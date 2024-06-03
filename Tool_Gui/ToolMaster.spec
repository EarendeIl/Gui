# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['D:\\Tool_Gui\\Perfect_Gui\\new_gui.py'],
    pathex=['D:\\Tool_Gui\\Perfecert_Gui'],
    binaries=[],
    datas=[
        ('Perfect_Gui/data/bb.png', 'data'),
        ('Perfect_Gui/data/bug.png', 'data'),
        ('Perfect_Gui/data/lala.png', 'data'),
        ('Perfect_Gui/data/map.png', 'data'),
        ('Perfect_Gui/data/other.png', 'data'),
        ('Perfect_Gui/data/performance.png', 'data'),
        ('Perfect_Gui/data/powerful.png', 'data'),
        ('Perfect_Gui/data/report.png', 'data'),
        ('Perfect_Gui/data/tools.png', 'data'),
        ('Perfect_Gui/data/map_location.html', 'data'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,

)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ToolMaster',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Perfect_Gui\\data\\powerful.ico'  # 这里指定图标文件

)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ToolMaster',
)

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

addedFiles = [
('GlobEnModes/__init__.py', 'GlobEnModes'),
('GlobGamChrom/__init__.py', 'GlobGamChrom'),
('GlobGamFonds/__init__.py', 'GlobGamFonds'),
('GlobGamMicro/__init__.py', 'GlobGamMicro'),
('GlobGamSim/__init__.py', 'GlobGamSim'),
('GlobGamVers6/__init__.py', 'GlobGamVers6'),
('GlobInverseAcc/__init__.py', 'GlobInverseAcc'),
('GlobModelGammy/__init__.py', 'GlobModelGammy'),
('GlobTetraCord/__init__.py', 'GlobTetraCord'),
('GlobalTexte/CommentGlobGamChrom.txt', 'GlobalTexte'),
('GlobalTexte/CommentGlobGamChromII.txt', 'GlobalTexte'),
('GlobalTexte/couleursethexa.txt', 'GlobalTexte'),
('GlobalTexte/glob_datagams.txt', 'GlobalTexte'),
('GlobalTexte/globdic_Dana.txt', 'GlobalTexte'),
('GlobalTexte/globdicTcode.txt', 'GlobalTexte'),
('GlobalTexte/globdicTcord.txt', 'GlobalTexte'),
('GlobalTexte/globdicTcoup.txt', 'GlobalTexte'),
('GlobalTexte/globdicTgams.txt', 'GlobalTexte'),
('GlobalTexte/RunGlobalApplisPy22012022PLUS.txt', 'GlobalTexte'),
('GlobalTexte/RésultatRunGlobalApplisPy_1.txt', 'GlobalTexte'),
('GlobalDoc/calcul_tare_gam.py', 'GlobalDoc'),
('GlobalDoc/Contemplation_alteration_1', 'GlobalDoc'),
('GlobalDoc/Contemplation_alteration_2', 'GlobalDoc'),
('GlobalDoc/Definition_modules', 'GlobalDoc'),
('GlobalDoc/Notes Analyses', 'GlobalDoc'),
('a1.wav', '.'), ('a2.wav', '.'), ('a3.wav', '.'), ('a4.wav', '.'), ('a5.wav', '.'),
('a6.wav', '.'), ('a7.wav', '.'), ('acc1.wav', '.'), ('acc2.wav', '.'), ('acc3.wav', '.'),
('acc4.wav', '.'), ('acc5.wav', '.'), ('acc6.wav', '.'), ('acc7.wav', '.'),
('p_w1.wav', '.'), ('p_w2.wav', '.')]

a = Analysis(
    ['GlobalApplis.spec'],
    pathex=[],
    binaries=[],
    datas=addedFiles,
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='GlobalApplis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GlobalApplis',
)

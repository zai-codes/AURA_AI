def test_main_runs():
    import pathlib
    import importlib.util

    root = pathlib.Path(__file__).resolve().parents[1]
    candidates = list(root.rglob('aura_main.py'))
    if not candidates:
        raise FileNotFoundError('aura_main.py not found in workspace')
    p = candidates[0]

    spec = importlib.util.spec_from_file_location("aura_main", str(p))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, 'main'):
        module.main()

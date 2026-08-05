import pathlib
import py_compile

root = pathlib.Path('D:/AGI/pygiga')
errors = []
for path in sorted(root.rglob('*.py')):
    try:
        py_compile.compile(str(path), doraise=True)
    except Exception as exc:
        errors.append((str(path), str(exc)))

print('ERROR_COUNT:', len(errors))
for path, err in errors:
    print('FILE:', path)
    print('ERR:', err)

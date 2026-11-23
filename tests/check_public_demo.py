"""Fail-fast public showcase policy checks. No external dependency."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent.parent
text=(ROOT/'index.html').read_text('utf-8')
files=[p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
assert '<!doctype html>' in text.lower()
assert 'NO REAL HOUSEHOLD DATA' not in text  # selector replaced the original ribbon
assert 'ALL DATA IS FICTIONAL' in text
assert "connect-src 'none'" in text
assert "throw new Error('This preview is offline. External requests are blocked.')" in text
assert "id=\"demo-member\"" in text
assert 'No real household data' not in text
for real in ['C:' + chr(92) + 'Users' + chr(92), '192.168.', 'hub.home.arpa', 'password_hash=', 'session_token=']:
    assert not any(real.casefold() in p.read_text('utf-8').casefold() for p in files if p.suffix in ('.html','.md')), f'private string {real}'
for f in files:
    assert f.suffix.lower() not in {'.db','.sqlite','.pem','.key','.pfx','.p12','.crt','.zip','.bak','.log','.jpg','.jpeg','.png'}
assert len(re.findall(r"name:'(?:Alex|Morgan|Riley)'", text))==3
print('PUBLIC DEMO RELEASE AUDIT PASS:',len(files),'text files, 3 fictional personas, no known private strings')

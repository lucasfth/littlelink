"""Run with: python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Tags(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class RedirectTests(unittest.TestCase):
    def test_redirects_work_without_javascript_and_declare_destination(self):
        pages = sorted(ROOT.glob('*/index.html'))
        redirects = 0
        for page in pages:
            source = page.read_text()
            match = re.search(r'window\.location\.replace\("([^"]+)"\)', source)
            if not match:
                continue
            redirects += 1
            destination = match[1]
            tags = Tags(source).tags
            with self.subTest(page=str(page.relative_to(ROOT))):
                self.assertTrue(any(tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh'
                                    and attrs.get('content') == '0;url=' + destination
                                    for tag, attrs in tags), 'Missing immediate non-JavaScript redirect')
                self.assertTrue(any(tag == 'link' and attrs.get('rel') == 'canonical'
                                    and attrs.get('href') == destination for tag, attrs in tags),
                                'Canonical must point to the real destination')
                self.assertTrue(any(tag == 'a' and attrs.get('href') == destination
                                    for tag, attrs in tags), 'Missing clickable fallback')
        self.assertEqual(redirects, 12, 'All existing redirect aliases must be checked')


if __name__ == '__main__':
    unittest.main()

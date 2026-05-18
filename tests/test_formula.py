"""Tests for homebrew-vectrade formula validation."""

import re
from pathlib import Path

import pytest

FORMULA_DIR = Path(__file__).parent.parent / "Formula"
FORMULA_FILE = FORMULA_DIR / "vectrade.rb"


@pytest.fixture
def formula_content():
    """Load formula content."""
    return FORMULA_FILE.read_text()


@pytest.fixture
def formula_lines(formula_content):
    """Split formula into lines."""
    return formula_content.strip().splitlines()


class TestFormulaExists:
    """Verify formula file exists and is readable."""

    def test_formula_directory_exists(self):
        assert FORMULA_DIR.is_dir(), "Formula/ directory must exist"

    def test_formula_file_exists(self):
        assert FORMULA_FILE.is_file(), "Formula/vectrade.rb must exist"

    def test_formula_not_empty(self, formula_content):
        assert len(formula_content.strip()) > 0, "Formula must not be empty"


class TestFormulaStructure:
    """Verify formula follows Homebrew conventions."""

    def test_has_class_definition(self, formula_content):
        assert re.search(r"^class Vectrade < Formula$", formula_content, re.MULTILINE)

    def test_class_name_matches_filename(self, formula_content):
        match = re.search(r"^class (\w+) < Formula$", formula_content, re.MULTILINE)
        assert match, "Must have a class inheriting Formula"
        class_name = match.group(1)
        expected = FORMULA_FILE.stem.capitalize()
        assert class_name == expected, f"Class {class_name} must match file {FORMULA_FILE.stem}"

    def test_has_desc(self, formula_content):
        assert re.search(r'^\s+desc\s+"[^"]+"', formula_content, re.MULTILINE)

    def test_has_homepage(self, formula_content):
        assert re.search(r'^\s+homepage\s+"https?://[^"]+"', formula_content, re.MULTILINE)

    def test_has_version(self, formula_content):
        assert re.search(r'^\s+version\s+"[\d.]+"', formula_content, re.MULTILINE)

    def test_has_license(self, formula_content):
        assert re.search(r'^\s+license\s+"[^"]+"', formula_content, re.MULTILINE)

    def test_has_url(self, formula_content):
        assert re.search(r'^\s+url\s+"https?://[^"]+"', formula_content, re.MULTILINE)

    def test_has_sha256(self, formula_content):
        assert re.search(r'^\s+sha256\s+"[^"]+"', formula_content, re.MULTILINE)

    def test_has_install_method(self, formula_content):
        assert re.search(r"^\s+def install$", formula_content, re.MULTILINE)

    def test_has_test_block(self, formula_content):
        assert re.search(r"^\s+test do$", formula_content, re.MULTILINE)

    def test_install_has_bin_install(self, formula_content):
        assert re.search(r'bin\.install\s+"vectrade"', formula_content)

    def test_ends_with_end(self, formula_lines):
        assert formula_lines[-1].strip() == "end"


class TestFormulaMetadata:
    """Verify formula metadata is correct."""

    def test_desc_mentions_vectrade(self, formula_content):
        match = re.search(r'desc\s+"([^"]+)"', formula_content)
        assert match
        assert "vectrade" in match.group(1).lower() or "VecTrade" in match.group(1)

    def test_homepage_is_vectrade_cli(self, formula_content):
        match = re.search(r'homepage\s+"([^"]+)"', formula_content)
        assert match
        assert "VecTrade-io/vectrade-cli" in match.group(1)

    def test_license_is_mit(self, formula_content):
        assert re.search(r'license\s+"MIT"', formula_content)

    def test_version_is_semver(self, formula_content):
        match = re.search(r'version\s+"([^"]+)"', formula_content)
        assert match
        version = match.group(1)
        assert re.match(r"^\d+\.\d+\.\d+$", version), f"Version {version} not semver"


class TestFormulaURLs:
    """Verify download URLs are correctly structured."""

    def test_urls_reference_github_releases(self, formula_content):
        urls = re.findall(r'url\s+"([^"]+)"', formula_content)
        for url in urls:
            assert "github.com/VecTrade-io/vectrade-cli/releases" in url

    def test_urls_use_version_interpolation(self, formula_content):
        urls = re.findall(r'url\s+"([^"]+)"', formula_content)
        for url in urls:
            assert "#{version}" in url, f"URL must use version interpolation: {url}"

    def test_has_darwin_urls(self, formula_content):
        assert re.search(r"on_macos", formula_content)

    def test_has_linux_urls(self, formula_content):
        assert re.search(r"on_linux", formula_content)

    def test_has_amd64_support(self, formula_content):
        assert re.search(r"on_intel", formula_content)

    def test_has_arm64_support(self, formula_content):
        assert re.search(r"on_arm", formula_content)

    def test_url_archive_format_tar_gz(self, formula_content):
        urls = re.findall(r'url\s+"([^"]+)"', formula_content)
        for url in urls:
            assert url.endswith(".tar.gz"), f"URL must end with .tar.gz: {url}"


class TestFormulaCompletions:
    """Verify shell completions are installed."""

    def test_bash_completion(self, formula_content):
        assert re.search(r"bash_completion\.install", formula_content)

    def test_zsh_completion(self, formula_content):
        assert re.search(r"zsh_completion\.install", formula_content)

    def test_fish_completion(self, formula_content):
        assert re.search(r"fish_completion\.install", formula_content)


class TestFormulaTestBlock:
    """Verify test block has meaningful assertions."""

    def test_test_block_checks_version(self, formula_content):
        # Extract test block
        test_match = re.search(r"test do(.+?)end\s*\nend", formula_content, re.DOTALL)
        assert test_match, "Must have test block"
        test_block = test_match.group(1)
        assert "version" in test_block, "Test must verify version"

    def test_test_block_checks_help(self, formula_content):
        test_match = re.search(r"test do(.+?)end\s*\nend", formula_content, re.DOTALL)
        assert test_match
        test_block = test_match.group(1)
        assert "--help" in test_block, "Test must verify --help"


class TestFormulaSyntax:
    """Verify Ruby syntax is valid."""

    def test_balanced_do_end(self, formula_content):
        do_count = len(re.findall(r"\bdo\b", formula_content))
        end_count = len(re.findall(r"\bend\b", formula_content))
        # class has one end, each do has one end
        assert end_count >= do_count, "Unbalanced do/end blocks"

    def test_no_trailing_whitespace(self, formula_lines):
        for i, line in enumerate(formula_lines, 1):
            assert line == line.rstrip(), f"Trailing whitespace on line {i}"

    def test_uses_two_space_indent(self, formula_content):
        indented_lines = re.findall(r"^( +)\S", formula_content, re.MULTILINE)
        for indent in indented_lines:
            assert len(indent) % 2 == 0, f"Indent '{indent}' is not a multiple of 2 spaces"

    def test_frozen_string_literal(self, formula_content):
        assert "frozen_string_literal: true" in formula_content

    def test_no_tabs(self, formula_content):
        assert "\t" not in formula_content, "Formula must not contain tabs"

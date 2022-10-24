"""Tests for deploying and upgrading a proxy."""
from pathlib import Path

from click.testing import CliRunner

from nile.cli import cli


RESOURCES_DIR = Path(__file__).parent / "resources"

def test_deploy_upgrade_proxy():
    script = RESOURCES_DIR / "scripts" / "deploy_upgrade_proxy.py"

    # Run test script
    result = CliRunner().invoke(cli, ["run", str(script)])
    assert result.exit_code == 0

    # Check script output
    assert "result 1234" in result.output

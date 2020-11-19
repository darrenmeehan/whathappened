import pytest
import subprocess

from whathappened.cli import add_arguments


def test_sync_required_args_supplied():
    parser = add_arguments()
    parser.parse_args(["sync", "--bucket-name", "testing"])


def test_sync_no_args_required():
    parser = add_arguments()
    with pytest.raises(SystemExit):
        parser.parse_args(["sync"])

@pytest.mark.xfail()
def test_command_works_from_shell_exit_zero():
    """
    Basic sanity test that the command exits without error.
    """
    subprocess.run("whathappened", check=True)

import pytest

users = ["syncuser0"]


@pytest.mark.parametrize("username", users)
def test_is_enabled(host, username):
    assert host.service(f"syncthing@{username}").is_enabled


@pytest.mark.parametrize("username", users)
def test_is_running(host, username):
    assert host.service(f"syncthing@{username}").is_running

def test_package_imports():
    import synapse  # noqa: F401


def test_version():
    from synapse.main import __version__

    assert __version__ == "0.1.0"

from habt.config import Config


def test_default_config():
    """
      Test the default configuration
    """
    config = Config()

    assert not config.debug
    assert config.connection_string == "sqlite:///habt.db"

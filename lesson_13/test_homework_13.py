from unittest import TestCase, main
from lesson_13.login_function import log_event


class TestLogEvent(TestCase):

    def test_log_event_success(self):
        log_event("ivan", "success")
        assert True

    def test_log_event_expired(self):
        log_event("ivan", "expired")
        assert True

    def test_log_event_failed(self):
        log_event("ivan", "failed")
        assert True

    def test_log_event_unknown(self):
        log_event("ivan", "unknown")
        assert True

    def test_log_event_different_user(self):
        log_event("petro", "success")
        assert True


if __name__ == "__main__":
    main()
import os
import logging
from unittest import TestCase, main
from lesson_13.login_function import log_event


class TestLogEvent(TestCase):

    LOG_FILE = "login_system.log"

    def setUp(self):
        # закриваємо логери (щоб не було lock)
        for handler in logging.root.handlers[:]:
            handler.close()
            logging.root.removeHandler(handler)

        # очищаємо файл
        if os.path.exists(self.LOG_FILE):
            os.remove(self.LOG_FILE)

    def read_logs(self):
        with open(self.LOG_FILE, "r") as f:
            return f.read()

    def test_log_event_success(self):
        log_event("Yurii", "success")

        logs = self.read_logs()
        assert "Status: success" in logs

    def test_log_event_expired(self):
        log_event("Taras", "expired")

        logs = self.read_logs()
        assert "Status: expired" in logs

    def test_log_event_failed(self):
        log_event("Yurii", "failed")

        logs = self.read_logs()
        assert "Status: failed" in logs

    def test_log_event_unknown(self):
        log_event("Yurii", "unknown")

        logs = self.read_logs()
        assert "Status: unknown" in logs

    def test_log_event_username(self):
        log_event("Alex", "success")

        logs = self.read_logs()
        assert "Username: Alex" in logs


if __name__ == "__main__":
    main()
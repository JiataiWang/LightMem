from types import SimpleNamespace
from unittest.mock import Mock

from lightmem.memory.lightmem import LightMemory


def test_offline_update_trigger_uses_supported_score_threshold():
    memory = LightMemory.__new__(LightMemory)
    memory.config = SimpleNamespace(index_strategy="embedding")
    memory.logger = Mock()
    received = {}

    def offline_update_all_entries(*, score_threshold, max_workers=5):
        received["score_threshold"] = score_threshold

    memory.offline_update_all_entries = offline_update_all_entries

    memory.offline_update([], offline_update_trigger=True)

    assert received["score_threshold"] == 0.8

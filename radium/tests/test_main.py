# -*- coding: utf-8 -*-
"""Module for testing."""

import asyncio
import io

import pytest

from src.functions import input_to_sha, loop_random_print, random_print

TEST_VAL = '12'
TEST_SHA = '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918'


def test_input_to_sha(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
):
    monkeypatch.setattr('sys.stdin', io.StringIO(TEST_VAL))
    input_to_sha()
    captured = capsys.readouterr()
    assert captured.out.strip().split('\n', 1)[1] == TEST_SHA


@pytest.fixture(name='tst_event_loop')
def event_loop():
    return asyncio.get_event_loop()


def test_random_print(
    capsys: pytest.CaptureFixture,
    tst_event_loop: pytest.fixture,
):
    tst_event_loop.run_until_complete(random_print(TEST_VAL))
    captured = capsys.readouterr()
    assert captured.out == TEST_VAL


def test_loop_random_print(capsys: pytest.CaptureFixture):
    text_list = ['1', '2', '3']
    loop_random_print(text_list)
    captured = capsys.readouterr()
    out = sorted(captured.out)
    assert out == text_list

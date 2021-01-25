# -*- coding:utf-8 -*-

"""Test files module."""

import logging
import tempfile
from filecmp import dircmp

import pytest

from page_loader import files, log


def test_save_html_exception(caplog, response):
    """Test exception in save_html function."""
    caplog.set_level(logging.INFO)
    with pytest.raises(log.KnownError):
        assert files.save_html('/no_permission.html', response)


def test_save_data_exception(caplog, response):
    """Test exception in save_data function."""
    caplog.set_level(logging.INFO)
    with pytest.raises(log.KnownError):
        assert files.save_data('/no_permission.file', response)


def test_save_soup_exception(caplog, soup):
    """Test exception in save_soup function."""
    caplog.set_level(logging.INFO)
    with pytest.raises(log.KnownError):
        assert files.save_soup('/no_permission.html', soup)


def test_make_dir_exception(caplog):
    """Test exception in make_dir function."""
    caplog.set_level(logging.INFO)
    with pytest.raises(log.KnownError):
        assert files.make_dir('/no_permission')


def test_save_exception(caplog):
    """Test exception in save function."""
    caplog.set_level(logging.INFO)
    url = 'error'
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(log.KnownError):
            assert files.save(tmpdirname, url)


def test_save(caplog):
    """Test save function."""
    caplog.set_level(logging.INFO)
    url = 'https://andrka.github.io/page-loader-test'
    with tempfile.TemporaryDirectory() as tmpdirname:
        files.save(tmpdirname, url)
        compare = dircmp(tmpdirname, 'tests/fixtures')
        assert not compare.left_only
        assert not compare.right_only
        assert not compare.diff_files
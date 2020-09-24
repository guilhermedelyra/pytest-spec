# -*- coding: utf-8 -*-
"""Module contains command line option definition and logic needed to enable new formatting.

:author: Pawel Chomicki
"""
from .replacer import logstart_replacer, report_replacer, modifyitems_replacer


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--spec',
        action='store_true',
        dest='spec',
        help='Print test result in specification format'
    )

    # register config options
    parser.addini(
        'spec_header_format',
        default='{module_path}:',
        help='The format of the test headers when using the spec plugin'
    )
    parser.addini(
        'spec_test_format',
        default='{result} {name}',
        help='The format of the test results when using the spec plugin'
    )
    parser.addini(
        'spec_success_indicator',
        default='✓',
        help='The indicator displayed when a test passes'
    )
    parser.addini(
        'spec_failure_indicator',
        default='✗',
        help='The indicator displayed when a test fails'
    )
    parser.addini(
        'spec_skipped_indicator',
        default='?',
        help='The indicator displayed when a test is skipped'
    )
    parser.addini(
        'spec_indent',
        default='  ',
        help='The string used for indentation in the spec output'
    )


def pytest_configure(config):
    if getattr(config.option, 'spec', 0) and not getattr(config.option, 'quiet', 0) and not getattr(config.option, 'verbose', 0):
        import imp
        import _pytest
        _pytest.terminal.TerminalReporter.pytest_runtest_logstart = logstart_replacer
        _pytest.terminal.TerminalReporter.pytest_runtest_logreport = report_replacer
        _pytest.terminal.TerminalReporter.pytest_collection_modifyitems = modifyitems_replacer
        imp.reload(_pytest)

# SPDX-License-Identifier: GPL-2.0
# Copyright (c) 2015 Stephen Warren
# Copyright (c) 2015-2016, NVIDIA CORPORATION. All rights reserved.

import pytest
import signal

@pytest.mark.boardspec('sandbox')
@pytest.mark.buildconfigspec('sysreset_cmd_poweroff')
def test_poweroff(u_boot_console):
    """Test that the "poweroff" command exits sandbox process."""

    u_boot_console.run_command('poweroff', wait_for_prompt=False)
    assert(u_boot_console.validate_exited())

@pytest.mark.boardspec('sandbox')
def test_ctrl_c(u_boot_console):
    """Test that sending SIGINT to sandbox causes it to exit."""

    u_boot_console.kill(signal.SIGINT)
    assert(u_boot_console.validate_exited())

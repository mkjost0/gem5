# Copyright (c) 2022 The Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from testlib import *

"""
These tests are designed to test the BaseCPUProcessor. It utilizes the
tests/gem5/configs/simple_binary_run.py to run a simple SE-mode simualation
with different configurations of the BaseCPUProcessor.
"""

verifiers = (verifier.MatchStdoutNoPerf(joinpath(getcwd(), "ref", "simout")),)


gem5_verify_config(
    name="simulator-exit-event-handler-with-function-list",
    verifiers=verifiers,
    fixtures=(),
    config=joinpath(
        config.base_dir,
        "tests",
        "gem5",
        "stdlib",
        "configs",
        "simulator_exit_event_run.py",
    ),
    config_args=["-e", "function-list"],
    valid_isas=(constants.all_compiled_tag,),
    length=constants.quick_tag,
)

gem5_verify_config(
    name="simulator-exit-event-handler-with-generator",
    verifiers=verifiers,
    fixtures=(),
    config=joinpath(
        config.base_dir,
        "tests",
        "gem5",
        "stdlib",
        "configs",
        "simulator_exit_event_run.py",
    ),
    config_args=["-e", "generator"],
    valid_isas=(constants.all_compiled_tag,),
    length=constants.quick_tag,
)

gem5_verify_config(
    name="simulator-exit-event-handler-with-lone-function",
    verifiers=verifiers,
    fixtures=(),
    config=joinpath(
        config.base_dir,
        "tests",
        "gem5",
        "stdlib",
        "configs",
        "simulator_exit_event_run.py",
    ),
    config_args=["-e", "function"],
    valid_isas=(constants.all_compiled_tag,),
    length=constants.quick_tag,
)
